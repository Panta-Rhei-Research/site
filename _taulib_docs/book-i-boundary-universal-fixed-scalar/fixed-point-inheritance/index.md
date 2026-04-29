---
{
  "projection_kind": "taulib_declaration",
  "title": "HolEndMorphism.fixed_point_inheritance",
  "permalink": "/verify/taulib/docs/book-i-boundary-universal-fixed-scalar/fixed-point-inheritance/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.UniversalFixedScalar`.",
  "declaration_id": "TauLib.BookI.Boundary.UniversalFixedScalar::HolEndMorphism.fixed_point_inheritance",
  "declaration_slug": "fixed-point-inheritance",
  "kind": "theorem",
  "name": "HolEndMorphism.fixed_point_inheritance",
  "module_name": "TauLib.BookI.Boundary.UniversalFixedScalar",
  "module_url": "/verify/taulib/docs/book-i-boundary-universal-fixed-scalar/",
  "source_line_start": 158,
  "source_line_end": 163,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/UniversalFixedScalar.lean#L158-L163",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/UniversalFixedScalar.lean#L158-L163",
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
- Source path: [`TauLib/BookI/Boundary/UniversalFixedScalar.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/UniversalFixedScalar.lean#L158-L163)
- Source range: L158-L163
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Fixed-point inheritance under σ-equivariance**
    (paper Proposition 5.6, `prop:fixed-inheritance`): if `f` is a
    HolEnd_τ morphism and `t` is a σ-fixed thread, then `f.act t`
    is σ-fixed.

    Proof: direct from `HolEndMorphism.preserves_sigma_fixed`
    applied to `t.sigma_fixed`.  Structurally, the codomain of
    `actSigmaFixed` is `SigmaFixedThread`, so σ-fixedness is
    built in.

    This is the σ-equivariance content of paper's one-line proof:
    `σ(f(G)) = f(σ(G)) = f(G)`. -/
```

## Source Excerpt

```lean
theorem HolEndMorphism.fixed_point_inheritance
    {D : DefectInverseSystem} (f : HolEndMorphism D)
    (t : D.SigmaFixedThread) :
    ∀ n, D.sigma_level n ((f.actSigmaFixed t).point n) =
         (f.actSigmaFixed t).point n :=
  (f.actSigmaFixed t).sigma_fixed
```
