---
{
  "projection_kind": "taulib_declaration",
  "title": "wave_equation_from_split_cr",
  "permalink": "/verify/taulib/docs/book-i-holomorphy-h6-earned-codomain-wave-cr/wave-equation-from-split-cr/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Holomorphy.H6EarnedCodomainWaveCR`.",
  "declaration_id": "TauLib.BookI.Holomorphy.H6EarnedCodomainWaveCR::wave_equation_from_split_cr",
  "declaration_slug": "wave-equation-from-split-cr",
  "kind": "theorem",
  "name": "wave_equation_from_split_cr",
  "module_name": "TauLib.BookI.Holomorphy.H6EarnedCodomainWaveCR",
  "module_url": "/verify/taulib/docs/book-i-holomorphy-h6-earned-codomain-wave-cr/",
  "source_line_start": 214,
  "source_line_end": 221,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/H6EarnedCodomainWaveCR.lean#L214-L221",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Holomorphy.H6EarnedCodomainWaveCR",
        "url": "/verify/taulib/docs/book-i-holomorphy-h6-earned-codomain-wave-cr/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/H6EarnedCodomainWaveCR.lean#L214-L221",
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

- Module: [TauLib.BookI.Holomorphy.H6EarnedCodomainWaveCR](/verify/taulib/docs/book-i-holomorphy-h6-earned-codomain-wave-cr/)
- Source path: [`TauLib/BookI/Holomorphy/H6EarnedCodomainWaveCR.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/H6EarnedCodomainWaveCR.lean#L214-L221)
- Source range: L214-L221
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Paper §5 Theorem `wave-CR` — KEYSTONE**.

    Given commuting linear operators `dt, dx : (α → ℤ) → (α → ℤ)`
    and functions `u, v : α → ℤ` satisfying the split-complex
    Cauchy–Riemann system, the function `u` satisfies the
    **hyperbolic wave equation** `∂_t² u = ∂_x² u`.

    The 4-step derivation (see paper §5):
    ```
    ∂_t² u = ∂_t (∂_x v)    -- by CR1
           = ∂_x (∂_t v)    -- commutativity
           = ∂_x (∂_x u)    -- by CR2 reversed
           = ∂_x² u
    ```

    This IS the structural fingerprint of `j² = +1`: with
    `i² = -1` the same derivation produces Laplace's equation
    `∂_t² u + ∂_x² u = 0` (Remark `elliptic-contrast` in
    paper §5). -/
```

## Source Excerpt

```lean
theorem wave_equation_from_split_cr {α : Type*}
    (dt dx : (α → Int) → (α → Int))
    (commute : ∀ f, dt (dx f) = dx (dt f))
    (u v : α → Int)
    (cr : split_cr_system dt dx u v) :
    dt (dt u) = dx (dx u) := by
  obtain ⟨cr1, cr2⟩ := cr
  rw [cr1, commute, ← cr2]
```
