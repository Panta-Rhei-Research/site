---
{
  "projection_kind": "taulib_declaration",
  "title": "split_complex_forced",
  "permalink": "/verify/taulib/docs/book-i-polarity-bipolar-algebra/split-complex-forced/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Polarity.BipolarAlgebra`.",
  "declaration_id": "TauLib.BookI.Polarity.BipolarAlgebra::split_complex_forced",
  "declaration_slug": "split-complex-forced",
  "kind": "theorem",
  "name": "split_complex_forced",
  "module_name": "TauLib.BookI.Polarity.BipolarAlgebra",
  "module_url": "/verify/taulib/docs/book-i-polarity-bipolar-algebra/",
  "source_line_start": 229,
  "source_line_end": 237,
  "registry_ids": [
    "I.T10"
  ],
  "related_registry_items": [
    {
      "id": "I.T10",
      "title": "Split-Complex Forced",
      "url": "/registry/object/I.T10/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/BipolarAlgebra.lean#L229-L237",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Polarity.BipolarAlgebra",
        "url": "/verify/taulib/docs/book-i-polarity-bipolar-algebra/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/BipolarAlgebra.lean#L229-L237",
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

- Module: [TauLib.BookI.Polarity.BipolarAlgebra](/verify/taulib/docs/book-i-polarity-bipolar-algebra/)
- Source path: [`TauLib/BookI/Polarity/BipolarAlgebra.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/BipolarAlgebra.lean#L229-L237)
- Source range: L229-L237
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `I.T10` — Split-Complex Forced

## Immediate Comment / Docstring

```lean
/-- [I.T10] Split-complex forced: the split-complex algebra (j² = +1) admits
    nontrivial idempotents (e+, e-), while the elliptic algebra (i² = -1) does not.
    Therefore, encoding a bipolar partition requires j² = +1. -/
```

## Source Excerpt

```lean
theorem split_complex_forced :
    -- Split-complex has nontrivial idempotent
    (∃ e : SectorPair, SectorPair.mul e e = e ∧ e ≠ ⟨0, 0⟩ ∧ e ≠ ⟨1, 1⟩) ∧
    -- Elliptic has NO nontrivial idempotent
    (∀ z : GaussInt, GaussInt.mul z z = z → z = ⟨0, 0⟩ ∨ z = ⟨1, 0⟩) := by
  constructor
  · -- Witness: e_plus_sector = (1, 0)
    exact ⟨e_plus_sector, e_plus_idem, by simp [e_plus_sector], by simp [e_plus_sector]⟩
  · exact no_elliptic_idempotent
```
