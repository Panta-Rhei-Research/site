---
{
  "projection_kind": "taulib_declaration",
  "title": "TorusDefect",
  "permalink": "/verify/taulib/docs/book-i-boundary-torus-defect-system/torus-defect/",
  "summary_short": "`inductive` declaration in `TauLib.BookI.Boundary.TorusDefectSystem`.",
  "declaration_id": "TauLib.BookI.Boundary.TorusDefectSystem::TorusDefect",
  "declaration_slug": "torus-defect",
  "kind": "inductive",
  "name": "TorusDefect",
  "module_name": "TauLib.BookI.Boundary.TorusDefectSystem",
  "module_url": "/verify/taulib/docs/book-i-boundary-torus-defect-system/",
  "source_line_start": 141,
  "source_line_end": 145,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TorusDefectSystem.lean#L141-L145",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TorusDefectSystem.lean#L141-L145",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "inductive",
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
- Source path: [`TauLib/BookI/Boundary/TorusDefectSystem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TorusDefectSystem.lean#L141-L145)
- Source range: L141-L145
- Kind: `inductive`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Concrete defect type** at each depth: three constructors
    encoding the two lobe sides plus the crossing anchor.

    - `bSide` = B-lobe side (paper's off-diagonal `b ∈ B_n`)
    - `cSide` = C-lobe side (paper's off-diagonal `c ∈ C_n`)
    - `crossing` = the crossing anchor (paper's `×`-labelled class)

    This is the **minimal non-trivial** off-diagonal defect carrier.
    The singleton `crossing` is σ-fixed; `bSide` and `cSide` swap
    under σ.

    A custom inductive type (rather than `Option (Fin 2)`) avoids
    `Fin`-destructuring pitfalls in subsequent proofs — a
    calibration lesson from the "three-iteration tactics-dance"
    playbook. -/
```

## Source Excerpt

```lean
inductive TorusDefect where
  | bSide   : TorusDefect
  | cSide   : TorusDefect
  | crossing : TorusDefect
  deriving DecidableEq, Repr
```
