---
{
  "projection_kind": "taulib_declaration",
  "title": "problem_part",
  "permalink": "/verify/taulib/docs/book-iii-doors-master-schema/problem-part/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Doors.MasterSchema`.",
  "declaration_id": "TauLib.BookIII.Doors.MasterSchema::problem_part",
  "declaration_slug": "problem-part",
  "kind": "def",
  "name": "problem_part",
  "module_name": "TauLib.BookIII.Doors.MasterSchema",
  "module_url": "/verify/taulib/docs/book-iii-doors-master-schema/",
  "source_line_start": 62,
  "source_line_end": 71,
  "registry_ids": [
    "III.T23"
  ],
  "related_registry_items": [
    {
      "id": "III.T23",
      "title": "Master Schema Theorem",
      "url": "/registry/object/III.T23/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/MasterSchema.lean#L62-L71",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Doors.MasterSchema",
        "url": "/verify/taulib/docs/book-iii-doors-master-schema/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/MasterSchema.lean#L62-L71",
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

- Module: [TauLib.BookIII.Doors.MasterSchema](/verify/taulib/docs/book-iii-doors-master-schema/)
- Source path: [`TauLib/BookIII/Doors/MasterSchema.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/MasterSchema.lean#L62-L71)
- Source range: L62-L71
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.T23` — Master Schema Theorem

## Immediate Comment / Docstring

```lean
/-- [III.T23] Part assignment (which Book III part treats each problem). -/
```

## Source Excerpt

```lean
def problem_part (p : MillenniumProblem) : TauIdx :=
  match p with
  | .RH => 4
  | .Poincare => 4
  | .NS => 5
  | .YM => 5
  | .Hodge => 5
  | .BSD => 6
  | .Langlands => 6
  | .PvsNP => 7
```
