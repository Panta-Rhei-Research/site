---
{
  "projection_kind": "taulib_declaration",
  "title": "PeriodLengthSequence",
  "permalink": "/verify/taulib/docs/book-iv-particles-periodic-table/period-length-sequence/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.PeriodicTable`.",
  "declaration_id": "TauLib.BookIV.Particles.PeriodicTable::PeriodLengthSequence",
  "declaration_slug": "period-length-sequence",
  "kind": "structure",
  "name": "PeriodLengthSequence",
  "module_name": "TauLib.BookIV.Particles.PeriodicTable",
  "module_url": "/verify/taulib/docs/book-iv-particles-periodic-table/",
  "source_line_start": 164,
  "source_line_end": 173,
  "registry_ids": [
    "IV.T88"
  ],
  "related_registry_items": [
    {
      "id": "IV.T88",
      "title": "Period length sequence",
      "url": "/registry/object/IV.T88/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/PeriodicTable.lean#L164-L173",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Particles.PeriodicTable",
        "url": "/verify/taulib/docs/book-iv-particles-periodic-table/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/PeriodicTable.lean#L164-L173",
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

- Module: [TauLib.BookIV.Particles.PeriodicTable](/verify/taulib/docs/book-iv-particles-periodic-table/)
- Source path: [`TauLib/BookIV/Particles/PeriodicTable.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/PeriodicTable.lean#L164-L173)
- Source range: L164-L173
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.T88` — Period length sequence

## Immediate Comment / Docstring

```lean
/-- [IV.T88] The periodic table period lengths follow:
    2, 8, 8, 18, 18, 32, 32,...

    Each length = 2n² (twice a perfect square).
    Each value (except 2) appears twice.

    This is a topological consequence of T² fiber geometry:
    shell capacity 2n² combined with Aufbau filling order
    determines noble gas closures. -/
```

## Source Excerpt

```lean
structure PeriodLengthSequence where
  /-- First 7 period lengths. -/
  lengths : List Nat := [2, 8, 8, 18, 18, 32, 32]
  /-- Each is twice a perfect square. -/
  twice_perfect_square : Bool := true
  /-- Each (except 2) appears twice. -/
  doubled : Bool := true
  /-- Topological origin. -/
  topological : Bool := true
  deriving Repr
```
