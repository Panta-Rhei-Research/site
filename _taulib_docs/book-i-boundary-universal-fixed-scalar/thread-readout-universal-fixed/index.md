---
{
  "projection_kind": "taulib_declaration",
  "title": "HolEndMorphismFull.threadReadout_universal_fixed",
  "permalink": "/verify/taulib/docs/book-i-boundary-universal-fixed-scalar/thread-readout-universal-fixed/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.UniversalFixedScalar`.",
  "declaration_id": "TauLib.BookI.Boundary.UniversalFixedScalar::HolEndMorphismFull.threadReadout_universal_fixed",
  "declaration_slug": "thread-readout-universal-fixed",
  "kind": "theorem",
  "name": "HolEndMorphismFull.threadReadout_universal_fixed",
  "module_name": "TauLib.BookI.Boundary.UniversalFixedScalar",
  "module_url": "/verify/taulib/docs/book-i-boundary-universal-fixed-scalar/",
  "source_line_start": 282,
  "source_line_end": 298,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/UniversalFixedScalar.lean#L282-L298",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/UniversalFixedScalar.lean#L282-L298",
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
- Source path: [`TauLib/BookI/Boundary/UniversalFixedScalar.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/UniversalFixedScalar.lean#L282-L298)
- Source range: L282-L298
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Abstract universal fixed scalar (statement-level form)** —
    records the paper's Corollary 5.8 claim as a structural
    identity *without* requiring the scalar readout to be supplied
    at the point of statement.  This is the "ι_τ is universally
    fixed" claim at the most general abstract level. -/
```

## Source Excerpt

```lean
theorem HolEndMorphismFull.threadReadout_universal_fixed
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
    (readout_level : ∀ n, D.defect_level n → TauRat) (n : Nat) :
    D.threadReadout readout_level
      (f.toHolEndMorphism.actSigmaFixed g).toThread n =
    D.threadReadout readout_level g.toThread n := by
  rw [f.universal_fixed_theorem g h_g singleton_uniqueness]
```
