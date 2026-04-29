---
{
  "projection_kind": "taulib_declaration",
  "title": "temporal_direction",
  "permalink": "/verify/taulib/docs/book-v-temporal-base-circle/temporal-direction/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Temporal.BaseCircle`.",
  "declaration_id": "TauLib.BookV.Temporal.BaseCircle::temporal_direction",
  "declaration_slug": "temporal-direction",
  "kind": "theorem",
  "name": "temporal_direction",
  "module_name": "TauLib.BookV.Temporal.BaseCircle",
  "module_url": "/verify/taulib/docs/book-v-temporal-base-circle/",
  "source_line_start": 188,
  "source_line_end": 191,
  "registry_ids": [
    "V.P03"
  ],
  "related_registry_items": [
    {
      "id": "V.P03",
      "title": "Arrow of Time = Orbit Direction",
      "url": "/registry/object/V.P03/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/BaseCircle.lean#L188-L191",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/BaseCircle.lean#L188-L191",
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
- Source path: [`TauLib/BookV/Temporal/BaseCircle.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/BaseCircle.lean#L188-L191)
- Source range: L188-L191
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.P03` — Arrow of Time = Orbit Direction

## Immediate Comment / Docstring

```lean
/-- [V.P03] Temporal direction: the generative direction of the α-orbit
    defines the arrow of time. Deeper refinement levels are "later."

    The alpha generator uniquely determines this direction:
    - seed = .alpha (gravity/temporal sector)
    - Profinite limit is directed (from structural arrow)
    - Direction is irreversible (from tower monotonicity) -/
```

## Source Excerpt

```lean
theorem temporal_direction :
    canonical_base_circle.seed = .alpha ∧
    canonical_base_circle.profinite.seed = .alpha := by
  exact ⟨rfl, rfl⟩
```
