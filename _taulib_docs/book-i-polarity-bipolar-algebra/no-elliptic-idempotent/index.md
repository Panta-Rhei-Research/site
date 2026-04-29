---
{
  "projection_kind": "taulib_declaration",
  "title": "no_elliptic_idempotent",
  "permalink": "/verify/taulib/docs/book-i-polarity-bipolar-algebra/no-elliptic-idempotent/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Polarity.BipolarAlgebra`.",
  "declaration_id": "TauLib.BookI.Polarity.BipolarAlgebra::no_elliptic_idempotent",
  "declaration_slug": "no-elliptic-idempotent",
  "kind": "theorem",
  "name": "no_elliptic_idempotent",
  "module_name": "TauLib.BookI.Polarity.BipolarAlgebra",
  "module_url": "/verify/taulib/docs/book-i-polarity-bipolar-algebra/",
  "source_line_start": 201,
  "source_line_end": 224,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/BipolarAlgebra.lean#L201-L224",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/BipolarAlgebra.lean#L201-L224",
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
- Source path: [`TauLib/BookI/Polarity/BipolarAlgebra.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/BipolarAlgebra.lean#L201-L224)
- Source range: L201-L224
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `I.T10` — Split-Complex Forced

## Immediate Comment / Docstring

```lean
/-- [I.T10] No nontrivial idempotent in the Gaussian integers:
    if (a+bi)² = (a+bi) over Z, then (a,b) = (0,0) or (a,b) = (1,0).

    Proof: From (a+bi)² = a+bi:
    - Real part: a² - b² = a
    - Imaginary part: 2ab = b
    From 2ab = b: either b = 0 or 2a = 1 (impossible in Z).
    If b = 0: a² = a, so a(a-1) = 0, hence a = 0 or a = 1. -/
```

## Source Excerpt

```lean
theorem no_elliptic_idempotent (z : GaussInt)
    (h : GaussInt.mul z z = z) :
    z = ⟨0, 0⟩ ∨ z = ⟨1, 0⟩ := by
  -- Extract component equations
  have hR : z.re * z.re - z.im * z.im = z.re := by
    have := congrArg GaussInt.re h; simp [GaussInt.mul] at this; exact this
  have hI : z.im * z.re + z.im * z.re = z.im := by
    have := congrArg GaussInt.im h; simp [GaussInt.mul] at this
    rw [Int.mul_comm z.re z.im] at this; exact this
  -- Factor IM equation: z.im * (z.re + z.re - 1) = 0
  have him_factor : z.im * (z.re + z.re - 1) = 0 := by linear_combination hI
  -- Int integral domain: z.im = 0 or z.re + z.re = 1 (impossible)
  rcases int_no_zero_div him_factor with hb | hab
  · -- z.im = 0: then z.re² = z.re
    rw [hb] at hR; simp at hR
    -- hR: z.re * z.re = z.re
    have hre_factor : z.re * (z.re - 1) = 0 := by linear_combination hR
    rcases int_no_zero_div hre_factor with ha | ha
    · left; exact GaussInt.ext ha hb
    · right
      have hre1 : z.re = 1 := by omega
      exact GaussInt.ext hre1 hb
  · -- z.re + z.re = 1: impossible in ℤ (parity)
    exfalso; omega
```
