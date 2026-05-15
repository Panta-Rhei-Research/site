---
{
  "projection_kind": "taulib_declaration",
  "title": "trivial_actSigmaFixed_identity",
  "permalink": "/corpus/taulib/docs/book-i-boundary-universal-fixed-scalar/trivial-act-sigma-fixed-identity/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.UniversalFixedScalar`.",
  "declaration_id": "TauLib.BookI.Boundary.UniversalFixedScalar::trivial_actSigmaFixed_identity",
  "declaration_slug": "trivial-act-sigma-fixed-identity",
  "kind": "theorem",
  "name": "trivial_actSigmaFixed_identity",
  "module_name": "TauLib.BookI.Boundary.UniversalFixedScalar",
  "module_url": "/corpus/taulib/docs/book-i-boundary-universal-fixed-scalar/",
  "source_line_start": 371,
  "source_line_end": 377,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/UniversalFixedScalar.lean#L371-L377",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.UniversalFixedScalar",
        "url": "/corpus/taulib/docs/book-i-boundary-universal-fixed-scalar/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/UniversalFixedScalar.lean#L371-L377",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "role": "proof obligation",
      "status": "formal proof obligation checked"
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

- Module: [TauLib.BookI.Boundary.UniversalFixedScalar](/corpus/taulib/docs/book-i-boundary-universal-fixed-scalar/)
- Source path: [`TauLib/BookI/Boundary/UniversalFixedScalar.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/UniversalFixedScalar.lean#L371-L377)
- Source range: L371-L377
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **The trivial HolEndMorphism is the identity on its
    SigmaFixedThread**: a sanity check on `actSigmaFixed`'s
    definition. -/
```

## Source Excerpt

```lean
theorem trivial_actSigmaFixed_identity (n : Nat) :
    (TrivialHolEndMorphism.actSigmaFixed
       TrivialDefectSystem.trivialThread).point n
      = TrivialDefectSystem.trivialThread.point n :=
  rfl

end Tau.Boundary
```
