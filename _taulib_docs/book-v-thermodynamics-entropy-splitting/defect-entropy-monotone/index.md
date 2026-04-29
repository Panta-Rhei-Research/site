---
{
  "projection_kind": "taulib_declaration",
  "title": "defect_entropy_monotone",
  "permalink": "/verify/taulib/docs/book-v-thermodynamics-entropy-splitting/defect-entropy-monotone/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Thermodynamics.EntropySplitting`.",
  "declaration_id": "TauLib.BookV.Thermodynamics.EntropySplitting::defect_entropy_monotone",
  "declaration_slug": "defect-entropy-monotone",
  "kind": "theorem",
  "name": "defect_entropy_monotone",
  "module_name": "TauLib.BookV.Thermodynamics.EntropySplitting",
  "module_url": "/verify/taulib/docs/book-v-thermodynamics-entropy-splitting/",
  "source_line_start": 190,
  "source_line_end": 191,
  "registry_ids": [
    "V.T58"
  ],
  "related_registry_items": [
    {
      "id": "V.T58",
      "title": "Defect entropy is monotonically decreasing",
      "url": "/registry/object/V.T58/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/EntropySplitting.lean#L190-L191",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Thermodynamics.EntropySplitting",
        "url": "/verify/taulib/docs/book-v-thermodynamics-entropy-splitting/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/EntropySplitting.lean#L190-L191",
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

- Module: [TauLib.BookV.Thermodynamics.EntropySplitting](/verify/taulib/docs/book-v-thermodynamics-entropy-splitting/)
- Source path: [`TauLib/BookV/Thermodynamics/EntropySplitting.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/EntropySplitting.lean#L190-L191)
- Source range: L190-L191
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T58` — Defect entropy is monotonically decreasing

## Immediate Comment / Docstring

```lean
/-- [V.T58] Defect entropy is monotonically decreasing:
    S_def(n+1) <= (1 - iota_tau) S_def(n).

    The contraction factor (1 - iota_tau) is the gravitational
    self-coupling, ensuring exponential convergence to zero. -/
```

## Source Excerpt

```lean
theorem defect_entropy_monotone :
    contraction_numer < contraction_denom := contraction_lt_one
```
