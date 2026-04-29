---
{
  "projection_kind": "taulib_declaration",
  "title": "laplace_from_classical_cr_witness",
  "permalink": "/verify/taulib/docs/book-i-holomorphy-h6-earned-codomain-wave-cr/laplace-from-classical-cr-witness/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Holomorphy.H6EarnedCodomainWaveCR`.",
  "declaration_id": "TauLib.BookI.Holomorphy.H6EarnedCodomainWaveCR::laplace_from_classical_cr_witness",
  "declaration_slug": "laplace-from-classical-cr-witness",
  "kind": "theorem",
  "name": "laplace_from_classical_cr_witness",
  "module_name": "TauLib.BookI.Holomorphy.H6EarnedCodomainWaveCR",
  "module_url": "/verify/taulib/docs/book-i-holomorphy-h6-earned-codomain-wave-cr/",
  "source_line_start": 247,
  "source_line_end": 263,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/H6EarnedCodomainWaveCR.lean#L247-L263",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/H6EarnedCodomainWaveCR.lean#L247-L263",
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
- Source path: [`TauLib/BookI/Holomorphy/H6EarnedCodomainWaveCR.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/H6EarnedCodomainWaveCR.lean#L247-L263)
- Source range: L247-L263
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Paper §5 Remark `elliptic-contrast` witness — structural
    form**.

    The classical complex case `i² = -1` would have CR system
    `∂_t u = ∂_x v ∧ ∂_x u = -∂_t v` (with the MINUS sign).
    Same 4-step derivation produces Laplace `∂_t² u = -∂_x² u`,
    i.e.\ `∂_t² u + ∂_x² u = 0`.

    This theorem records the structural contrast: with
    `dx u = -dt v` (note the negative), the wave equation
    becomes `∂_t² u = -∂_x² u`. -/
```

## Source Excerpt

```lean
theorem laplace_from_classical_cr_witness {α : Type*}
    (dt dx : (α → Int) → (α → Int))
    (commute : ∀ f, dt (dx f) = dx (dt f))
    (neg : (α → Int) → (α → Int))
    (neg_neg : ∀ f, neg (neg f) = f)
    (neg_dx : ∀ f, dx (neg f) = neg (dx f))
    (u v : α → Int)
    (cr1 : dt u = dx v) (cr2_classical : dx u = neg (dt v)) :
    dt (dt u) = neg (dx (dx u)) := by
  -- Same proof structure but with the negative sign tracked
  rw [cr1, commute]
  -- Goal: dx (dt v) = neg (dx (dx u))
  -- From cr2_classical: dx u = neg (dt v), so dt v = neg (dx u)
  have h : dt v = neg (dx u) := by
    have := neg_neg (dt v)
    rw [← this, cr2_classical]
  rw [h, neg_dx]
```
