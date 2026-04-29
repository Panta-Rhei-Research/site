---
{
  "projection_kind": "taulib_declaration",
  "title": "HolEndMorphism.actSigmaFixed_commutes_proj",
  "permalink": "/verify/taulib/docs/book-i-boundary-universal-fixed-scalar/act-sigma-fixed-commutes-proj/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.UniversalFixedScalar`.",
  "declaration_id": "TauLib.BookI.Boundary.UniversalFixedScalar::HolEndMorphism.actSigmaFixed_commutes_proj",
  "declaration_slug": "act-sigma-fixed-commutes-proj",
  "kind": "theorem",
  "name": "HolEndMorphism.actSigmaFixed_commutes_proj",
  "module_name": "TauLib.BookI.Boundary.UniversalFixedScalar",
  "module_url": "/verify/taulib/docs/book-i-boundary-universal-fixed-scalar/",
  "source_line_start": 170,
  "source_line_end": 175,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/UniversalFixedScalar.lean#L170-L175",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/UniversalFixedScalar.lean#L170-L175",
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
- Source path: [`TauLib/BookI/Boundary/UniversalFixedScalar.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/UniversalFixedScalar.lean#L170-L175)
- Source range: L170-L175
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Thread-compatibility of the σ-fixed image** — a companion to
    `fixed_point_inheritance`: the σ-commutes-with-projection
    property lifts through `f.actSigmaFixed`.  This is the "passage
    to the inverse limit preserves σ-invariance" content at the
    abstract scaffold level. -/
```

## Source Excerpt

```lean
theorem HolEndMorphism.actSigmaFixed_commutes_proj
    {D : DefectInverseSystem} (f : HolEndMorphism D)
    (t : D.SigmaFixedThread) (n : Nat) :
    D.proj n (D.sigma_level (n + 1) ((f.actSigmaFixed t).point (n + 1)))
      = D.sigma_level n ((f.actSigmaFixed t).point n) :=
  D.sigma_thread_compatible (f.actSigmaFixed t).toThread n
```
