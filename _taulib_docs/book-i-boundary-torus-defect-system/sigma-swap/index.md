---
{
  "projection_kind": "taulib_declaration",
  "title": "TorusDefect.sigmaSwap",
  "permalink": "/verify/taulib/docs/book-i-boundary-torus-defect-system/sigma-swap/",
  "summary_short": "`def` declaration in `TauLib.BookI.Boundary.TorusDefectSystem`.",
  "declaration_id": "TauLib.BookI.Boundary.TorusDefectSystem::TorusDefect.sigmaSwap",
  "declaration_slug": "sigma-swap",
  "kind": "def",
  "name": "TorusDefect.sigmaSwap",
  "module_name": "TauLib.BookI.Boundary.TorusDefectSystem",
  "module_url": "/verify/taulib/docs/book-i-boundary-torus-defect-system/",
  "source_line_start": 152,
  "source_line_end": 164,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TorusDefectSystem.lean#L152-L164",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TorusDefectSystem.lean#L152-L164",
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
- Source path: [`TauLib/BookI/Boundary/TorusDefectSystem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TorusDefectSystem.lean#L152-L164)
- Source range: L152-L164
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **σ-involution on TorusDefect**: swap lobe sides, fix crossing.

    Realises paper §4's `σ_n : T_n → T_n` as the
    B↔C lobe exchange with the crossing as the unique fixed
    element. -/
```

## Source Excerpt

```lean
def TorusDefect.sigmaSwap : TorusDefect → TorusDefect
  | bSide => cSide
  | cSide => bSide
  | crossing => crossing

@[simp] theorem TorusDefect.sigmaSwap_bSide :
    TorusDefect.sigmaSwap TorusDefect.bSide = TorusDefect.cSide := rfl

@[simp] theorem TorusDefect.sigmaSwap_cSide :
    TorusDefect.sigmaSwap TorusDefect.cSide = TorusDefect.bSide := rfl

@[simp] theorem TorusDefect.sigmaSwap_crossing :
    TorusDefect.sigmaSwap TorusDefect.crossing = TorusDefect.crossing := rfl
```
