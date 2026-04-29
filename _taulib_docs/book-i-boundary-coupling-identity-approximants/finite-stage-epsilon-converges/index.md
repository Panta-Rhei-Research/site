---
{
  "projection_kind": "taulib_declaration",
  "title": "finiteStageEpsilon_converges",
  "permalink": "/verify/taulib/docs/book-i-boundary-coupling-identity-approximants/finite-stage-epsilon-converges/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.CouplingIdentityApproximants`.",
  "declaration_id": "TauLib.BookI.Boundary.CouplingIdentityApproximants::finiteStageEpsilon_converges",
  "declaration_slug": "finite-stage-epsilon-converges",
  "kind": "theorem",
  "name": "finiteStageEpsilon_converges",
  "module_name": "TauLib.BookI.Boundary.CouplingIdentityApproximants",
  "module_url": "/verify/taulib/docs/book-i-boundary-coupling-identity-approximants/",
  "source_line_start": 229,
  "source_line_end": 257,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/CouplingIdentityApproximants.lean#L229-L257",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.CouplingIdentityApproximants",
        "url": "/verify/taulib/docs/book-i-boundary-coupling-identity-approximants/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/CouplingIdentityApproximants.lean#L229-L257",
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

- Module: [TauLib.BookI.Boundary.CouplingIdentityApproximants](/verify/taulib/docs/book-i-boundary-coupling-identity-approximants/)
- Source path: [`TauLib/BookI/Boundary/CouplingIdentityApproximants.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/CouplingIdentityApproximants.lean#L229-L257)
- Source range: L229-L257
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Paper §6.2's `ε_n → 0`, structural Cauchy form**: for every
    tolerance `1/(k+1)`, there exists a modulus `N(k)` such that
    `|ε_n|_{toRat} < 1/(k+1)` for all `n ≥ N(k)`.

    **Proved**: `ε_n → 0` is the Cauchy-equivalence witness of
    `coupling_identity_at_omega` — the same modulus that proves
    the ω-limit identity serves as the ε_n-bound modulus.

    The paper's claim about `ε_n = 0` at primorial depths
    specifically (paper's `thm:primorial-convergence`) is a sharper
    quantitative statement requiring the Book II Ch. 28 primorial-
    sieve machinery; here we land the qualitative `ε_n → 0`
    (Cauchy) form, which is what Wave 4's capstone delivers. -/
```

## Source Excerpt

```lean
theorem finiteStageEpsilon_converges :
    ∃ μ : Nat → Nat, ∀ k n, n ≥ μ k →
      (finiteStageEpsilon n).abs.toRat < 1 / ((k : Rat) + 1) := by
  obtain ⟨μ, hμ⟩ := coupling_identity_at_omega
  refine ⟨μ, fun k n hn => ?_⟩
  have h_base := hμ k n hn
  -- h_base: TauRat.lt (ofNatRecip k) (((iota·(π+e)).approx n).sub (two.approx n)).abs
  -- or with the other direction; let's normalise via rewrites.
  unfold TauRat.lt at h_base
  rw [TauRat.toRat_abs, toRat_sub, TauRat.ofNatRecip_toRat] at h_base
  -- h_base now (after rewrites): |(iota·(π+e)).approx n .toRat - (two.approx n).toRat|
  --                                  < 1 / ((k : Rat) + 1)
  -- or with the inequality flipped depending on equiv's direction.
  --
  -- Bridge: ((iota·(π+e)).approx n) = (iota.approx n).mul ((π+e).approx n)
  --                                 = (iota.approx n).mul ((π.approx n).add (e.approx n))
  -- at the TauRat struct level.  The toRat values match.
  have h_lhs_eq :
      ((TauReal.iota_tau.mul (TauReal.pi.add TauReal.e)).approx n).toRat =
      ((TauReal.iota_tau.approx n).mul
        ((TauReal.pi.approx n).add (TauReal.e.approx n))).toRat := by
    show ((TauReal.iota_tau.approx n).mul
            ((TauReal.pi.approx n).add (TauReal.e.approx n))).toRat = _
    rfl
  rw [h_lhs_eq] at h_base
  -- Goal: (finiteStageEpsilon n).abs.toRat < 1 / ((k : Rat) + 1)
  unfold finiteStageEpsilon iotaApproxAt piApproxAt eApproxAt twoApproxAt
  rw [TauRat.toRat_abs, toRat_sub]
  exact h_base
```
