---
{
  "projection_kind": "taulib_declaration",
  "title": "weak_gauge_su2",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-weak-holonomy/weak-gauge-su2/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Electroweak.WeakHolonomy`.",
  "declaration_id": "TauLib.BookIV.Electroweak.WeakHolonomy::weak_gauge_su2",
  "declaration_slug": "weak-gauge-su2",
  "kind": "theorem",
  "name": "weak_gauge_su2",
  "module_name": "TauLib.BookIV.Electroweak.WeakHolonomy",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-weak-holonomy/",
  "source_line_start": 204,
  "source_line_end": 208,
  "registry_ids": [
    "IV.T52"
  ],
  "related_registry_items": [
    {
      "id": "IV.T52",
      "title": "Weak Gauge Group",
      "url": "/registry/object/IV.T52/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakHolonomy.lean#L204-L208",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.WeakHolonomy",
        "url": "/verify/taulib/docs/book-iv-electroweak-weak-holonomy/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakHolonomy.lean#L204-L208",
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

- Module: [TauLib.BookIV.Electroweak.WeakHolonomy](/verify/taulib/docs/book-iv-electroweak-weak-holonomy/)
- Source path: [`TauLib/BookIV/Electroweak/WeakHolonomy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakHolonomy.lean#L204-L208)
- Source range: L204-L208
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.T52` — Weak Gauge Group

## Immediate Comment / Docstring

```lean
/-- [IV.T52] The weak gauge group is SU(2)_L: this follows from
    (1) the crossing-point action space has dim = 3,
    (2) the holonomy is non-abelian,
    (3) only left-handed states participate.
    The subscript L denotes left-handed chirality selection. -/
```

## Source Excerpt

```lean
theorem weak_gauge_su2 :
    crossing_action.real_dim = 3 ∧
    weak_holonomy_single.non_abelian = true ∧
    su2l_identification.chirality = .Left := by
  exact ⟨rfl, rfl, rfl⟩
```
