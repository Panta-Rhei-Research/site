---
{
  "projection_kind": "taulib_declaration",
  "title": "physical_time_derived",
  "permalink": "/verify/taulib/docs/book-v-temporal-base-circle/physical-time-derived/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Temporal.BaseCircle`.",
  "declaration_id": "TauLib.BookV.Temporal.BaseCircle::physical_time_derived",
  "declaration_slug": "physical-time-derived",
  "kind": "theorem",
  "name": "physical_time_derived",
  "module_name": "TauLib.BookV.Temporal.BaseCircle",
  "module_url": "/verify/taulib/docs/book-v-temporal-base-circle/",
  "source_line_start": 168,
  "source_line_end": 175,
  "registry_ids": [
    "V.T08"
  ],
  "related_registry_items": [
    {
      "id": "V.T08",
      "title": "Time Derivation Theorem",
      "url": "/registry/object/V.T08/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/BaseCircle.lean#L168-L175",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/BaseCircle.lean#L168-L175",
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
- Source path: [`TauLib/BookV/Temporal/BaseCircle.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/BaseCircle.lean#L168-L175)
- Source range: L168-L175
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T08` — Time Derivation Theorem

## Immediate Comment / Docstring

```lean
/-- [V.T08] Physical time is a DERIVED quantity: it emerges from the
    refinement tower ordering and accumulated arc length, NOT from
    a postulated spacetime manifold.

    The derivation path:
    1. α-orbit generates refinement tower levels
    2. Tower levels carry structural ordering (earlier < later)
    3. Each tick contributes proper-time increment
    4. Accumulated arc length = physical time

    This theorem records that the ProtoTime ordering precedes and
    generates the proper time series. -/
```

## Source Excerpt

```lean
theorem physical_time_derived :
    -- ProtoTime exists before proper time
    (∃ t : ProtoTime, t.tick > 0) ∧
    -- NNO (natural numbers) from alpha-orbit
    (∀ n : Nat, ∃ t : ProtoTime, prototime_to_nat t = n) := by
  constructor
  · exact ⟨⟨1, by omega⟩, by decide⟩
  · exact nno_from_alpha
```
