---
{
  "projection_kind": "taulib_declaration",
  "title": "FixStructure",
  "permalink": "/verify/taulib/docs/book-iv-strong-strong-vacuum/fix-structure/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Strong.StrongVacuum`.",
  "declaration_id": "TauLib.BookIV.Strong.StrongVacuum::FixStructure",
  "declaration_slug": "fix-structure",
  "kind": "structure",
  "name": "FixStructure",
  "module_name": "TauLib.BookIV.Strong.StrongVacuum",
  "module_url": "/verify/taulib/docs/book-iv-strong-strong-vacuum/",
  "source_line_start": 337,
  "source_line_end": 346,
  "registry_ids": [
    "IV.P86"
  ],
  "related_registry_items": [
    {
      "id": "IV.P86",
      "title": "Structure of Fix(s)",
      "url": "/registry/object/IV.P86/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/StrongVacuum.lean#L337-L346",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/StrongVacuum.lean#L337-L346",
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
- Source path: [`TauLib/BookIV/Strong/StrongVacuum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/StrongVacuum.lean#L337-L346)
- Source range: L337-L346
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P86` — Structure of Fix(s)

## Immediate Comment / Docstring

```lean
/-- [IV.P86] Fix(s)[n] is a subalgebra containing the identity;
    its omega-limit Fix(s) is a well-defined pro-algebra. -/
```

## Source Excerpt

```lean
structure FixStructure where
  /-- Subalgebra of End(H_partial[n])_eta. -/
  subalgebra : Bool := true
  /-- Contains identity. -/
  contains_id : Bool := true
  /-- Omega-limit is well-defined. -/
  omega_limit_defined : Bool := true
  /-- Encodes symmetries commuting with strong vacuum. -/
  symmetry_role : String := "symmetries commuting with Gamma_s^*"
  deriving Repr
```
