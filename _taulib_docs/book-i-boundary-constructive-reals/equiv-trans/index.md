---
{
  "projection_kind": "taulib_declaration",
  "title": "TauReal.equiv_trans",
  "permalink": "/verify/taulib/docs/book-i-boundary-constructive-reals/equiv-trans/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.ConstructiveReals`.",
  "declaration_id": "TauLib.BookI.Boundary.ConstructiveReals::TauReal.equiv_trans",
  "declaration_slug": "equiv-trans",
  "kind": "theorem",
  "name": "TauReal.equiv_trans",
  "module_name": "TauLib.BookI.Boundary.ConstructiveReals",
  "module_url": "/verify/taulib/docs/book-i-boundary-constructive-reals/",
  "source_line_start": 249,
  "source_line_end": 275,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/ConstructiveReals.lean#L249-L275",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.ConstructiveReals",
        "url": "/verify/taulib/docs/book-i-boundary-constructive-reals/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/ConstructiveReals.lean#L249-L275",
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

- Module: [TauLib.BookI.Boundary.ConstructiveReals](/verify/taulib/docs/book-i-boundary-constructive-reals/)
- Source path: [`TauLib/BookI/Boundary/ConstructiveReals.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/ConstructiveReals.lean#L249-L275)
- Source range: L249-L275
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- TauReal equivalence is transitive (triangle inequality on the modulus). -/
```

## Source Excerpt

```lean
theorem TauReal.equiv_trans {a b c : TauReal}
    (hab : TauReal.equiv a b) (hbc : TauReal.equiv b c) :
    TauReal.equiv a c := by
  obtain ⟨μ₁, h₁⟩ := hab
  obtain ⟨μ₂, h₂⟩ := hbc
  -- Target tolerance `1/(k+1)` via halved tolerance at level `2k+1`.
  refine ⟨fun k => max (μ₁ (2 * k + 1)) (μ₂ (2 * k + 1)), fun k n hn => ?_⟩
  have hn₁ : μ₁ (2 * k + 1) ≤ n := le_of_max_le_left hn
  have hn₂ : μ₂ (2 * k + 1) ≤ n := le_of_max_le_right hn
  have h_ab := h₁ (2 * k + 1) n hn₁
  have h_bc := h₂ (2 * k + 1) n hn₂
  unfold TauRat.lt at h_ab h_bc ⊢
  rw [TauRat.toRat_abs, toRat_sub] at h_ab h_bc
  rw [TauRat.toRat_abs, toRat_sub]
  rw [TauRat.ofNatRecip_toRat] at h_ab h_bc ⊢
  have h_triangle :
      |(a.approx n).toRat - (c.approx n).toRat|
        ≤ |(a.approx n).toRat - (b.approx n).toRat|
        + |(b.approx n).toRat - (c.approx n).toRat| := by
    rw [show (a.approx n).toRat - (c.approx n).toRat =
           ((a.approx n).toRat - (b.approx n).toRat)
           + ((b.approx n).toRat - (c.approx n).toRat) from by ring]
    exact abs_add_le _ _
  have h_eq : (1 : Rat) / ((2 * k + 1 : Nat) + 1) + 1 / ((2 * k + 1 : Nat) + 1)
              = 1 / ((k : Rat) + 1) := by
    push_cast; field_simp; ring
  linarith [h_triangle, h_ab, h_bc, h_eq]
```
