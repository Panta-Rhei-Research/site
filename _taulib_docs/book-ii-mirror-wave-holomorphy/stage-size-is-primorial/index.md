---
{
  "projection_kind": "taulib_declaration",
  "title": "stage_size_is_primorial",
  "permalink": "/verify/taulib/docs/book-ii-mirror-wave-holomorphy/stage-size-is-primorial/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Mirror.WaveHolomorphy`.",
  "declaration_id": "TauLib.BookII.Mirror.WaveHolomorphy::stage_size_is_primorial",
  "declaration_slug": "stage-size-is-primorial",
  "kind": "theorem",
  "name": "stage_size_is_primorial",
  "module_name": "TauLib.BookII.Mirror.WaveHolomorphy",
  "module_url": "/verify/taulib/docs/book-ii-mirror-wave-holomorphy/",
  "source_line_start": 185,
  "source_line_end": 186,
  "registry_ids": [
    "II.T45"
  ],
  "related_registry_items": [
    {
      "id": "II.T45",
      "title": "Parallel Preservation",
      "url": "/registry/object/II.T45/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/WaveHolomorphy.lean#L185-L186",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/WaveHolomorphy.lean#L185-L186",
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

- Module: [TauLib.BookII.Mirror.WaveHolomorphy](/verify/taulib/docs/book-ii-mirror-wave-holomorphy/)
- Source path: [`TauLib/BookII/Mirror/WaveHolomorphy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/WaveHolomorphy.lean#L185-L186)
- Source range: L185-L186
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `II.T45` — Parallel Preservation

## Immediate Comment / Docstring

```lean
/-- [II.T45] The stage size at k is the k-th primorial. -/
```

## Source Excerpt

```lean
theorem stage_size_is_primorial (k : Nat) :
    (default_stage_geometry k).stage_size = primorial k := rfl
```
