---
{
  "projection_kind": "taulib_declaration",
  "title": "supports_distinct",
  "permalink": "/verify/taulib/docs/book-iv-physics-lemniscate-capacity/supports-distinct/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Physics.LemniscateCapacity`.",
  "declaration_id": "TauLib.BookIV.Physics.LemniscateCapacity::supports_distinct",
  "declaration_slug": "supports-distinct",
  "kind": "theorem",
  "name": "supports_distinct",
  "module_name": "TauLib.BookIV.Physics.LemniscateCapacity",
  "module_url": "/verify/taulib/docs/book-iv-physics-lemniscate-capacity/",
  "source_line_start": 91,
  "source_line_end": 106,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/LemniscateCapacity.lean#L91-L106",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/LemniscateCapacity.lean#L91-L106",
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
- Source path: [`TauLib/BookIV/Physics/LemniscateCapacity.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/LemniscateCapacity.lean#L91-L106)
- Source range: L91-L106
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.T11` — Three-Fold Distance Squared

## Immediate Comment / Docstring

```lean
/-- All three support types are distinct. -/
```

## Source Excerpt

```lean
theorem supports_distinct :
    LemniscateSupport.Lobe1 ≠ LemniscateSupport.Lobe2 ∧
    LemniscateSupport.Lobe2 ≠ LemniscateSupport.Crossing ∧
    LemniscateSupport.Lobe1 ≠ LemniscateSupport.Crossing := by
  exact ⟨by decide, by decide, by decide⟩

-- ============================================================
-- CUBE ROOT DISTANCE [IV.T11]
-- ============================================================

/-! |1 - ω|² components for the cube root of unity ω = e^{2πi/3}.

    ω = -1/2 + i(√3/2), so:
    - (1 - ω_re)² = (1 - (-1/2))² = (3/2)² = 9/4
    - (ω_im)² = (√3/2)² = 3/4
    - |1 - ω|² = 9/4 + 3/4 = 12/4 = 3 -/
```
