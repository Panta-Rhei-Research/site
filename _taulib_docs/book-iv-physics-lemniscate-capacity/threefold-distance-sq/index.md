---
{
  "projection_kind": "taulib_declaration",
  "title": "threefold_distance_sq",
  "permalink": "/verify/taulib/docs/book-iv-physics-lemniscate-capacity/threefold-distance-sq/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Physics.LemniscateCapacity`.",
  "declaration_id": "TauLib.BookIV.Physics.LemniscateCapacity::threefold_distance_sq",
  "declaration_slug": "threefold-distance-sq",
  "kind": "theorem",
  "name": "threefold_distance_sq",
  "module_name": "TauLib.BookIV.Physics.LemniscateCapacity",
  "module_url": "/verify/taulib/docs/book-iv-physics-lemniscate-capacity/",
  "source_line_start": 127,
  "source_line_end": 129,
  "registry_ids": [
    "IV.T11"
  ],
  "related_registry_items": [
    {
      "id": "IV.T11",
      "title": "Three-Fold Distance Squared",
      "url": "/registry/object/IV.T11/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/LemniscateCapacity.lean#L127-L129",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Physics.LemniscateCapacity",
        "url": "/verify/taulib/docs/book-iv-physics-lemniscate-capacity/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/LemniscateCapacity.lean#L127-L129",
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

- Module: [TauLib.BookIV.Physics.LemniscateCapacity](/verify/taulib/docs/book-iv-physics-lemniscate-capacity/)
- Source path: [`TauLib/BookIV/Physics/LemniscateCapacity.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/LemniscateCapacity.lean#L127-L129)
- Source range: L127-L129
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.T11` — Three-Fold Distance Squared

## Immediate Comment / Docstring

```lean
/-- [IV.T11] |1 - ω|² = 3.

    Proof: |1 - ω|² = (3/2)² + (√3/2)² = 9/4 + 3/4 = 12/4 = 3.

    In integer arithmetic:
    - Numerator sum: 9 + 3 = 12
    - Denominator: 4
    - Quotient: 12 / 4 = 3

    This is the origin of √3 in the mass ratio formula. -/
```

## Source Excerpt

```lean
theorem threefold_distance_sq :
    omega_real_sq + omega_imag_sq = 3 * omega_denom := by
  simp [omega_real_sq, omega_imag_sq, omega_denom]
```
