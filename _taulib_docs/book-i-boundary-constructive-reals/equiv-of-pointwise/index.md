---
{
  "projection_kind": "taulib_declaration",
  "title": "TauReal.equiv_of_pointwise",
  "permalink": "/verify/taulib/docs/book-i-boundary-constructive-reals/equiv-of-pointwise/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.ConstructiveReals`.",
  "declaration_id": "TauLib.BookI.Boundary.ConstructiveReals::TauReal.equiv_of_pointwise",
  "declaration_slug": "equiv-of-pointwise",
  "kind": "theorem",
  "name": "TauReal.equiv_of_pointwise",
  "module_name": "TauLib.BookI.Boundary.ConstructiveReals",
  "module_url": "/verify/taulib/docs/book-i-boundary-constructive-reals/",
  "source_line_start": 215,
  "source_line_end": 225,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/ConstructiveReals.lean#L215-L225",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/ConstructiveReals.lean#L215-L225",
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
- Source path: [`TauLib/BookI/Boundary/ConstructiveReals.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/ConstructiveReals.lean#L215-L225)
- Source range: L215-L225
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Pointwise equivalence is strictly stronger than Cauchy equivalence.

    The modulus is the constant zero — at every index the pointwise
    difference is already equiv to zero, hence strictly below any
    positive `1/(k+1)`.  This bridge wraps every existing pointwise
    witness (ring axioms, fromTauRat embedding, downstream callers)
    into a Cauchy-equiv proof. -/
```

## Source Excerpt

```lean
theorem TauReal.equiv_of_pointwise {a b : TauReal}
    (h : ∀ n, TauRat.equiv (a.approx n) (b.approx n)) :
    TauReal.equiv a b := by
  refine ⟨fun _ => 0, fun k n _ => ?_⟩
  unfold TauRat.lt
  rw [TauRat.toRat_abs, toRat_sub]
  have h_eq : (a.approx n).toRat = (b.approx n).toRat :=
    (equiv_iff_toRat_eq _ _).mp (h n)
  rw [h_eq]
  simp
  exact TauRat.ofNatRecip_pos k
```
