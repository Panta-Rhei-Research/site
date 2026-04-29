---
{
  "projection_kind": "taulib_declaration",
  "title": "causal_ordering_enforced",
  "permalink": "/verify/taulib/docs/book-v-temporal-base-circle/causal-ordering-enforced/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Temporal.BaseCircle`.",
  "declaration_id": "TauLib.BookV.Temporal.BaseCircle::causal_ordering_enforced",
  "declaration_slug": "causal-ordering-enforced",
  "kind": "theorem",
  "name": "causal_ordering_enforced",
  "module_name": "TauLib.BookV.Temporal.BaseCircle",
  "module_url": "/verify/taulib/docs/book-v-temporal-base-circle/",
  "source_line_start": 209,
  "source_line_end": 211,
  "registry_ids": [
    "V.T09"
  ],
  "related_registry_items": [
    {
      "id": "V.T09",
      "title": "Causal Ordering Theorem",
      "url": "/registry/object/V.T09/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/BaseCircle.lean#L209-L211",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Temporal.BaseCircle",
        "url": "/verify/taulib/docs/book-v-temporal-base-circle/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/BaseCircle.lean#L209-L211",
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

- Module: [TauLib.BookV.Temporal.BaseCircle](/verify/taulib/docs/book-v-temporal-base-circle/)
- Source path: [`TauLib/BookV/Temporal/BaseCircle.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/BaseCircle.lean#L209-L211)
- Source range: L209-L211
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T09` — Causal Ordering Theorem

## Immediate Comment / Docstring

```lean
/-- [V.T09] Causal ordering is structurally enforced: no axiom needed.
    Wraps structural_arrow from RefinementTower with Book V interpretation.

    The structural arrow of time is built into the refinement tower —
    it is not an additional postulate but a consequence of tower directedness. -/
```

## Source Excerpt

```lean
theorem causal_ordering_enforced (t1 t2 : ProtoTime) (h : t1 < t2) :
    t2.tick > t1.tick :=
  structural_arrow t1 t2 h
```
