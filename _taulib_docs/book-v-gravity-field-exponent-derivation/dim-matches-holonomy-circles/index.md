---
{
  "projection_kind": "taulib_declaration",
  "title": "dim_matches_holonomy_circles",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-exponent-derivation/dim-matches-holonomy-circles/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.GravityField.ExponentDerivation`.",
  "declaration_id": "TauLib.BookV.GravityField.ExponentDerivation::dim_matches_holonomy_circles",
  "declaration_slug": "dim-matches-holonomy-circles",
  "kind": "theorem",
  "name": "dim_matches_holonomy_circles",
  "module_name": "TauLib.BookV.GravityField.ExponentDerivation",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-exponent-derivation/",
  "source_line_start": 134,
  "source_line_end": 135,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/ExponentDerivation.lean#L134-L135",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.GravityField.ExponentDerivation",
        "url": "/verify/taulib/docs/book-v-gravity-field-exponent-derivation/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/ExponentDerivation.lean#L134-L135",
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

- Module: [TauLib.BookV.GravityField.ExponentDerivation](/verify/taulib/docs/book-v-gravity-field-exponent-derivation/)
- Source path: [`TauLib/BookV/GravityField/ExponentDerivation.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/ExponentDerivation.lean#L134-L135)
- Source range: L134-L135
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- dim(τ³) = 3 matches the circle count in the holonomy correction.
    This is the L3 connection: the SAME invariant gives π³ and one
    factor of the exponent 18. -/
```

## Source Excerpt

```lean
theorem dim_matches_holonomy_circles :
    canonical_factors.dim_tau3 = triple_holonomy.circle_count := by rfl
```
