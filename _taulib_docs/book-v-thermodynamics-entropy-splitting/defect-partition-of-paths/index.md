---
{
  "projection_kind": "taulib_declaration",
  "title": "DefectPartitionOfPaths",
  "permalink": "/verify/taulib/docs/book-v-thermodynamics-entropy-splitting/defect-partition-of-paths/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Thermodynamics.EntropySplitting`.",
  "declaration_id": "TauLib.BookV.Thermodynamics.EntropySplitting::DefectPartitionOfPaths",
  "declaration_slug": "defect-partition-of-paths",
  "kind": "structure",
  "name": "DefectPartitionOfPaths",
  "module_name": "TauLib.BookV.Thermodynamics.EntropySplitting",
  "module_url": "/verify/taulib/docs/book-v-thermodynamics-entropy-splitting/",
  "source_line_start": 68,
  "source_line_end": 79,
  "registry_ids": [
    "V.D85"
  ],
  "related_registry_items": [
    {
      "id": "V.D85",
      "title": "Defect partition of paths",
      "url": "/registry/object/V.D85/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/EntropySplitting.lean#L68-L79",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/EntropySplitting.lean#L68-L79",
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
- Source path: [`TauLib/BookV/Thermodynamics/EntropySplitting.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/EntropySplitting.lean#L68-L79)
- Source range: L68-L79
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D85` — Defect partition of paths

## Immediate Comment / Docstring

```lean
/-- [V.D85] Defect partition of paths at orbit depth n.

    CR-compatible paths of bounded length are partitioned into:
    - defect-traversing (passing through defect sites)
    - defect-free (avoiding all defect sites)

    The partition is exhaustive at every orbit depth. -/
```

## Source Excerpt

```lean
structure DefectPartitionOfPaths where
  /-- Orbit depth. -/
  depth : Nat
  /-- Number of defect-traversing paths (up to length bound). -/
  p_def : Nat
  /-- Number of defect-free paths (up to length bound). -/
  p_free : Nat
  /-- Total paths = defect + free. -/
  total : Nat
  /-- Partition is exhaustive. -/
  exhaustive : total = p_def + p_free
  deriving Repr
```
