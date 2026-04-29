---
{
  "projection_kind": "taulib_declaration",
  "title": "all_stages_euclidean",
  "permalink": "/verify/taulib/docs/book-ii-mirror-wave-holomorphy/all-stages-euclidean/",
  "summary_short": "`def` declaration in `TauLib.BookII.Mirror.WaveHolomorphy`.",
  "declaration_id": "TauLib.BookII.Mirror.WaveHolomorphy::all_stages_euclidean",
  "declaration_slug": "all-stages-euclidean",
  "kind": "def",
  "name": "all_stages_euclidean",
  "module_name": "TauLib.BookII.Mirror.WaveHolomorphy",
  "module_url": "/verify/taulib/docs/book-ii-mirror-wave-holomorphy/",
  "source_line_start": 154,
  "source_line_end": 161,
  "registry_ids": [
    "II.D71"
  ],
  "related_registry_items": [
    {
      "id": "II.D71",
      "title": "Stage-Finite Euclidean Geometry",
      "url": "/registry/object/II.D71/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/WaveHolomorphy.lean#L154-L161",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Mirror.WaveHolomorphy",
        "url": "/verify/taulib/docs/book-ii-mirror-wave-holomorphy/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/WaveHolomorphy.lean#L154-L161",
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

- Module: [TauLib.BookII.Mirror.WaveHolomorphy](/verify/taulib/docs/book-ii-mirror-wave-holomorphy/)
- Source path: [`TauLib/BookII/Mirror/WaveHolomorphy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/WaveHolomorphy.lean#L154-L161)
- Source range: L154-L161
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D71` — Stage-Finite Euclidean Geometry

## Immediate Comment / Docstring

```lean
/-- [II.D71] Check all stages up to depth db. -/
```

## Source Excerpt

```lean
def all_stages_euclidean (db : Nat) : Bool :=
  go 0 (db + 1)
where
  go (k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k > db then true
    else stage_euclidean_check k && go (k + 1) (fuel - 1)
  termination_by fuel
```
