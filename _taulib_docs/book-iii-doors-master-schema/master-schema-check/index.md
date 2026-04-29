---
{
  "projection_kind": "taulib_declaration",
  "title": "master_schema_check",
  "permalink": "/verify/taulib/docs/book-iii-doors-master-schema/master-schema-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Doors.MasterSchema`.",
  "declaration_id": "TauLib.BookIII.Doors.MasterSchema::master_schema_check",
  "declaration_slug": "master-schema-check",
  "kind": "def",
  "name": "master_schema_check",
  "module_name": "TauLib.BookIII.Doors.MasterSchema",
  "module_url": "/verify/taulib/docs/book-iii-doors-master-schema/",
  "source_line_start": 105,
  "source_line_end": 116,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/MasterSchema.lean#L105-L116",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/MasterSchema.lean#L105-L116",
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
- Source path: [`TauLib/BookIII/Doors/MasterSchema.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/MasterSchema.lean#L105-L116)
- Source range: L105-L116
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.T23` — Master Schema Theorem

## Immediate Comment / Docstring

```lean
/-- [III.T23] Master Schema: assemble all eight problem schemas. -/
```

## Source Excerpt

```lean
def master_schema_check (bound db : TauIdx) : Bool :=
  -- E₀ level: RH and Poincaré
  let e0_ok := rh_schema_check bound db && poincare_schema_check bound db
  -- E₁ level: NS, YM, Hodge — verify all at E₁ + template ready
  let e1_ok := generic_schema_check bound db &&
    problem_level .NS == .E1 && problem_level .YM == .E1 &&
    problem_level .Hodge == .E1
  -- E₂ level: BSD, Langlands, P vs NP — verify all at E₂ + template ready
  let e2_ok := generic_schema_check bound db &&
    problem_level .BSD == .E2 && problem_level .Langlands == .E2 &&
    problem_level .PvsNP == .E2
  e0_ok && e1_ok && e2_ok
```
