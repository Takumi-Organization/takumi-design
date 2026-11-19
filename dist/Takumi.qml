// Generado desde tokens.json por scripts/generate.py. No editar a mano.
pragma Singleton
import QtQuick

QtObject {
    property bool oscuro: true
    readonly property var paletaOscura: ({
        fondo: "#000000",
        panel: "#080808",
        elevado: "#111111",
        tinta: "#f2f2f2",
        tintaSuave: "#c9c9c9",
        tintaApagada: "#8c8c8c",
        tintaTenue: "#4a4a4a",
        linea: "#1c1c1c",
        lineaAlta: "#3a3a3a",
        inversoFondo: "#f2f2f2",
        inversoTinta: "#000000",

    })
    readonly property var paletaClara: ({
        fondo: "#f4f4f4",
        panel: "#ffffff",
        elevado: "#ebebeb",
        tinta: "#0a0a0a",
        tintaSuave: "#333333",
        tintaApagada: "#6b6b6b",
        tintaTenue: "#b0b0b0",
        linea: "#e0e0e0",
        lineaAlta: "#c0c0c0",
        inversoFondo: "#0a0a0a",
        inversoTinta: "#f4f4f4",

    })
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
    readonly property int corteSm: 10
    readonly property int corteMd: 14
    readonly property int corteLg: 22
    readonly property int borde: 1
    readonly property string fuenteUi: "Outfit"
    readonly property string fuenteDatos: "JetBrains Mono"
    readonly property int rapido: 120
    readonly property int normal: 200
    readonly property int lento: 300
    readonly property var curva: [0.2, 0.7, 0.2, 1.0]
}
