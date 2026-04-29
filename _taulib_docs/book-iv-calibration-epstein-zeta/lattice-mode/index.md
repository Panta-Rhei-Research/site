---
{
  "projection_kind": "taulib_declaration",
  "title": "LatticeMode",
  "permalink": "/verify/taulib/docs/book-iv-calibration-epstein-zeta/lattice-mode/",
  "summary_short": "`inductive` declaration in `TauLib.BookIV.Calibration.EpsteinZeta`.",
  "declaration_id": "TauLib.BookIV.Calibration.EpsteinZeta::LatticeMode",
  "declaration_slug": "lattice-mode",
  "kind": "inductive",
  "name": "LatticeMode",
  "module_name": "TauLib.BookIV.Calibration.EpsteinZeta",
  "module_url": "/verify/taulib/docs/book-iv-calibration-epstein-zeta/",
  "source_line_start": 148,
  "source_line_end": 151,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/EpsteinZeta.lean#L148-L151",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Calibration.EpsteinZeta",
        "url": "/verify/taulib/docs/book-iv-calibration-epstein-zeta/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/EpsteinZeta.lean#L148-L151",
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

- Module: [TauLib.BookIV.Calibration.EpsteinZeta](/verify/taulib/docs/book-iv-calibration-epstein-zeta/)
- Source path: [`TauLib/BookIV/Calibration/EpsteinZeta.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/EpsteinZeta.lean#L148-L151)
- Source range: L148-L151
- Kind: `inductive`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Lattice modes classified by their role in the zeta sum. -/
```

## Source Excerpt

```lean
inductive LatticeMode
  | Axis      -- (m, 0) or (0, n): axis modes
  | Interior  -- (m, n) with m ≠ 0, n ≠ 0: interior modes
  deriving Repr, DecidableEq
```
