---
{
  "projection_kind": "taulib_declaration",
  "title": "channelFraction",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-rotation-curves/channel-fraction/",
  "summary_short": "`def` declaration in `TauLib.BookV.Astrophysics.RotationCurves`.",
  "declaration_id": "TauLib.BookV.Astrophysics.RotationCurves::channelFraction",
  "declaration_slug": "channel-fraction",
  "kind": "def",
  "name": "channelFraction",
  "module_name": "TauLib.BookV.Astrophysics.RotationCurves",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-rotation-curves/",
  "source_line_start": 829,
  "source_line_end": 831,
  "registry_ids": [
    "V.D267"
  ],
  "related_registry_items": [
    {
      "id": "V.D267",
      "title": "Channel Fraction",
      "url": "/registry/object/V.D267/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L829-L831",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L829-L831",
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
- Source path: [`TauLib/BookV/Astrophysics/RotationCurves.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L829-L831)
- Source range: L829-L831
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `V.D267` — Channel Fraction

## Immediate Comment / Docstring

```lean
/-- [V.D267] Channel Fraction.

    f_fiber = g_fiber²/g² = a₀/(g_N+a₀) = 1/(1+y), y = g_N/a₀.
    NGC 3198 at 30 kpc: f_fiber ≈ 0.98 — fiber provides 98%
    of total gravitational acceleration. -/
```

## Source Excerpt

```lean
def channelFraction : String :=
  "f_fiber = a_0/(g_N+a_0) = 1/(1+y). " ++
  "NGC 3198 at 30 kpc: f_fiber = 0.98."
```
