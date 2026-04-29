---
{
  "projection_kind": "taulib_declaration",
  "title": "TrivialHolEndMorphism",
  "permalink": "/verify/taulib/docs/book-i-boundary-universal-fixed-scalar/trivial-hol-end-morphism/",
  "summary_short": "`def` declaration in `TauLib.BookI.Boundary.UniversalFixedScalar`.",
  "declaration_id": "TauLib.BookI.Boundary.UniversalFixedScalar::TrivialHolEndMorphism",
  "declaration_slug": "trivial-hol-end-morphism",
  "kind": "def",
  "name": "TrivialHolEndMorphism",
  "module_name": "TauLib.BookI.Boundary.UniversalFixedScalar",
  "module_url": "/verify/taulib/docs/book-i-boundary-universal-fixed-scalar/",
  "source_line_start": 354,
  "source_line_end": 356,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/UniversalFixedScalar.lean#L354-L356",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/UniversalFixedScalar.lean#L354-L356",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
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
- Source path: [`TauLib/BookI/Boundary/UniversalFixedScalar.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/UniversalFixedScalar.lean#L354-L356)
- Source range: L354-L356
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Trivial HolEnd_τ morphism** on `TrivialDefectSystem`: the
    identity action.  Sanity check that the scaffold compiles
    end-to-end. -/
```

## Source Excerpt

```lean
def TrivialHolEndMorphism : HolEndMorphism TrivialDefectSystem where
  act t := t
  preserves_sigma_fixed := fun _ h_sigma => h_sigma
```
