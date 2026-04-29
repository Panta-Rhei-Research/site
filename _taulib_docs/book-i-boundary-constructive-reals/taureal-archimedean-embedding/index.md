---
{
  "projection_kind": "taulib_declaration",
  "title": "taureal_archimedean_embedding",
  "permalink": "/verify/taulib/docs/book-i-boundary-constructive-reals/taureal-archimedean-embedding/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.ConstructiveReals`.",
  "declaration_id": "TauLib.BookI.Boundary.ConstructiveReals::taureal_archimedean_embedding",
  "declaration_slug": "taureal-archimedean-embedding",
  "kind": "theorem",
  "name": "taureal_archimedean_embedding",
  "module_name": "TauLib.BookI.Boundary.ConstructiveReals",
  "module_url": "/verify/taulib/docs/book-i-boundary-constructive-reals/",
  "source_line_start": 387,
  "source_line_end": 411,
  "registry_ids": [
    "I.T42"
  ],
  "related_registry_items": [
    {
      "id": "I.T42",
      "title": "Archimedean Property",
      "url": "/registry/object/I.T42/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/ConstructiveReals.lean#L387-L411",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/ConstructiveReals.lean#L387-L411",
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
- Source path: [`TauLib/BookI/Boundary/ConstructiveReals.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/ConstructiveReals.lean#L387-L411)
- Source range: L387-L411
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `I.T42` — Archimedean Property

## Immediate Comment / Docstring

```lean
/-- [I.T42] The Archimedean property: the natural number embedding
    into TauReal is unbounded.  The sequence `fromNat n` is strictly
    increasing (distinct naturals give non-equivalent TauReals).

    Under the Cauchy `equiv`, distinctness means the difference
    sequence does NOT converge to zero.  Since `fromNat n` is constant
    at `n`, the difference `|m - n|` is a fixed nonzero constant, and
    any small enough `1/(k+1)` tolerance witnesses non-convergence. -/
```

## Source Excerpt

```lean
theorem taureal_archimedean_embedding :
    ∀ n m : TauIdx, n < m →
    ¬ TauReal.equiv (TauReal.fromNat m) (TauReal.fromNat n) := by
  intro n m hnm h_eq
  obtain ⟨μ, h⟩ := h_eq
  -- Pick tolerance level `k = 1` (tolerance `1/2`).  The difference
  -- `|m - n|` is a constant integer ≥ 1, so it never dips below `1/2`.
  have h1 := h 1 (μ 1) (_root_.le_refl _)
  have h_toRat_nat : ∀ k : TauIdx, (nat_to_taurat k).toRat = (k : Rat) := by
    intro k
    simp only [nat_to_taurat, int_to_taurat, nat_to_tauint, TauRat.toRat,
               TauInt.toInt, TauInt.fromNat]
    push_cast; ring
  unfold TauRat.lt at h1
  rw [TauRat.toRat_abs, toRat_sub, TauRat.ofNatRecip_toRat] at h1
  -- Constant-sequence `.approx (μ 1)` reduces definitionally to `nat_to_taurat _`.
  have h_approx_m : (TauReal.fromNat m).approx (μ 1) = nat_to_taurat m := rfl
  have h_approx_n : (TauReal.fromNat n).approx (μ 1) = nat_to_taurat n := rfl
  rw [h_approx_m, h_approx_n, h_toRat_nat, h_toRat_nat] at h1
  have hmn_rat : ((m : Rat) - n) ≥ 1 := by
    have : (n : Rat) + 1 ≤ m := by exact_mod_cast hnm
    linarith
  rw [abs_of_nonneg (by linarith : (0 : Rat) ≤ (m : Rat) - n)] at h1
  push_cast at h1
  linarith
```
