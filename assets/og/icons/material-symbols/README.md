# Material Symbols SVGs

This directory contains the selected Material Symbols SVGs needed by the v4
OG/Twitter card pipeline.

The files are fetched from the official Google `material-design-icons`
repository by:

```sh
python3 scripts/fetch_material_symbols.py
```

The generator embeds the SVG path data into the produced cards, so public pages
do not load icons from Google Fonts, GitHub, or any CDN.
