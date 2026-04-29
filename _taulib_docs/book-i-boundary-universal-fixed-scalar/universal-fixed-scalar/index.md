---
{
  "projection_kind": "taulib_declaration",
  "title": "HolEndMorphismFull.universal_fixed_scalar",
  "permalink": "/verify/taulib/docs/book-i-boundary-universal-fixed-scalar/universal-fixed-scalar/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.UniversalFixedScalar`.",
  "declaration_id": "TauLib.BookI.Boundary.UniversalFixedScalar::HolEndMorphismFull.universal_fixed_scalar",
  "declaration_slug": "universal-fixed-scalar",
  "kind": "theorem",
  "name": "HolEndMorphismFull.universal_fixed_scalar",
  "module_name": "TauLib.BookI.Boundary.UniversalFixedScalar",
  "module_url": "/verify/taulib/docs/book-i-boundary-universal-fixed-scalar/",
  "source_line_start": 259,
  "source_line_end": 275,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/UniversalFixedScalar.lean#L259-L275",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/UniversalFixedScalar.lean#L259-L275",
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
- Source path: [`TauLib/BookI/Boundary/UniversalFixedScalar.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/UniversalFixedScalar.lean#L259-L275)
- Source range: L259-L275
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Universal fixed scalar** (paper Corollary 5.8,
    `cor:iota-universal`) at the abstract readout level.

    Given the universal-fixed property at the thread level, the
    scalar readout is fixed by the induced action of `f` on
    `Read_F`.  Paper proof: immediate from Theorem 5.7 by
    applying `Read_F`. -/
```

## Source Excerpt

```lean
theorem HolEndMorphismFull.universal_fixed_scalar
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
    (readout_level : ∀ n, D.defect_level n → TauRat) :
    D.threadReadoutTauReal readout_level
      (f.toHolEndMorphism.actSigmaFixed g).toThread =
    D.threadReadoutTauReal readout_level g.toThread := by
  rw [f.universal_fixed_theorem g h_g singleton_uniqueness]
```
