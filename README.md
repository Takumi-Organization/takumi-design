# takumi-design

Sistema de diseño de **Takumi Organization**: tokens y guía de estilo para todas las aplicaciones propias (móvil, escritorio y terminal).

- `tokens.json` — fuente de verdad.
- `docs/ESTILO.md` — principios, componentes por plataforma y lista de conformidad.
- `dist/` — generado: `takumi.css`, `Takumi.kt` (Compose M3), `Takumi.qml` + `qmldir`, `takumi.rs` (Ratatui), `tokens.flat.json`.
- `assets/` — marca y logotipo.

```bash
python3 scripts/generate.py   # regenera dist/
```

Verificado al generar: el Rust compila y corre contra Ratatui 0.30 y el QML pasa `qmllint`. El Kotlin se verifica al aplicarlo en cada app.
Licencia: MIT. Las fuentes Outfit y JetBrains Mono son OFL.
