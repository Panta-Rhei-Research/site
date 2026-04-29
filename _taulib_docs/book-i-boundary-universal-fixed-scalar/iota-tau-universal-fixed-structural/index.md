---
{
  "projection_kind": "taulib_declaration",
  "title": "iota_tau_universal_fixed_structural",
  "permalink": "/verify/taulib/docs/book-i-boundary-universal-fixed-scalar/iota-tau-universal-fixed-structural/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.UniversalFixedScalar`.",
  "declaration_id": "TauLib.BookI.Boundary.UniversalFixedScalar::iota_tau_universal_fixed_structural",
  "declaration_slug": "iota-tau-universal-fixed-structural",
  "kind": "theorem",
  "name": "iota_tau_universal_fixed_structural",
  "module_name": "TauLib.BookI.Boundary.UniversalFixedScalar",
  "module_url": "/verify/taulib/docs/book-i-boundary-universal-fixed-scalar/",
  "source_line_start": 324,
  "source_line_end": 345,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/UniversalFixedScalar.lean#L324-L345",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.UniversalFixedScalar",
        "url": "/verify/taulib/docs/book-i-boundary-universal-fixed-scalar/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/UniversalFixedScalar.lean#L324-L345",
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

- Module: [TauLib.BookI.Boundary.UniversalFixedScalar](/verify/taulib/docs/book-i-boundary-universal-fixed-scalar/)
- Source path: [`TauLib/BookI/Boundary/UniversalFixedScalar.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/UniversalFixedScalar.lean#L324-L345)
- Source range: L324-L345
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Master constant `ι_τ` as universal fixed scalar**
    (paper Definition `def:iota-tau` + Corollary 5.8).

    The paper defines `ι_τ := Read_F(G_×[ω]) = Read_F(Δ_ω)` as the
    canonical scalar readout of the crossing-point defect germ,
    and Corollary 5.8 asserts it is universally fixed.

    At the TauLib level: we already have Wave 7's
    `CrossingPointDefectGerm` with its scalar readout via
    `toTauReal`, and Wave 4's operational `TauReal.iota_tau`.
    The universal-fixed-scalar theorem at the concrete level is:
    for any HolEnd_τ morphism `f` lifting to a `CrossingPointDefectGerm`
    action, `f.readout ≡ TauReal.iota_tau` at Cauchy equivalence.

    Rendered here as a **structural observation** tying the
    abstract `universal_fixed_scalar` back to the operational
    `iota_tau` — the concrete instantiation is deferred to a
    future wave that supplies the geometric `DefectInverseSystem`
    instance with the `anchor` / `mwd` machinery satisfying
    singleton uniqueness. -/
```

## Source Excerpt

```lean
theorem iota_tau_universal_fixed_structural
    {D : DefectInverseSystem}
    {anchor : ∀ n, D.defect_level n → Prop}
    {mwd : D.SigmaFixedThread → Nat}
    (f : HolEndMorphismFull D anchor mwd)
    (g : D.SigmaFixedThread)
    (h_g : DefectInverseSystem.IsCrossingPoint anchor mwd g)
    (singleton_uniqueness :
      ∀ t₁ t₂ : D.SigmaFixedThread,
        DefectInverseSystem.IsCrossingPoint anchor mwd t₁ →
        DefectInverseSystem.IsCrossingPoint anchor mwd t₂ →
        t₁ = t₂)
    (readout_level : ∀ n, D.defect_level n → TauRat)
    (iota_approx_eq :
      ∀ n, D.threadReadout readout_level g.toThread n =
           TauReal.iota_tau.approx n) :
    ∀ n, D.threadReadout readout_level
           (f.toHolEndMorphism.actSigmaFixed g).toThread n =
         TauReal.iota_tau.approx n := by
  intro n
  rw [f.threadReadout_universal_fixed g h_g singleton_uniqueness readout_level n]
  exact iota_approx_eq n
```
