---
{
  "projection_kind": "taulib_declaration",
  "title": "count_fixed_points",
  "permalink": "/verify/taulib/docs/book-iii-computation-e2-witness/count-fixed-points/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Computation.E2Witness`.",
  "declaration_id": "TauLib.BookIII.Computation.E2Witness::count_fixed_points",
  "declaration_slug": "count-fixed-points",
  "kind": "def",
  "name": "count_fixed_points",
  "module_name": "TauLib.BookIII.Computation.E2Witness",
  "module_url": "/verify/taulib/docs/book-iii-computation-e2-witness/",
  "source_line_start": 67,
  "source_line_end": 76,
  "registry_ids": [
    "III.D83"
  ],
  "related_registry_items": [
    {
      "id": "III.D83",
      "title": "Kleene Fixed Point",
      "url": "/registry/object/III.D83/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/E2Witness.lean#L67-L76",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Computation.E2Witness",
        "url": "/verify/taulib/docs/book-iii-computation-e2-witness/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/E2Witness.lean#L67-L76",
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

- Module: [TauLib.BookIII.Computation.E2Witness](/verify/taulib/docs/book-iii-computation-e2-witness/)
- Source path: [`TauLib/BookIII/Computation/E2Witness.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/E2Witness.lean#L67-L76)
- Source range: L67-L76
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D83` — Kleene Fixed Point

## Immediate Comment / Docstring

```lean
/-- [III.D83] Count fixed points of self-application at stage k. -/
```

## Source Excerpt

```lean
def count_fixed_points (k : Nat) : Nat :=
  let pk := primorial k
  go 0 pk 0
where
  go (c bound acc : Nat) : Nat :=
    if c >= bound then acc
    else
      let fp := if self_apply c k == c then 1 else 0
      go (c + 1) bound (acc + fp)
  termination_by bound - c
```
