---
{
  "projection_kind": "taulib_declaration",
  "title": "TauReal.mul_respects_equiv_under_cauchy",
  "permalink": "/verify/taulib/docs/book-i-boundary-bridge-tau-real-congruence/mul-respects-equiv-under-cauchy/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.Bridge.TauRealCongruence`.",
  "declaration_id": "TauLib.BookI.Boundary.Bridge.TauRealCongruence::TauReal.mul_respects_equiv_under_cauchy",
  "declaration_slug": "mul-respects-equiv-under-cauchy",
  "kind": "theorem",
  "name": "TauReal.mul_respects_equiv_under_cauchy",
  "module_name": "TauLib.BookI.Boundary.Bridge.TauRealCongruence",
  "module_url": "/verify/taulib/docs/book-i-boundary-bridge-tau-real-congruence/",
  "source_line_start": 272,
  "source_line_end": 293,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Bridge/TauRealCongruence.lean#L272-L293",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Bridge/TauRealCongruence.lean#L272-L293",
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
- Source path: [`TauLib/BookI/Boundary/Bridge/TauRealCongruence.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Bridge/TauRealCongruence.lean#L272-L293)
- Source range: L272-L293
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Multiplication respects Cauchy equivalence under Cauchy hypotheses.**

    Given `equiv a₁ a₂`, `equiv b₁ b₂`, and `IsCauchy a₂`, `IsCauchy b₁`,
    we get `equiv (a₁ * b₁) (a₂ * b₂)`. The Cauchy hypotheses provide
    the boundedness witnesses needed by `mul_respects_equiv_right_of_bound`.

    Strategy: chain through `a₂ * b₁` as middle step.
       a₁ * b₁ ≈ a₂ * b₁  via right-bounded mul-congr (b₁ bounded)
       a₂ * b₁ ≈ a₂ * b₂  via right-bounded mul-congr after commutation -/
```

## Source Excerpt

```lean
theorem TauReal.mul_respects_equiv_under_cauchy
    (a₁ a₂ b₁ b₂ : TauReal)
    (h_a2_cauchy : a₂.IsCauchy) (h_b1_cauchy : b₁.IsCauchy)
    (ha : TauReal.equiv a₁ a₂) (hb : TauReal.equiv b₁ b₂) :
    TauReal.equiv (a₁.mul b₁) (a₂.mul b₂) := by
  obtain ⟨Mb, hMb_pos, hMb⟩ := h_b1_cauchy.bounded
  obtain ⟨Ma, hMa_pos, hMa⟩ := h_a2_cauchy.bounded
  -- Step 1: a₁ * b₁ ≈ a₂ * b₁ (using b₁ bound)
  have h_step1 :=
    TauReal.mul_respects_equiv_right_of_bound a₁ a₂ b₁ Mb hMb_pos hMb ha
  -- Step 2: a₂ * b₁ ≈ a₂ * b₂. By commutativity:
  --   a₂ * b₁ ≈ b₁ * a₂ (via taureal_mul_comm)
  --   b₁ * a₂ ≈ b₂ * a₂ (via mul_respects_equiv_right_of_bound, a₂ bound)
  --   b₂ * a₂ ≈ a₂ * b₂ (via taureal_mul_comm)
  have h_swap1 : TauReal.equiv (a₂.mul b₁) (b₁.mul a₂) := taureal_mul_comm a₂ b₁
  have h_step2_inner :=
    TauReal.mul_respects_equiv_right_of_bound b₁ b₂ a₂ Ma hMa_pos hMa hb
  have h_swap2 : TauReal.equiv (b₂.mul a₂) (a₂.mul b₂) := taureal_mul_comm b₂ a₂
  -- Chain everything via equiv_trans
  exact TauReal.equiv_trans h_step1
        (TauReal.equiv_trans h_swap1
          (TauReal.equiv_trans h_step2_inner h_swap2))
```
