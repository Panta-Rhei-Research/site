---
{
  "projection_kind": "taulib_declaration",
  "title": "piPlusENumericalAt",
  "permalink": "/verify/taulib/docs/book-i-boundary-numerical-projection/pi-plus-enumerical-at/",
  "summary_short": "`def` declaration in `TauLib.BookI.Boundary.NumericalProjection`.",
  "declaration_id": "TauLib.BookI.Boundary.NumericalProjection::piPlusENumericalAt",
  "declaration_slug": "pi-plus-enumerical-at",
  "kind": "def",
  "name": "piPlusENumericalAt",
  "module_name": "TauLib.BookI.Boundary.NumericalProjection",
  "module_url": "/verify/taulib/docs/book-i-boundary-numerical-projection/",
  "source_line_start": 127,
  "source_line_end": 128,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/NumericalProjection.lean#L127-L128",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.NumericalProjection",
        "url": "/verify/taulib/docs/book-i-boundary-numerical-projection/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/NumericalProjection.lean#L127-L128",
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

- Module: [TauLib.BookI.Boundary.NumericalProjection](/verify/taulib/docs/book-i-boundary-numerical-projection/)
- Source path: [`TauLib/BookI/Boundary/NumericalProjection.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/NumericalProjection.lean#L127-L128)
- Source range: L127-L128
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Convenience name**: the depth-`N` readout of `GerPi + GerE`. -/
```

## Source Excerpt

```lean
def piPlusENumericalAt (N : TauIdx) : Rat :=
  numericalReadoutAtDepth (TauReal.pi.add TauReal.e) N
```
