---
{
  "projection_kind": "taulib_declaration",
  "title": "emotions_as_register_crossings",
  "permalink": "/verify/taulib/docs/book-vii-logos-sector/emotions-as-register-crossings/",
  "summary_short": "`theorem` declaration in `TauLib.BookVII.Logos.Sector`.",
  "declaration_id": "TauLib.BookVII.Logos.Sector::emotions_as_register_crossings",
  "declaration_slug": "emotions-as-register-crossings",
  "kind": "theorem",
  "name": "emotions_as_register_crossings",
  "module_name": "TauLib.BookVII.Logos.Sector",
  "module_url": "/verify/taulib/docs/book-vii-logos-sector/",
  "source_line_start": 274,
  "source_line_end": 277,
  "registry_ids": [
    "VII.T44"
  ],
  "related_registry_items": [
    {
      "id": "VII.T44",
      "title": "Emotions as Register-Crossings",
      "url": "/registry/object/VII.T44/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Logos/Sector.lean#L274-L277",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Logos/Sector.lean#L274-L277",
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
- Source path: [`TauLib/BookVII/Logos/Sector.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Logos/Sector.lean#L274-L277)
- Source range: L274-L277
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `VII.T44` — Emotions as Register-Crossings

## Immediate Comment / Docstring

```lean
/-- [VII.T44] Emotions as Register-Crossings (ch116). Emotions arise
    at register boundaries: they signal transitions between registers
    (E→P: fear, P→C: guilt, C→E: wonder). Each emotion type
    corresponds to a specific register-pair crossing. -/
```

## Source Excerpt

```lean
theorem emotions_as_register_crossings :
    canonical_sector_decomp.sector_count = 5 ∧
    canonical_sector_decomp.pure_sector_count = 4 :=
  ⟨rfl, rfl⟩
```
