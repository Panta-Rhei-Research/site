---
{
  "projection_kind": "taulib_declaration",
  "title": "SubjectToolCollapse",
  "permalink": "/verify/taulib/docs/book-vii-final-boundary/subject-tool-collapse/",
  "summary_short": "`structure` declaration in `TauLib.BookVII.Final.Boundary`.",
  "declaration_id": "TauLib.BookVII.Final.Boundary::SubjectToolCollapse",
  "declaration_slug": "subject-tool-collapse",
  "kind": "structure",
  "name": "SubjectToolCollapse",
  "module_name": "TauLib.BookVII.Final.Boundary",
  "module_url": "/verify/taulib/docs/book-vii-final-boundary/",
  "source_line_start": 147,
  "source_line_end": 154,
  "registry_ids": [
    "VII.D89"
  ],
  "related_registry_items": [
    {
      "id": "VII.D89",
      "title": "Subject-Tool Collapse",
      "url": "/registry/object/VII.D89/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Final/Boundary.lean#L147-L154",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVII.Final.Boundary",
        "url": "/verify/taulib/docs/book-vii-final-boundary/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Final/Boundary.lean#L147-L154",
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

- Module: [TauLib.BookVII.Final.Boundary](/verify/taulib/docs/book-vii-final-boundary/)
- Source path: [`TauLib/BookVII/Final/Boundary.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Final/Boundary.lean#L147-L154)
- Source range: L147-L154
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VII.D89` — Subject-Tool Collapse

## Immediate Comment / Docstring

```lean
/-- [VII.D89] Subject-Tool Collapse (ch122). Boundary condition where
    the investigating subject and the formal tool become indistinguishable.
    At S_L, the proof (tool) and the prover's commitment (subject) are
    the same structural datum. The subject cannot step outside the tool
    without leaving S_L. -/
```

## Source Excerpt

```lean
structure SubjectToolCollapse where
  /-- Boundary condition. -/
  boundary_condition : Bool := true
  /-- Subject-tool indistinguishable at S_L. -/
  collapse : Bool := true
  /-- Cannot step outside without leaving S_L. -/
  no_external_standpoint : Bool := true
  deriving Repr
```
