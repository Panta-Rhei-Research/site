---
{
  "projection_kind": "taulib_declaration",
  "title": "tau_features",
  "permalink": "/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/tau-features/",
  "summary_short": "`def` declaration in `TauLib.BookII.Mirror.DimensionalLadder`.",
  "declaration_id": "TauLib.BookII.Mirror.DimensionalLadder::tau_features",
  "declaration_slug": "tau-features",
  "kind": "def",
  "name": "tau_features",
  "module_name": "TauLib.BookII.Mirror.DimensionalLadder",
  "module_url": "/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/",
  "source_line_start": 184,
  "source_line_end": 189,
  "registry_ids": [
    "II.T47"
  ],
  "related_registry_items": [
    {
      "id": "II.T47",
      "title": "Simultaneous Rung Theorem",
      "url": "/registry/object/II.T47/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/DimensionalLadder.lean#L184-L189",
  "formal_status": "defined",
  "declaration_role": "data/computed value",
  "formal_status_label": "data/computed value",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Mirror.DimensionalLadder",
        "url": "/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/DimensionalLadder.lean#L184-L189",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "role": "data/computed value",
      "status": "data/computed value"
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

- Module: [TauLib.BookII.Mirror.DimensionalLadder](/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/)
- Source path: [`TauLib/BookII/Mirror/DimensionalLadder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/DimensionalLadder.lean#L184-L189)
- Source range: L184-L189
- Kind: `def`
- Public role: `data/computed value`
- Formal status hint: `data/computed value`

## Registry Links

- `II.T47` — Simultaneous Rung Theorem

## Immediate Comment / Docstring

```lean
/-- [II.T47] Features present in τ³ holomorphy, drawn from multiple
    classical rungs simultaneously. -/
```

## Source Excerpt

```lean
def tau_features : List SCVFeature := [
  .CauchyIntegral,         -- from C1 (via Mutual Determination II.T27)
  .DistinguishedBoundary,  -- from C2 (lemniscate L = S¹ ∨ S¹)
  .HartogsExtension,       -- from C2 (via Global Hartogs I.T31)
  .FullHartogs             -- from C3 (via Global Hartogs I.T31)
]
```
