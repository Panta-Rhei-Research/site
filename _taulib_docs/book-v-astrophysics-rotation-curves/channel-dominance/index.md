---
{
  "projection_kind": "taulib_declaration",
  "title": "channelDominance",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-rotation-curves/channel-dominance/",
  "summary_short": "`def` declaration in `TauLib.BookV.Astrophysics.RotationCurves`.",
  "declaration_id": "TauLib.BookV.Astrophysics.RotationCurves::channelDominance",
  "declaration_slug": "channel-dominance",
  "kind": "def",
  "name": "channelDominance",
  "module_name": "TauLib.BookV.Astrophysics.RotationCurves",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-rotation-curves/",
  "source_line_start": 953,
  "source_line_end": 955,
  "registry_ids": [
    "V.R394"
  ],
  "related_registry_items": [
    {
      "id": "V.R394",
      "title": "Channel Dominance at Galactic Scales",
      "url": "/registry/object/V.R394/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L953-L955",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Astrophysics.RotationCurves",
        "url": "/verify/taulib/docs/book-v-astrophysics-rotation-curves/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L953-L955",
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

- Module: [TauLib.BookV.Astrophysics.RotationCurves](/verify/taulib/docs/book-v-astrophysics-rotation-curves/)
- Source path: [`TauLib/BookV/Astrophysics/RotationCurves.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L953-L955)
- Source range: L953-L955
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `V.R394` — Channel Dominance at Galactic Scales

## Immediate Comment / Docstring

```lean
/-- [V.R394] Channel Dominance at Galactic Scales.

    NGC 3198 at 30 kpc: g_N ≈ 2.2×10⁻¹², a₀ ≈ 10⁻¹⁰.
    f_fiber ≈ 0.98: fiber provides 98% of total acceleration.
    Keplerian 1/√r decline is the artifact of ignoring the fiber. -/
```

## Source Excerpt

```lean
def channelDominance : String :=
  "NGC 3198 at 30 kpc: f_fiber = 0.98. " ++
  "Fiber provides 98% of g. Keplerian decline = ignoring fiber."
```
