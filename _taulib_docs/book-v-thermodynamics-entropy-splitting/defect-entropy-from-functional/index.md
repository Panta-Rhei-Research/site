---
{
  "projection_kind": "taulib_declaration",
  "title": "DefectEntropyFromFunctional",
  "permalink": "/verify/taulib/docs/book-v-thermodynamics-entropy-splitting/defect-entropy-from-functional/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Thermodynamics.EntropySplitting`.",
  "declaration_id": "TauLib.BookV.Thermodynamics.EntropySplitting::DefectEntropyFromFunctional",
  "declaration_slug": "defect-entropy-from-functional",
  "kind": "structure",
  "name": "DefectEntropyFromFunctional",
  "module_name": "TauLib.BookV.Thermodynamics.EntropySplitting",
  "module_url": "/verify/taulib/docs/book-v-thermodynamics-entropy-splitting/",
  "source_line_start": 261,
  "source_line_end": 266,
  "registry_ids": [
    "V.P29"
  ],
  "related_registry_items": [
    {
      "id": "V.P29",
      "title": "Defect entropy from defect functional",
      "url": "/registry/object/V.P29/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/EntropySplitting.lean#L261-L266",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/EntropySplitting.lean#L261-L266",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
      "status": "defined"
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
- Source path: [`TauLib/BookV/Thermodynamics/EntropySplitting.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/EntropySplitting.lean#L261-L266)
- Source range: L261-L266
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.P29` — Defect entropy from defect functional

## Immediate Comment / Docstring

```lean
/-- [V.P29] Defect entropy from defect functional:
    S_def(n) = ln|supp(delta[omega]_n)| + O((ln n)/n).

    Links the path-counting definition to the 4-component
    defect functional from Book IV. -/
```

## Source Excerpt

```lean
structure DefectEntropyFromFunctional where
  /-- Defect support size at depth n. -/
  support_size : Nat
  /-- S_def ~ ln(support_size). -/
  entropy_log_approx : Bool := true
  deriving Repr
```
