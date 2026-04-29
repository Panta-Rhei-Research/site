---
{
  "projection_kind": "taulib_declaration",
  "title": "eval at L250",
  "permalink": "/verify/taulib/docs/tour-central-theorem/eval-l250/",
  "summary_short": "`eval` declaration in `TauLib.Tour.CentralTheorem`.",
  "declaration_id": "TauLib.Tour.CentralTheorem::#eval:250",
  "declaration_slug": "eval-l250",
  "kind": "eval",
  "name": null,
  "module_name": "TauLib.Tour.CentralTheorem",
  "module_url": "/verify/taulib/docs/tour-central-theorem/",
  "source_line_start": 250,
  "source_line_end": 254,
  "registry_ids": [
    "II.C01"
  ],
  "related_registry_items": [
    {
      "id": "II.C01",
      "title": "Holographic Principle",
      "url": "/registry/object/II.C01/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/Tour/CentralTheorem.lean#L250-L254",
  "formal_status": "computed",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.Tour.CentralTheorem",
        "url": "/verify/taulib/docs/tour-central-theorem/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/Tour/CentralTheorem.lean#L250-L254",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "eval",
      "status": "computed"
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

- Module: [TauLib.Tour.CentralTheorem](/verify/taulib/docs/tour-central-theorem/)
- Source path: [`TauLib/Tour/CentralTheorem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/Tour/CentralTheorem.lean#L250-L254)
- Source range: L250-L254
- Kind: `eval`
- Formal status hint: `computed`

## Registry Links

- `II.C01` — Holographic Principle

## Immediate Comment / Docstring

```lean
-- ================================================================
-- PART 7: THE HOLOGRAPHIC PRINCIPLE
-- ================================================================

-- The Central Theorem implies the Holographic Principle [II.C01]:
-- The 1-dimensional boundary (lemniscate data) completely encodes
-- the 3-dimensional interior (tau^3 data).
-- Nothing is lost. Nothing is added.

-- bndlift reconstructs interior from boundary:
```

## Source Excerpt

```lean
#eval holographic_check 3 15                  -- true
#check holographic_3_15    -- holographic_check 3 15 = true (formally proved)

-- Structural: reduce(bndlift(x, k), k) = reduce(x, k)
#check holographic_roundtrip
```
