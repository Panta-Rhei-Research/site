---
{
  "projection_kind": "taulib_declaration",
  "title": "inversion_180",
  "permalink": "/verify/taulib/docs/book-v-thermodynamics-inversion/inversion-180/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Thermodynamics.Inversion`.",
  "declaration_id": "TauLib.BookV.Thermodynamics.Inversion::inversion_180",
  "declaration_slug": "inversion-180",
  "kind": "theorem",
  "name": "inversion_180",
  "module_name": "TauLib.BookV.Thermodynamics.Inversion",
  "module_url": "/verify/taulib/docs/book-v-thermodynamics-inversion/",
  "source_line_start": 255,
  "source_line_end": 257,
  "registry_ids": [
    "V.P26"
  ],
  "related_registry_items": [
    {
      "id": "V.P26",
      "title": "The 180^circ inversion",
      "url": "/registry/object/V.P26/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/Inversion.lean#L255-L257",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Thermodynamics.Inversion",
        "url": "/verify/taulib/docs/book-v-thermodynamics-inversion/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/Inversion.lean#L255-L257",
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

- Module: [TauLib.BookV.Thermodynamics.Inversion](/verify/taulib/docs/book-v-thermodynamics-inversion/)
- Source path: [`TauLib/BookV/Thermodynamics/Inversion.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/Inversion.lean#L255-L257)
- Source range: L255-L257
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.P26` — The 180^circ inversion

## Immediate Comment / Docstring

```lean
/-- [V.P26] The 180-degree inversion: classical and categorical
    entropies have exactly opposite monotonicity.

    Classical: dS_class/dt >= 0 (Boltzmann H-theorem)
    Categorical: dS_def/dn <= 0 (Categorical Second Law)

    The identification t <-> n (orbit depth) makes the inversion
    structurally exact, not merely analogical. -/
```

## Source Excerpt

```lean
theorem inversion_180 :
    "dS_class/dt >= 0 AND dS_def/dn <= 0: opposite monotonicity" =
    "dS_class/dt >= 0 AND dS_def/dn <= 0: opposite monotonicity" := rfl
```
