---
{
  "projection_kind": "taulib_declaration",
  "title": "s_def_zero_at_horizon",
  "permalink": "/verify/taulib/docs/book-iv-physics-thermodynamics/s-def-zero-at-horizon/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Physics.Thermodynamics`.",
  "declaration_id": "TauLib.BookIV.Physics.Thermodynamics::s_def_zero_at_horizon",
  "declaration_slug": "s-def-zero-at-horizon",
  "kind": "theorem",
  "name": "s_def_zero_at_horizon",
  "module_name": "TauLib.BookIV.Physics.Thermodynamics",
  "module_url": "/verify/taulib/docs/book-iv-physics-thermodynamics/",
  "source_line_start": 218,
  "source_line_end": 219,
  "registry_ids": [
    "IV.R05"
  ],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/Thermodynamics.lean#L218-L219",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Physics.Thermodynamics",
        "url": "/verify/taulib/docs/book-iv-physics-thermodynamics/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/Thermodynamics.lean#L218-L219",
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

- Module: [TauLib.BookIV.Physics.Thermodynamics](/verify/taulib/docs/book-iv-physics-thermodynamics/)
- Source path: [`TauLib/BookIV/Physics/Thermodynamics.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/Thermodynamics.lean#L218-L219)
- Source range: L218-L219
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [IV.R05] S_def = 0 at coherence horizon: when s_def_numer = 0,
    the defect entropy numerator vanishes. -/
```

## Source Excerpt

```lean
theorem s_def_zero_at_horizon (e : EntropySplitting)
    (h : e.s_def_numer = 0) : e.s_def_numer = 0 := h
```
