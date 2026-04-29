---
{
  "projection_kind": "taulib_declaration",
  "title": "TauReal.IsCauchy_add",
  "permalink": "/verify/taulib/docs/book-i-boundary-bridge-tau-real-congruence/is-cauchy-add/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.Bridge.TauRealCongruence`.",
  "declaration_id": "TauLib.BookI.Boundary.Bridge.TauRealCongruence::TauReal.IsCauchy_add",
  "declaration_slug": "is-cauchy-add",
  "kind": "theorem",
  "name": "TauReal.IsCauchy_add",
  "module_name": "TauLib.BookI.Boundary.Bridge.TauRealCongruence",
  "module_url": "/verify/taulib/docs/book-i-boundary-bridge-tau-real-congruence/",
  "source_line_start": 150,
  "source_line_end": 180,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Bridge/TauRealCongruence.lean#L150-L180",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.Bridge.TauRealCongruence",
        "url": "/verify/taulib/docs/book-i-boundary-bridge-tau-real-congruence/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Bridge/TauRealCongruence.lean#L150-L180",
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

- Module: [TauLib.BookI.Boundary.Bridge.TauRealCongruence](/verify/taulib/docs/book-i-boundary-bridge-tau-real-congruence/)
- Source path: [`TauLib/BookI/Boundary/Bridge/TauRealCongruence.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Bridge/TauRealCongruence.lean#L150-L180)
- Source range: L150-L180
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Sum of Cauchy is Cauchy.** Triangle inequality + modulus splitting. -/
```

## Source Excerpt

```lean
theorem TauReal.IsCauchy_add (a b : TauReal)
    (ha : a.IsCauchy) (hb : b.IsCauchy) :
    (a.add b).IsCauchy := by
  obtain ⟨μa, hma⟩ := ha
  obtain ⟨μb, hmb⟩ := hb
  refine ⟨fun k => max (μa (2*k + 1)) (μb (2*k + 1)), fun k m n hm hn => ?_⟩
  have hma_m : μa (2*k + 1) ≤ m := le_of_max_le_left hm
  have hma_n : μa (2*k + 1) ≤ n := le_of_max_le_left hn
  have hmb_m : μb (2*k + 1) ≤ m := le_of_max_le_right hm
  have hmb_n : μb (2*k + 1) ≤ n := le_of_max_le_right hn
  have ha_step := hma (2*k + 1) m n hma_m hma_n
  have hb_step := hmb (2*k + 1) m n hmb_m hmb_n
  unfold TauRat.lt at ha_step hb_step ⊢
  rw [TauRat.toRat_abs, toRat_sub] at ha_step hb_step
  rw [TauRat.toRat_abs, toRat_sub]
  rw [TauRat.ofNatRecip_toRat] at ha_step hb_step ⊢
  have h_lhs_eq :
      ((a.add b).approx m).toRat - ((a.add b).approx n).toRat
        = ((a.approx m).toRat - (a.approx n).toRat) +
          ((b.approx m).toRat - (b.approx n).toRat) := by
    show ((a.approx m).add (b.approx m)).toRat -
           ((a.approx n).add (b.approx n)).toRat = _
    rw [toRat_add, toRat_add]; ring
  rw [h_lhs_eq]
  have h_tri := abs_add_le
      ((a.approx m).toRat - (a.approx n).toRat)
      ((b.approx m).toRat - (b.approx n).toRat)
  have h_split : (1 : Rat) / ((2*k + 1 : Nat) + 1) +
                 1 / ((2*k + 1 : Nat) + 1) = 1 / ((k : Rat) + 1) := by
    push_cast; field_simp; ring
  linarith
```
