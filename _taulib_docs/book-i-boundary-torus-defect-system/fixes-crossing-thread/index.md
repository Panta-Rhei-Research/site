---
{
  "projection_kind": "taulib_declaration",
  "title": "TorusIdentity.fixes_crossing_thread",
  "permalink": "/verify/taulib/docs/book-i-boundary-torus-defect-system/fixes-crossing-thread/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.TorusDefectSystem`.",
  "declaration_id": "TauLib.BookI.Boundary.TorusDefectSystem::TorusIdentity.fixes_crossing_thread",
  "declaration_slug": "fixes-crossing-thread",
  "kind": "theorem",
  "name": "TorusIdentity.fixes_crossing_thread",
  "module_name": "TauLib.BookI.Boundary.TorusDefectSystem",
  "module_url": "/verify/taulib/docs/book-i-boundary-torus-defect-system/",
  "source_line_start": 370,
  "source_line_end": 378,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TorusDefectSystem.lean#L370-L378",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.TorusDefectSystem",
        "url": "/verify/taulib/docs/book-i-boundary-torus-defect-system/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TorusDefectSystem.lean#L370-L378",
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

- Module: [TauLib.BookI.Boundary.TorusDefectSystem](/verify/taulib/docs/book-i-boundary-torus-defect-system/)
- Source path: [`TauLib/BookI/Boundary/TorusDefectSystem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TorusDefectSystem.lean#L370-L378)
- Source range: L370-L378
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Specialisation to the concrete crossing thread**: the identity
    fixes the crossing thread unconditionally and **computationally**
    (no hypotheses at all).

    This is the sharpest form of the litmus test: the entire Wave 12
    + Wave 13 structural scaffold applied to a specific concrete
    thread with no external dependencies. -/
```

## Source Excerpt

```lean
theorem TorusIdentity.fixes_crossing_thread :
    TorusIdentityFull.toHolEndMorphism.actSigmaFixed
      TorusDefectSystem.crossingThread =
    TorusDefectSystem.crossingThread :=
  TorusIdentity.universal_fixed_unconditional
    TorusDefectSystem.crossingThread
    TorusDefectSystem.crossingThread_is_crossingPoint

end Tau.Boundary
```
