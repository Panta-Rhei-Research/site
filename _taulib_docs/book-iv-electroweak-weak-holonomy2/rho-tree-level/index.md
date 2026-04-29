---
{
  "projection_kind": "taulib_declaration",
  "title": "rho_tree_level",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-weak-holonomy2/rho-tree-level/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Electroweak.WeakHolonomy2`.",
  "declaration_id": "TauLib.BookIV.Electroweak.WeakHolonomy2::rho_tree_level",
  "declaration_slug": "rho-tree-level",
  "kind": "theorem",
  "name": "rho_tree_level",
  "module_name": "TauLib.BookIV.Electroweak.WeakHolonomy2",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-weak-holonomy2/",
  "source_line_start": 127,
  "source_line_end": 129,
  "registry_ids": [
    "IV.T56"
  ],
  "related_registry_items": [
    {
      "id": "IV.T56",
      "title": "Tree-Level Rho = 1",
      "url": "/registry/object/IV.T56/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakHolonomy2.lean#L127-L129",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.WeakHolonomy2",
        "url": "/verify/taulib/docs/book-iv-electroweak-weak-holonomy2/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakHolonomy2.lean#L127-L129",
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

- Module: [TauLib.BookIV.Electroweak.WeakHolonomy2](/verify/taulib/docs/book-iv-electroweak-weak-holonomy2/)
- Source path: [`TauLib/BookIV/Electroweak/WeakHolonomy2.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakHolonomy2.lean#L127-L129)
- Source range: L127-L129
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.T56` — Tree-Level Rho = 1

## Immediate Comment / Docstring

```lean
/-- [IV.T56] At tree level, rho = 1 exactly. This is a structural
    consequence of SU(2) custodial symmetry, which is automatic
    in the tau-framework (the crossing-point geometry preserves
    the SU(2) doublet structure). -/
```

## Source Excerpt

```lean
theorem rho_tree_level :
    rho_tree.numer = rho_tree.denom := by
  simp [rho_tree]
```
