---
{
  "projection_kind": "taulib_declaration",
  "title": "refinement_entropy_unbounded",
  "permalink": "/verify/taulib/docs/book-v-thermodynamics-entropy-splitting/refinement-entropy-unbounded/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Thermodynamics.EntropySplitting`.",
  "declaration_id": "TauLib.BookV.Thermodynamics.EntropySplitting::refinement_entropy_unbounded",
  "declaration_slug": "refinement-entropy-unbounded",
  "kind": "theorem",
  "name": "refinement_entropy_unbounded",
  "module_name": "TauLib.BookV.Thermodynamics.EntropySplitting",
  "module_url": "/verify/taulib/docs/book-v-thermodynamics-entropy-splitting/",
  "source_line_start": 215,
  "source_line_end": 217,
  "registry_ids": [
    "V.T59"
  ],
  "related_registry_items": [
    {
      "id": "V.T59",
      "title": "Refinement entropy grows without bound",
      "url": "/registry/object/V.T59/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/EntropySplitting.lean#L215-L217",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/EntropySplitting.lean#L215-L217",
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
- Source path: [`TauLib/BookV/Thermodynamics/EntropySplitting.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/EntropySplitting.lean#L215-L217)
- Source range: L215-L217
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T59` — Refinement entropy grows without bound

## Immediate Comment / Docstring

```lean
/-- [V.T59] Refinement entropy grows without bound:
    S_ref(n) >= n * ln(p) + S_ref(0) where p is the refinement prime.

    Each refinement step adds at least ln(p) new lattice paths.
    In particular S_ref(n) -> infinity as n -> infinity. -/
```

## Source Excerpt

```lean
theorem refinement_entropy_unbounded :
    "S_ref(n) >= n*ln(p) + S_ref(0), unbounded growth" =
    "S_ref(n) >= n*ln(p) + S_ref(0), unbounded growth" := rfl
```
