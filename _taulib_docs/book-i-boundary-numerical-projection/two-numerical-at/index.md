---
{
  "projection_kind": "taulib_declaration",
  "title": "twoNumericalAt",
  "permalink": "/corpus/taulib/docs/book-i-boundary-numerical-projection/two-numerical-at/",
  "summary_short": "`def` declaration in `TauLib.BookI.Boundary.NumericalProjection`.",
  "declaration_id": "TauLib.BookI.Boundary.NumericalProjection::twoNumericalAt",
  "declaration_slug": "two-numerical-at",
  "kind": "def",
  "name": "twoNumericalAt",
  "module_name": "TauLib.BookI.Boundary.NumericalProjection",
  "module_url": "/corpus/taulib/docs/book-i-boundary-numerical-projection/",
  "source_line_start": 111,
  "source_line_end": 112,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/NumericalProjection.lean#L111-L112",
  "formal_status": "defined",
  "declaration_role": "definition",
  "formal_status_label": "definition",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.NumericalProjection",
        "url": "/corpus/taulib/docs/book-i-boundary-numerical-projection/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/NumericalProjection.lean#L111-L112",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "role": "definition",
      "status": "definition"
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

- Module: [TauLib.BookI.Boundary.NumericalProjection](/corpus/taulib/docs/book-i-boundary-numerical-projection/)
- Source path: [`TauLib/BookI/Boundary/NumericalProjection.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/NumericalProjection.lean#L111-L112)
- Source range: L111-L112
- Kind: `def`
- Public role: `definition`
- Formal status hint: `definition`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Convenience name**: the depth-`N` readout of `Ger2`. -/
```

## Source Excerpt

```lean
def twoNumericalAt (N : TauIdx) : Rat :=
  numericalReadoutAtDepth TauReal.two N
```
