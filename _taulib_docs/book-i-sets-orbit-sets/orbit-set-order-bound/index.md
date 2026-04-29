---
{
  "projection_kind": "taulib_declaration",
  "title": "orbit_set_order_bound",
  "permalink": "/verify/taulib/docs/book-i-sets-orbit-sets/orbit-set-order-bound/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Sets.OrbitSets`.",
  "declaration_id": "TauLib.BookI.Sets.OrbitSets::orbit_set_order_bound",
  "declaration_slug": "orbit-set-order-bound",
  "kind": "theorem",
  "name": "orbit_set_order_bound",
  "module_name": "TauLib.BookI.Sets.OrbitSets",
  "module_url": "/verify/taulib/docs/book-i-sets-orbit-sets/",
  "source_line_start": 172,
  "source_line_end": 174,
  "registry_ids": [
    "I.P42"
  ],
  "related_registry_items": [
    {
      "id": "I.P42",
      "title": "Order Bound",
      "url": "/registry/object/I.P42/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/OrbitSets.lean#L172-L174",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Sets.OrbitSets",
        "url": "/verify/taulib/docs/book-i-sets-orbit-sets/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/OrbitSets.lean#L172-L174",
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

- Module: [TauLib.BookI.Sets.OrbitSets](/verify/taulib/docs/book-i-sets-orbit-sets/)
- Source path: [`TauLib/BookI/Sets/OrbitSets.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/OrbitSets.lean#L172-L174)
- Source range: L172-L174
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `I.P42` — Order Bound

## Immediate Comment / Docstring

```lean
/-- [I.P42] Order bound: if α_k ∈ Set(α_n) and n ≠ 0, then k ≤ n.
    This is tau_mem_le restated in orbit-set language. -/
```

## Source Excerpt

```lean
theorem orbit_set_order_bound (n k : TauIdx)
    (h : orbit_set_alpha n k) (hn : n ≠ 0) : k ≤ n :=
  tau_mem_le h hn
```
