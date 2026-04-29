---
{
  "projection_kind": "taulib_declaration",
  "title": "HolEndMorphismFull",
  "permalink": "/verify/taulib/docs/book-i-boundary-universal-fixed-scalar/hol-end-morphism-full/",
  "summary_short": "`structure` declaration in `TauLib.BookI.Boundary.UniversalFixedScalar`.",
  "declaration_id": "TauLib.BookI.Boundary.UniversalFixedScalar::HolEndMorphismFull",
  "declaration_slug": "hol-end-morphism-full",
  "kind": "structure",
  "name": "HolEndMorphismFull",
  "module_name": "TauLib.BookI.Boundary.UniversalFixedScalar",
  "module_url": "/verify/taulib/docs/book-i-boundary-universal-fixed-scalar/",
  "source_line_start": 185,
  "source_line_end": 196,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/UniversalFixedScalar.lean#L185-L196",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/UniversalFixedScalar.lean#L185-L196",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
      "status": "defined"
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
- Source path: [`TauLib/BookI/Boundary/UniversalFixedScalar.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/UniversalFixedScalar.lean#L185-L196)
- Source range: L185-L196
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **HolEnd_τ morphism equipped with NP / OA preservation data**.
    Extending `HolEndMorphism` with the paper's "preserves
    polarisation status" and "preserves ω-approach" content
    (paper Thm 5.7 proof lines 1567–1572). -/
```

## Source Excerpt

```lean
structure HolEndMorphismFull (D : DefectInverseSystem)
    (anchor : ∀ n, D.defect_level n → Prop)
    (mwd : D.SigmaFixedThread → Nat) extends HolEndMorphism D where
  /-- Preserves the non-polarity half (paper §5.2). -/
  preserves_NP : ∀ (t : D.SigmaFixedThread),
    DefectInverseSystem.IsNonPolar anchor t →
    DefectInverseSystem.IsNonPolar anchor (toHolEndMorphism.actSigmaFixed t)
  /-- Preserves the ω-approach half (paper §5.3). -/
  preserves_OA : ∀ (t : D.SigmaFixedThread),
    DefectInverseSystem.IsOmegaApproaching mwd t →
    DefectInverseSystem.IsOmegaApproaching mwd
      (toHolEndMorphism.actSigmaFixed t)
```
