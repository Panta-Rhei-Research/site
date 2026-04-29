---
{
  "projection_kind": "taulib_declaration",
  "title": "affect_as_subsymbolic_pressure",
  "permalink": "/verify/taulib/docs/book-vii-logos-sector/affect-as-subsymbolic-pressure/",
  "summary_short": "`theorem` declaration in `TauLib.BookVII.Logos.Sector`.",
  "declaration_id": "TauLib.BookVII.Logos.Sector::affect_as_subsymbolic_pressure",
  "declaration_slug": "affect-as-subsymbolic-pressure",
  "kind": "theorem",
  "name": "affect_as_subsymbolic_pressure",
  "module_name": "TauLib.BookVII.Logos.Sector",
  "module_url": "/verify/taulib/docs/book-vii-logos-sector/",
  "source_line_start": 287,
  "source_line_end": 290,
  "registry_ids": [
    "VII.L15"
  ],
  "related_registry_items": [
    {
      "id": "VII.L15",
      "title": "Affect as Subsymbolic Pressure",
      "url": "/registry/object/VII.L15/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Logos/Sector.lean#L287-L290",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVII.Logos.Sector",
        "url": "/verify/taulib/docs/book-vii-logos-sector/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/verify/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Logos/Sector.lean#L287-L290",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
    }
  },
  "layout": "taulib-doc",
  "lane": "verify",
  "v2_lane": "verify",
  "status": "Canonical",
  "generated_from": "corpus/taulib-projections",
  "projection_version": "v0.1",
  "canonical_source": "Panta-Rhei-Research/taulib",
  "do_not_edit": true,
  "type": "TauLib Declaration"
}
---

## Declaration Projection

This page is generated directly from the pinned TauLib Lean source snapshot. The source excerpt is public because the active TauLib repository is public.

## Source Provenance

- Module: [TauLib.BookVII.Logos.Sector](/verify/taulib/docs/book-vii-logos-sector/)
- Source path: [`TauLib/BookVII/Logos/Sector.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Logos/Sector.lean#L287-L290)
- Source range: L287-L290
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `VII.L15` — Affect as Subsymbolic Pressure

## Immediate Comment / Docstring

```lean
/-- [VII.L15] Affect as Subsymbolic Pressure (ch116). Affect (the
    felt quality of emotion) is subsymbolic pressure at register
    boundaries. Below symbolic representation but causally
    efficacious through register-crossing dynamics. -/
```

## Source Excerpt

```lean
theorem affect_as_subsymbolic_pressure :
    canonical_sector_decomp.sector_count = 5 ∧
    canonical_sector_decomp.pure_sector_count = 4 :=
  ⟨rfl, rfl⟩
```
