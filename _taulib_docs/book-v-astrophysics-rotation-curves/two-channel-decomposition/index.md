---
{
  "projection_kind": "taulib_declaration",
  "title": "twoChannelDecomposition",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-rotation-curves/two-channel-decomposition/",
  "summary_short": "`def` declaration in `TauLib.BookV.Astrophysics.RotationCurves`.",
  "declaration_id": "TauLib.BookV.Astrophysics.RotationCurves::twoChannelDecomposition",
  "declaration_slug": "two-channel-decomposition",
  "kind": "def",
  "name": "twoChannelDecomposition",
  "module_name": "TauLib.BookV.Astrophysics.RotationCurves",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-rotation-curves/",
  "source_line_start": 816,
  "source_line_end": 818,
  "registry_ids": [
    "V.D266"
  ],
  "related_registry_items": [
    {
      "id": "V.D266",
      "title": "Two-Channel Acceleration Decomposition",
      "url": "/registry/object/V.D266/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L816-L818",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L816-L818",
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
- Source path: [`TauLib/BookV/Astrophysics/RotationCurves.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L816-L818)
- Source range: L816-L818
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `V.D266` — Two-Channel Acceleration Decomposition

## Immediate Comment / Docstring

```lean
/-- [V.D266] Two-Channel Acceleration Decomposition.

    On τ³ = τ¹ ×_f T², the total gravitational acceleration
    decomposes as a Pythagorean sum of two channels:
    • Base channel (τ¹, gravitoelectric): g_base = g_N = GM/r²
    • Fiber channel (T², rotational): g_fiber = √(g_N·a₀)

    Total: g² = g_N² + g_N·a₀, equivalently g = g_N·√(1 + a₀/g_N). -/
```

## Source Excerpt

```lean
def twoChannelDecomposition : String :=
  "g^2 = g_N^2 + g_N*a_0. Base channel: g_N = GM/r^2. " ++
  "Fiber channel: sqrt(g_N*a_0). Pythagorean sum on tau^3."
```
