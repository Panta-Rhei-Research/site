---
{
  "projection_kind": "taulib_declaration",
  "title": "count_e3_fixed_points",
  "permalink": "/verify/taulib/docs/book-iii-mirror-e3-witness/count-e3-fixed-points/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Mirror.E3Witness`.",
  "declaration_id": "TauLib.BookIII.Mirror.E3Witness::count_e3_fixed_points",
  "declaration_slug": "count-e3-fixed-points",
  "kind": "def",
  "name": "count_e3_fixed_points",
  "module_name": "TauLib.BookIII.Mirror.E3Witness",
  "module_url": "/verify/taulib/docs/book-iii-mirror-e3-witness/",
  "source_line_start": 71,
  "source_line_end": 80,
  "registry_ids": [
    "III.D85"
  ],
  "related_registry_items": [
    {
      "id": "III.D85",
      "title": "Self-Referential Fixed Point",
      "url": "/registry/object/III.D85/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Mirror/E3Witness.lean#L71-L80",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Mirror.E3Witness",
        "url": "/verify/taulib/docs/book-iii-mirror-e3-witness/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Mirror/E3Witness.lean#L71-L80",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
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

- Module: [TauLib.BookIII.Mirror.E3Witness](/verify/taulib/docs/book-iii-mirror-e3-witness/)
- Source path: [`TauLib/BookIII/Mirror/E3Witness.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Mirror/E3Witness.lean#L71-L80)
- Source range: L71-L80
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D85` — Self-Referential Fixed Point

## Immediate Comment / Docstring

```lean
/-- [III.D85] Count self-referential fixed points at stage k. -/
```

## Source Excerpt

```lean
def count_e3_fixed_points (k : Nat) : Nat :=
  let pk := primorial k
  go 0 pk 0 k
where
  go (x bound acc k : Nat) : Nat :=
    if x >= bound then acc
    else
      let fp := if e3_predicate x k then 1 else 0
      go (x + 1) bound (acc + fp) k
  termination_by bound - x
```
