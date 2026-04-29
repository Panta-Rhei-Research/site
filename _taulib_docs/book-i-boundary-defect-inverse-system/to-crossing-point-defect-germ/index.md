---
{
  "projection_kind": "taulib_declaration",
  "title": "DefectInverseSystem.toCrossingPointDefectGerm",
  "permalink": "/verify/taulib/docs/book-i-boundary-defect-inverse-system/to-crossing-point-defect-germ/",
  "summary_short": "`def` declaration in `TauLib.BookI.Boundary.DefectInverseSystem`.",
  "declaration_id": "TauLib.BookI.Boundary.DefectInverseSystem::DefectInverseSystem.toCrossingPointDefectGerm",
  "declaration_slug": "to-crossing-point-defect-germ",
  "kind": "def",
  "name": "DefectInverseSystem.toCrossingPointDefectGerm",
  "module_name": "TauLib.BookI.Boundary.DefectInverseSystem",
  "module_url": "/verify/taulib/docs/book-i-boundary-defect-inverse-system/",
  "source_line_start": 355,
  "source_line_end": 360,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/DefectInverseSystem.lean#L355-L360",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.DefectInverseSystem",
        "url": "/verify/taulib/docs/book-i-boundary-defect-inverse-system/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/DefectInverseSystem.lean#L355-L360",
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

- Module: [TauLib.BookI.Boundary.DefectInverseSystem](/verify/taulib/docs/book-i-boundary-defect-inverse-system/)
- Source path: [`TauLib/BookI/Boundary/DefectInverseSystem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/DefectInverseSystem.lean#L355-L360)
- Source range: L355-L360
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Bridge to Wave 7's `CrossingPointDefectGerm`**: a σ-fixed
    thread in a `DefectInverseSystem`, paired with a levelwise
    readout, gives a `CrossingPointDefectGerm` — the Wave 7 type
    capturing the operational scalar-readout side.

    This closes the structural loop: the abstract defect system
    of this module supplies the inverse-system side; Wave 7's
    `CrossingPointDefectGerm` supplies the scalar-readout side;
    the bridge here connects them. -/
```

## Source Excerpt

```lean
def DefectInverseSystem.toCrossingPointDefectGerm
    (D : DefectInverseSystem)
    (readout_level : ∀ n, D.defect_level n → TauRat)
    (t : D.Thread) : CrossingPointDefectGerm where
  approx := D.threadReadout readout_level t
  is_defect_germ := trivial
```
