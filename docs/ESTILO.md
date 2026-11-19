# Estilo visual Takumi (v1)

Fuente de verdad: `tokens.json`. Los ficheros de `dist/` se generan con `python3 scripts/generate.py`; no se editan a mano.
Origen: el logotipo de la organización (blanco/plata sobre negro, tajo diagonal) y la web `takumi-organization.github.io`.

## Principios
1. **Papel negro, tinta clara.** Fondo `#000`, tinta `#f2f2f2`. El modo claro («papel») es opcional; AMOLED = oscuro.
2. **Monocromo estricto.** Sin color de acento ni degradados de color, sin cristal ni desenfoque, sin sombras de neón. Todo se resuelve con luminancia.
3. **Trazo afilado.** Radio 0. La única curva permitida es ninguna: las esquinas se **cortan en diagonal** (esquina superior derecha), eco del tajo del logo.
4. **Tipografía fina y ancha.** Títulos en *Outfit* 200 con mucho espaciado en MAYÚSCULAS; datos y etiquetas en *JetBrains Mono*.
5. **El estado nunca va solo en color.** Icono + texto + peso; seleccionado = **inversión** (fondo tinta, texto fondo).
6. **Honestidad de datos.** Lo que no es de hoy o es una estimación se marca (borde discontinuo, «~», «estimado»).

## Tokens
| Rol | Oscuro | Claro |
|---|---|---|
| fondo | `#000000` | `#f4f4f4` |
| panel | `#080808` | `#ffffff` |
| elevado | `#111111` | `#ebebeb` |
| tinta / suave / apagada / tenue | `#f2f2f2` `#c9c9c9` `#8c8c8c` `#4a4a4a` | `#0a0a0a` `#333333` `#6b6b6b` `#b0b0b0` |
| línea / línea alta | `#1c1c1c` `#3a3a3a` | `#e0e0e0` `#c0c0c0` |

Corte diagonal: **10 / 14 / 22** (sm/md/lg). Borde: 1. Espaciado: 4·8·12·16·24·32·48·64·96.
Escala tipográfica: display 56/200/+0,26em · título 32/200 · sección 14/500/+0,22em MAYÚS · cuerpo 16/300 · pequeño 13/300 · etiqueta 12 mono MAYÚS · dato 14 mono.
Movimiento: 120 / 200 / 300 ms, revelado 800 ms, curva `cubic-bezier(.2,.7,.2,1)`. Sin rebotes.

## Componentes
- **Botón primario:** fondo tinta, texto fondo, corte md, etiqueta MAYÚSCULAS espaciada. **Secundario:** solo borde `lineaAlta`, sin corte.
- **Tarjeta/panel:** fondo `panel`, borde 1 `lineaAlta`, corte lg. Hover/pulsado: borde pasa a tinta.
- **Campo de texto:** fondo `#050505`, borde `lineaAlta`; foco = borde tinta (nada de brillo).
- **Selección / pestaña activa:** inversión de colores.
- **Lista:** filas separadas por `linea`; sin fondos alternos.
- **Gráficos:** escala de **grises** (`grises`), distinguir series con grosor, trazo (continuo/discontinuo/punteado) y marcadores, no con color.
- **Estados:** correcto `●`, aviso `▲`, error `✕` (o sus iconos de línea), siempre con texto. El error destaca con inversión, no con rojo.
- **Iconos:** línea fina (1,5 px), terminaciones rectas, sin relleno.
- **Icono de app:** la marca (`assets/marca-512.png`) sobre negro.

## Por plataforma
- **Android (Compose M3):** `TakumiColors.Oscuro/Claro` → `MaterialTheme(colorScheme=…)`; formas `TakumiShapes.CorteMd/Lg`; tipografías `TakumiType`; fuentes en `res/font`. Barra de estado/navegación negras.
- **Qt/QML (checkmate, PySide6):** singleton `Takumi.qml` (con `qmldir`); corte con `Shape`/`PathPolyline` o `Canvas`; sin `radius`.
- **Terminal (Ratatui):** `takumi.rs` con colores RGB; bordes `Borders::ALL` con `BorderType::Plain`; etiquetas en mayúsculas; seleccionado = vídeo inverso; sin colores ANSI de acento.
- **Web/Tauri/Angular/Svelte:** `takumi.css` (variables `--tk-*`) + `.tk-corte`; fuentes con `@fontsource/outfit` y `@fontsource/jetbrains-mono`.
- **Godot (juegos):** los juegos con dirección artística propia (p. ej. NULL//VEIL) **no se restilan**; sí sus menús y utilidades.

## Lista de conformidad (auditoría por app)
- [ ] Fondo y tinta de los tokens; ningún color fuera de la escala de grises.
- [ ] Sin radios: esquinas rectas o cortadas.
- [ ] Outfit + JetBrains Mono embebidas (licencia OFL incluida).
- [ ] Seleccionado/activo por inversión; estados con icono y texto.
- [ ] Gráficos en grises; sin degradados de color ni cristal.
- [ ] Icono de app = marca Takumi.
- [ ] Capturas reales actualizadas en el README.
- [ ] Contraste ≥ 4,5:1 para texto normal (tinta apagada solo en texto secundario ≥ 14 px).
