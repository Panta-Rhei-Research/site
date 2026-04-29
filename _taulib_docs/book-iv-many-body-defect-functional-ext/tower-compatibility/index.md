---
{
  "projection_kind": "taulib_declaration",
  "title": "TowerCompatibility",
  "permalink": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext/tower-compatibility/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.ManyBody.DefectFunctionalExt`.",
  "declaration_id": "TauLib.BookIV.ManyBody.DefectFunctionalExt::TowerCompatibility",
  "declaration_slug": "tower-compatibility",
  "kind": "structure",
  "name": "TowerCompatibility",
  "module_name": "TauLib.BookIV.ManyBody.DefectFunctionalExt",
  "module_url": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext/",
  "source_line_start": 264,
  "source_line_end": 271,
  "registry_ids": [
    "IV.T89"
  ],
  "related_registry_items": [
    {
      "id": "IV.T89",
      "title": "Tower compatibility",
      "url": "/registry/object/IV.T89/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L264-L271",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.ManyBody.DefectFunctionalExt",
        "url": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L264-L271",
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

- Module: [TauLib.BookIV.ManyBody.DefectFunctionalExt](/verify/taulib/docs/book-iv-many-body-defect-functional-ext/)
- Source path: [`TauLib/BookIV/ManyBody/DefectFunctionalExt.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L264-L271)
- Source range: L264-L271
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.T89` — Tower compatibility

## Immediate Comment / Docstring

```lean
/-- [IV.T89] Tower compatibility: restriction of delta_{n+1} to the
    coarser partition recovers delta_n exactly:
    delta_{n+1}[omega]|_n(C_{n,a}) = sum_b delta_{n+1}[omega](C_{n+1,a+b*p_n#})
                                   = delta_n[omega](C_{n,a}).

    This ensures coherence of the defect functional across primorial depths
    and is the structural prerequisite for the projective limit. -/
```

## Source Excerpt

```lean
structure TowerCompatibility where
  /-- Restriction to coarser partition recovers coarser functional. -/
  restriction_recovers : Bool := true
  /-- Coherence across all depths. -/
  coherent_all_depths : Bool := true
  /-- Prerequisite for projective limit. -/
  enables_proj_limit : Bool := true
  deriving Repr
```
