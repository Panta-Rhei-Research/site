---
{
  "projection_kind": "taulib_declaration",
  "title": "wave_char_roots",
  "permalink": "/verify/taulib/docs/book-ii-geometry-causal-structure/wave-char-roots/",
  "summary_short": "`def` declaration in `TauLib.BookII.Geometry.CausalStructure`.",
  "declaration_id": "TauLib.BookII.Geometry.CausalStructure::wave_char_roots",
  "declaration_slug": "wave-char-roots",
  "kind": "def",
  "name": "wave_char_roots",
  "module_name": "TauLib.BookII.Geometry.CausalStructure",
  "module_url": "/verify/taulib/docs/book-ii-geometry-causal-structure/",
  "source_line_start": 47,
  "source_line_end": 48,
  "registry_ids": [
    "II.D21"
  ],
  "related_registry_items": [
    {
      "id": "II.D21",
      "title": "Wave-Type PDE",
      "url": "/registry/object/II.D21/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Geometry/CausalStructure.lean#L47-L48",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Geometry.CausalStructure",
        "url": "/verify/taulib/docs/book-ii-geometry-causal-structure/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Geometry/CausalStructure.lean#L47-L48",
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

- Module: [TauLib.BookII.Geometry.CausalStructure](/verify/taulib/docs/book-ii-geometry-causal-structure/)
- Source path: [`TauLib/BookII/Geometry/CausalStructure.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Geometry/CausalStructure.lean#L47-L48)
- Source range: L47-L48
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D21` — Wave-Type PDE

## Immediate Comment / Docstring

```lean
/-- [II.D21] Wave equation signature from j² = +1.
    The split-complex CR equations yield a HYPERBOLIC equation.
    Verification: j² = +1 forces the wave equation signature (−)
    instead of the Laplace signature (+).

    Classical (i² = -1): characteristic polynomial ξ² + η² = 0 → NO real roots
    Split (j² = +1):   characteristic polynomial ξ² - η² = 0 → TWO real roots -/
```

## Source Excerpt

```lean
def wave_char_roots : List (Int × Int) :=
  [(1, 1), (1, -1)]  -- ξ = η and ξ = -η
```
