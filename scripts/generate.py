#!/usr/bin/env python3
"""Genera dist/ desde tokens.json: CSS, Kotlin (Compose M3), QML, Rust (Ratatui) y JSON plano."""
import json, pathlib
R = pathlib.Path(__file__).resolve().parent.parent
T = json.loads((R / "tokens.json").read_text(encoding="utf-8"))
D = R / "dist"; D.mkdir(exist_ok=True)
C = T["color"]; E = T["forma"]; Y = T["tipo"]; M = T["movimiento"]
cap = lambda s: s[0].upper() + s[1:]
hexrgb = lambda h: tuple(int(h[i:i+2], 16) for i in (1, 3, 5))
cabecera = "Generado desde tokens.json por scripts/generate.py. No editar a mano."

# ---------- CSS ----------
def bloque(sel, c): return sel + " {\n" + "".join(f"  --tk-{k}: {v};\n" for k, v in c.items()) + "}\n"
css = f"/* {cabecera} */\n:root {{\n  --tk-corte-sm: {E['corte']['sm']}px; --tk-corte-md: {E['corte']['md']}px; --tk-corte-lg: {E['corte']['lg']}px;\n  --tk-radio: 0; --tk-borde: {E['borde']}px;\n  --tk-fuente-ui: \"{Y['familiaUi']}\", system-ui, sans-serif; --tk-fuente-datos: \"{Y['familiaDatos']}\", ui-monospace, monospace;\n  --tk-curva: cubic-bezier({', '.join(map(str, M['curva']))});\n  --tk-rapido: {M['rapido']}ms; --tk-normal: {M['normal']}ms; --tk-lento: {M['lento']}ms; --tk-revelado: {M['revelado']}ms;\n}}\n"
css += bloque(":root, :root[data-tema=\"oscuro\"]", C["oscuro"]) + bloque(":root[data-tema=\"claro\"]", C["claro"])
css += "@media (prefers-color-scheme: light) {\n" + bloque("  :root:not([data-tema])", C["claro"]).replace("\n", "\n").rstrip() + "\n}\n"
css += "/* Corte diagonal del logo: esquina superior derecha */\n.tk-corte { clip-path: polygon(0 0, calc(100% - var(--tk-corte-lg)) 0, 100% var(--tk-corte-lg), 100% 100%, 0 100%); }\n"
(D / "takumi.css").write_text(css, encoding="utf-8")

# ---------- Kotlin (Compose Material 3) ----------
def kt_scheme(nombre, c, oscuro):
    k = lambda h: "Color(0xFF" + h[1:].upper() + ")"
    return f"""    val {nombre} = {"darkColorScheme" if oscuro else "lightColorScheme"}(
        primary = {k(c['tinta'])}, onPrimary = {k(c['fondo'])},
        secondary = {k(c['tintaSuave'])}, onSecondary = {k(c['fondo'])},
        tertiary = {k(c['tintaApagada'])}, onTertiary = {k(c['fondo'])},
        background = {k(c['fondo'])}, onBackground = {k(c['tinta'])},
        surface = {k(c['panel'])}, onSurface = {k(c['tinta'])},
        surfaceVariant = {k(c['elevado'])}, onSurfaceVariant = {k(c['tintaApagada'])},
        surfaceContainer = {k(c['panel'])}, surfaceContainerHigh = {k(c['elevado'])},
        outline = {k(c['lineaAlta'])}, outlineVariant = {k(c['linea'])},
        error = {k(c['tinta'])}, onError = {k(c['fondo'])},
        inverseSurface = {k(c['inversoFondo'])}, inverseOnSurface = {k(c['inversoTinta'])},
    )
"""
ks = ""
for n, v in T["tipo"]["escala"].items():
    fam = "TakumiMono" if v.get("mono") else "TakumiUi"
    ks += f"        val {n} = TextStyle(fontFamily = {fam}, fontWeight = FontWeight({v['peso']}), fontSize = {v['tam']}.sp, letterSpacing = {v['espaciado']}.em, lineHeight = {round(v['tam']*1.5)}.sp)\n"
kt = f"""// {cabecera}
package dev.takumi.design

import androidx.compose.foundation.shape.CutCornerShape
import androidx.compose.material3.darkColorScheme
import androidx.compose.material3.lightColorScheme
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.TextStyle
import androidx.compose.ui.text.font.FontFamily
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.em
import androidx.compose.ui.unit.sp

/** Las dos familias hay que enlazarlas con los .ttf (OFL) de cada app: res/font/outfit_*.ttf y jetbrains_mono_*.ttf. */
lateinit var TakumiUi: FontFamily
lateinit var TakumiMono: FontFamily

object TakumiColors {{
{kt_scheme('Oscuro', C['oscuro'], True)}
{kt_scheme('Claro', C['claro'], False)}
    /** Escala de grises para gráficos: nunca se usa color para distinguir series. */
    val Grises = listOf({", ".join('Color(0xFF'+g[1:].upper()+')' for g in C['grises'])})
}}

object TakumiShapes {{
    /** Corte diagonal del logo en la esquina superior derecha. Radio 0 en el resto. */
    val CorteSm = CutCornerShape(topStart = 0.dp, topEnd = {E['corte']['sm']}.dp, bottomEnd = 0.dp, bottomStart = 0.dp)
    val CorteMd = CutCornerShape(topStart = 0.dp, topEnd = {E['corte']['md']}.dp, bottomEnd = 0.dp, bottomStart = 0.dp)
    val CorteLg = CutCornerShape(topStart = 0.dp, topEnd = {E['corte']['lg']}.dp, bottomEnd = 0.dp, bottomStart = 0.dp)
    val Recto = CutCornerShape(0.dp)
    val Borde = {E['borde']}.dp
}}

object TakumiType {{
{ks}}}

object TakumiMotion {{
    const val Rapido = {M['rapido']}; const val Normal = {M['normal']}; const val Lento = {M['lento']}; const val Revelado = {M['revelado']}
    val Curva = androidx.compose.animation.core.CubicBezierEasing({', '.join(f'{x}f' for x in M['curva'])})
}}
"""
(D / "Takumi.kt").write_text(kt, encoding="utf-8")

# ---------- QML ----------
def qml_colors(c): return "".join(f'        {k}: "{v}"\n' for k, v in c.items())
qml = f"""// {cabecera}
pragma Singleton
import QtQuick

QtObject {{
    property bool oscuro: true
    readonly property var paletaOscura: ({{
{qml_colors(C['oscuro']).replace('        ', '        ').replace(chr(10), ','+chr(10)).rstrip(',')}
    }})
    readonly property var paletaClara: ({{
{qml_colors(C['claro']).replace(chr(10), ','+chr(10)).rstrip(',')}
    }})
    readonly property var p: oscuro ? paletaOscura : paletaClara
    readonly property color fondo: p.fondo
    readonly property color panel: p.panel
    readonly property color elevado: p.elevado
    readonly property color tinta: p.tinta
    readonly property color tintaSuave: p.tintaSuave
    readonly property color tintaApagada: p.tintaApagada
    readonly property color tintaTenue: p.tintaTenue
    readonly property color linea: p.linea
    readonly property color lineaAlta: p.lineaAlta
    readonly property color inversoFondo: p.inversoFondo
    readonly property color inversoTinta: p.inversoTinta
    readonly property int corteSm: {E['corte']['sm']}
    readonly property int corteMd: {E['corte']['md']}
    readonly property int corteLg: {E['corte']['lg']}
    readonly property int borde: {E['borde']}
    readonly property string fuenteUi: "{Y['familiaUi']}"
    readonly property string fuenteDatos: "{Y['familiaDatos']}"
    readonly property int rapido: {M['rapido']}
    readonly property int normal: {M['normal']}
    readonly property int lento: {M['lento']}
    readonly property var curva: [{', '.join(map(str, M['curva']))}]
}}
"""
(D / "Takumi.qml").write_text(qml, encoding="utf-8")
(D / "qmldir").write_text("singleton Takumi 1.0 Takumi.qml\n", encoding="utf-8")

# ---------- Rust (Ratatui) ----------
rs = f"// {cabecera}\nuse ratatui::style::Color;\n\n"
for modo in ("oscuro", "claro"):
    rs += f"pub mod {modo} {{\n    use super::Color;\n"
    for k, v in C[modo].items():
        r, g, b = hexrgb(v)
        nombre = "".join("_" + ch.lower() if ch.isupper() else ch for ch in k).upper()
        rs += f"    pub const {nombre}: Color = Color::Rgb({r}, {g}, {b});\n"
    rs += "}\n\n"
rs += "pub const GRISES: [Color; %d] = [%s];\n" % (len(C["grises"]), ", ".join("Color::Rgb(%d, %d, %d)" % hexrgb(g) for g in C["grises"]))
rs += "pub const ESPACIADO_ETIQUETA: usize = 1; // las etiquetas van en MAYÚSCULAS y separadas\n"
(D / "takumi.rs").write_text(rs, encoding="utf-8")

# ---------- JSON plano ----------
(D / "tokens.flat.json").write_text(json.dumps(T, ensure_ascii=False, indent=1), encoding="utf-8")
print("dist/:", ", ".join(sorted(p.name for p in D.iterdir())))
