---
{
  "projection_kind": "taulib_declaration",
  "title": "torusMwd",
  "permalink": "/verify/taulib/docs/book-i-boundary-torus-defect-system/torus-mwd/",
  "summary_short": "`def` declaration in `TauLib.BookI.Boundary.TorusDefectSystem`.",
  "declaration_id": "TauLib.BookI.Boundary.TorusDefectSystem::torusMwd",
  "declaration_slug": "torus-mwd",
  "kind": "def",
  "name": "torusMwd",
  "module_name": "TauLib.BookI.Boundary.TorusDefectSystem",
  "module_url": "/verify/taulib/docs/book-i-boundary-torus-defect-system/",
  "source_line_start": 273,
  "source_line_end": 275,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TorusDefectSystem.lean#L273-L275",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TorusDefectSystem.lean#L273-L275",
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
- Source path: [`TauLib/BookI/Boundary/TorusDefectSystem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TorusDefectSystem.lean#L273-L275)
- Source range: L273-L275
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Trivial mwd function**: every thread has maturity depth 0.
    On `TorusDefectSystem` this is appropriate because the unique
    σ-fixed thread is already crossing-anchored at depth 0 (indeed
    at every depth). -/
```

## Source Excerpt

```lean
def torusMwd :
    DefectInverseSystem.SigmaFixedThread TorusDefectSystem → Nat :=
  fun _ => 0
```
