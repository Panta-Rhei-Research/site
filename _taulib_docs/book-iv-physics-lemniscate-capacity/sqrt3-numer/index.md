---
{
  "projection_kind": "taulib_declaration",
  "title": "sqrt3_numer",
  "permalink": "/verify/taulib/docs/book-iv-physics-lemniscate-capacity/sqrt3-numer/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Physics.LemniscateCapacity`.",
  "declaration_id": "TauLib.BookIV.Physics.LemniscateCapacity::sqrt3_numer",
  "declaration_slug": "sqrt3-numer",
  "kind": "def",
  "name": "sqrt3_numer",
  "module_name": "TauLib.BookIV.Physics.LemniscateCapacity",
  "module_url": "/verify/taulib/docs/book-iv-physics-lemniscate-capacity/",
  "source_line_start": 150,
  "source_line_end": 150,
  "registry_ids": [
    "IV.D43"
  ],
  "related_registry_items": [
    {
      "id": "IV.D43",
      "title": "Spectral Distance √3",
      "url": "/registry/object/IV.D43/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/LemniscateCapacity.lean#L150-L150",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/LemniscateCapacity.lean#L150-L150",
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

- Module: [TauLib.BookIV.Physics.LemniscateCapacity](/verify/taulib/docs/book-iv-physics-lemniscate-capacity/)
- Source path: [`TauLib/BookIV/Physics/LemniscateCapacity.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/LemniscateCapacity.lean#L150-L150)
- Source range: L150-L150
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `IV.D43` — Spectral Distance √3

## Immediate Comment / Docstring

```lean
/-- [IV.D43] √3 rational approximation (7 significant digits).
    √3 = 1.7320508... ≈ 17320508/10000000

    Quality: (17320508)² = 299,999,982,338,064
             3 × (10000000)² = 300,000,000,000,000
             Relative error: ~5.9 × 10⁻⁸ -/
```

## Source Excerpt

```lean
def sqrt3_numer : Nat := 17320508
```
