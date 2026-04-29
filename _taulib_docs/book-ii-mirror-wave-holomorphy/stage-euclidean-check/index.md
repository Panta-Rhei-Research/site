---
{
  "projection_kind": "taulib_declaration",
  "title": "stage_euclidean_check",
  "permalink": "/verify/taulib/docs/book-ii-mirror-wave-holomorphy/stage-euclidean-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Mirror.WaveHolomorphy`.",
  "declaration_id": "TauLib.BookII.Mirror.WaveHolomorphy::stage_euclidean_check",
  "declaration_slug": "stage-euclidean-check",
  "kind": "def",
  "name": "stage_euclidean_check",
  "module_name": "TauLib.BookII.Mirror.WaveHolomorphy",
  "module_url": "/verify/taulib/docs/book-ii-mirror-wave-holomorphy/",
  "source_line_start": 149,
  "source_line_end": 151,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/WaveHolomorphy.lean#L149-L151",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/WaveHolomorphy.lean#L149-L151",
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
- Source path: [`TauLib/BookII/Mirror/WaveHolomorphy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/WaveHolomorphy.lean#L149-L151)
- Source range: L149-L151
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D71` — Stage-Finite Euclidean Geometry

## Immediate Comment / Docstring

```lean
/-- [II.D71] Stage-Euclidean check: verify the geometry at stage k
    is Euclidean with no light cones. -/
```

## Source Excerpt

```lean
def stage_euclidean_check (k : Nat) : Bool :=
  let sg := default_stage_geometry k
  sg.is_euclidean && !sg.has_light_cones
```
