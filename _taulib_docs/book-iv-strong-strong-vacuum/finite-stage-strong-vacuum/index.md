---
{
  "projection_kind": "taulib_declaration",
  "title": "FiniteStageStrongVacuum",
  "permalink": "/verify/taulib/docs/book-iv-strong-strong-vacuum/finite-stage-strong-vacuum/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Strong.StrongVacuum`.",
  "declaration_id": "TauLib.BookIV.Strong.StrongVacuum::FiniteStageStrongVacuum",
  "declaration_slug": "finite-stage-strong-vacuum",
  "kind": "structure",
  "name": "FiniteStageStrongVacuum",
  "module_name": "TauLib.BookIV.Strong.StrongVacuum",
  "module_url": "/verify/taulib/docs/book-iv-strong-strong-vacuum/",
  "source_line_start": 234,
  "source_line_end": 243,
  "registry_ids": [
    "IV.D149"
  ],
  "related_registry_items": [
    {
      "id": "IV.D149",
      "title": "Finite-stage strong vacuum",
      "url": "/registry/object/IV.D149/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/StrongVacuum.lean#L234-L243",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Strong.StrongVacuum",
        "url": "/verify/taulib/docs/book-iv-strong-strong-vacuum/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/StrongVacuum.lean#L234-L243",
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

- Module: [TauLib.BookIV.Strong.StrongVacuum](/verify/taulib/docs/book-iv-strong-strong-vacuum/)
- Source path: [`TauLib/BookIV/Strong/StrongVacuum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/StrongVacuum.lean#L234-L243)
- Source range: L234-L243
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D149` — Finite-stage strong vacuum

## Immediate Comment / Docstring

```lean
/-- [IV.D149] The finite-stage strong vacuum Gamma_s^*[n]:
    argmin of Delta_n^s over Adm_s[n] with NFMin tie-breaking. -/
```

## Source Excerpt

```lean
structure FiniteStageStrongVacuum where
  /-- Stage n. -/
  stage : Nat
  /-- Minimizes defect functional. -/
  is_argmin : Bool := true
  /-- NFMin tie-breaking among minimizers. -/
  nfmin_tiebreak : Bool := true
  /-- Unique after tie-breaking. -/
  unique : Bool := true
  deriving Repr
```
