---
{
  "projection_kind": "taulib_declaration",
  "title": "CrossingPointDefectGerm",
  "permalink": "/verify/taulib/docs/book-i-boundary-iota-tau-structural/crossing-point-defect-germ/",
  "summary_short": "`structure` declaration in `TauLib.BookI.Boundary.IotaTauStructural`.",
  "declaration_id": "TauLib.BookI.Boundary.IotaTauStructural::CrossingPointDefectGerm",
  "declaration_slug": "crossing-point-defect-germ",
  "kind": "structure",
  "name": "CrossingPointDefectGerm",
  "module_name": "TauLib.BookI.Boundary.IotaTauStructural",
  "module_url": "/verify/taulib/docs/book-i-boundary-iota-tau-structural/",
  "source_line_start": 96,
  "source_line_end": 103,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/IotaTauStructural.lean#L96-L103",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.IotaTauStructural",
        "url": "/verify/taulib/docs/book-i-boundary-iota-tau-structural/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/IotaTauStructural.lean#L96-L103",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
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

- Module: [TauLib.BookI.Boundary.IotaTauStructural](/verify/taulib/docs/book-i-boundary-iota-tau-structural/)
- Source path: [`TauLib/BookI/Boundary/IotaTauStructural.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/IotaTauStructural.lean#L96-L103)
- Source range: L96-L103
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The **crossing-point defect ω-germ** `Δ_ω` as a structural object:
    a depth-indexed family of TauRat values realising the defect
    inverse system `{T_n \ R_n}` of torus-projection failures.

    For Wave 7 we package this minimally as a refinement-compatible
    sequence of TauRat approximations — the same operational shape
    as `TauReal.approx`, plus a marker (`is_defect_germ`) connecting
    it to the lemniscate-boundary defect construction. -/
```

## Source Excerpt

```lean
structure CrossingPointDefectGerm where
  /-- The depth-indexed approximation sequence for the germ. -/
  approx : Nat → TauRat
  /-- Marker: this sequence arises from the lemniscate-boundary defect
      inverse system.  Refined by future waves with the full inverse-
      limit construction; for Wave 7 we treat it as an opaque
      "earned-via-defect-construction" witness. -/
  is_defect_germ : True
```
