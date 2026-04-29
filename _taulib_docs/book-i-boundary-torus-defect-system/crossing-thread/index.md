---
{
  "projection_kind": "taulib_declaration",
  "title": "TorusDefectSystem.crossingThread",
  "permalink": "/verify/taulib/docs/book-i-boundary-torus-defect-system/crossing-thread/",
  "summary_short": "`def` declaration in `TauLib.BookI.Boundary.TorusDefectSystem`.",
  "declaration_id": "TauLib.BookI.Boundary.TorusDefectSystem::TorusDefectSystem.crossingThread",
  "declaration_slug": "crossing-thread",
  "kind": "def",
  "name": "TorusDefectSystem.crossingThread",
  "module_name": "TauLib.BookI.Boundary.TorusDefectSystem",
  "module_url": "/verify/taulib/docs/book-i-boundary-torus-defect-system/",
  "source_line_start": 206,
  "source_line_end": 210,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TorusDefectSystem.lean#L206-L210",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TorusDefectSystem.lean#L206-L210",
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

- Module: [TauLib.BookI.Boundary.TorusDefectSystem](/verify/taulib/docs/book-i-boundary-torus-defect-system/)
- Source path: [`TauLib/BookI/Boundary/TorusDefectSystem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TorusDefectSystem.lean#L206-L210)
- Source range: L206-L210
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **The crossing-anchored thread**: constant `crossing` at every depth.

    This is the Lean realisation of paper's `G_×[ω]` — the unique
    σ-fixed non-polar ω-germ — on this concrete instance. -/
```

## Source Excerpt

```lean
def TorusDefectSystem.crossingThread :
    DefectInverseSystem.SigmaFixedThread TorusDefectSystem where
  point := fun _ => TorusDefect.crossing
  compat := fun _ => rfl
  sigma_fixed := fun _ => rfl
```
