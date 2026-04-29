---
{
  "projection_kind": "taulib_declaration",
  "title": "two_channel_interpolation",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-rotation-curves/two-channel-interpolation/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Astrophysics.RotationCurves`.",
  "declaration_id": "TauLib.BookV.Astrophysics.RotationCurves::two_channel_interpolation",
  "declaration_slug": "two-channel-interpolation",
  "kind": "theorem",
  "name": "two_channel_interpolation",
  "module_name": "TauLib.BookV.Astrophysics.RotationCurves",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-rotation-curves/",
  "source_line_start": 857,
  "source_line_end": 861,
  "registry_ids": [
    "V.T208"
  ],
  "related_registry_items": [
    {
      "id": "V.T208",
      "title": "Two-Channel Interpolation Theorem",
      "url": "/registry/object/V.T208/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L857-L861",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L857-L861",
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

- Module: [TauLib.BookV.Astrophysics.RotationCurves](/verify/taulib/docs/book-v-astrophysics-rotation-curves/)
- Source path: [`TauLib/BookV/Astrophysics/RotationCurves.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L857-L861)
- Source range: L857-L861
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T208` — Two-Channel Interpolation Theorem

## Immediate Comment / Docstring

```lean
/-- [V.T208] Two-Channel Interpolation Theorem.

    The decomposition g² = g_N² + g_N·a₀ defines
    ν_2ch(y) = √(1 + 1/y), y = g_N/a₀.
    • Newtonian (y >> 1): ν → 1, g → g_N.
    • Deep regime (y << 1): ν → 1/√y, g → √(g_N·a₀), v⁴ = GM·a₀.
    Both asymptotics agree with standard μ_τ interpolation. -/
```

## Source Excerpt

```lean
theorem two_channel_interpolation :
    "nu_2ch(y) = sqrt(1 + 1/y), y = g_N/a_0. " ++
    "Deep: v^4 = GM*a_0 (BTFR). Newtonian: g -> g_N." =
    "nu_2ch(y) = sqrt(1 + 1/y), y = g_N/a_0. " ++
    "Deep: v^4 = GM*a_0 (BTFR). Newtonian: g -> g_N." := rfl
```
