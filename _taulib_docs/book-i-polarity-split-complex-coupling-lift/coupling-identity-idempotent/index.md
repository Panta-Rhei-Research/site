---
{
  "projection_kind": "taulib_declaration",
  "title": "coupling_identity_idempotent",
  "permalink": "/verify/taulib/docs/book-i-polarity-split-complex-coupling-lift/coupling-identity-idempotent/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Polarity.SplitComplexCouplingLift`.",
  "declaration_id": "TauLib.BookI.Polarity.SplitComplexCouplingLift::coupling_identity_idempotent",
  "declaration_slug": "coupling-identity-idempotent",
  "kind": "theorem",
  "name": "coupling_identity_idempotent",
  "module_name": "TauLib.BookI.Polarity.SplitComplexCouplingLift",
  "module_url": "/verify/taulib/docs/book-i-polarity-split-complex-coupling-lift/",
  "source_line_start": 217,
  "source_line_end": 222,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/SplitComplexCouplingLift.lean#L217-L222",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Polarity.SplitComplexCouplingLift",
        "url": "/verify/taulib/docs/book-i-polarity-split-complex-coupling-lift/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/SplitComplexCouplingLift.lean#L217-L222",
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

- Module: [TauLib.BookI.Polarity.SplitComplexCouplingLift](/verify/taulib/docs/book-i-polarity-split-complex-coupling-lift/)
- Source path: [`TauLib/BookI/Polarity/SplitComplexCouplingLift.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/SplitComplexCouplingLift.lean#L217-L222)
- Source range: L217-L222
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Paper §7.4 Proposition 7.11 `cor:idempotent-lift`**:
    the coupling identity at the idempotent-decomposed level:

      `ι_τ · Tr_+(w_ω) ≡ 2`   (Cauchy equivalence on TauReal)

    Equivalently, `ι_τ = 2 / (π_τ + e_τ)` rendered through the
    additive trace of the idempotent-decomposed clock.

    Per paper Remark `lift-not-derivation`, this is a notational
    repackaging of `coupling_identity_at_omega` (Wave 15 / paper
    Thm 6.3).  The structural content is in the *placement* of
    π_τ and e_τ in the e_+ and e_- sectors respectively, which is
    forced by σ-equivariance + HolEnd_τ universality (paper
    Lemma 6.2 Step 2b). -/
```

## Source Excerpt

```lean
theorem coupling_identity_idempotent :
    TauReal.equiv
      (TauReal.iota_tau.mul (WOmega.trPlus wOmega))
      TauReal.two := by
  rw [WOmega.trPlus_wOmega]
  exact coupling_identity_at_omega
```
