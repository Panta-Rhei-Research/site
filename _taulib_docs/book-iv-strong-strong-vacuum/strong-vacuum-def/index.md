---
{
  "projection_kind": "taulib_declaration",
  "title": "StrongVacuumDef",
  "permalink": "/verify/taulib/docs/book-iv-strong-strong-vacuum/strong-vacuum-def/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Strong.StrongVacuum`.",
  "declaration_id": "TauLib.BookIV.Strong.StrongVacuum::StrongVacuumDef",
  "declaration_slug": "strong-vacuum-def",
  "kind": "structure",
  "name": "StrongVacuumDef",
  "module_name": "TauLib.BookIV.Strong.StrongVacuum",
  "module_url": "/verify/taulib/docs/book-iv-strong-strong-vacuum/",
  "source_line_start": 264,
  "source_line_end": 273,
  "registry_ids": [
    "IV.D150"
  ],
  "related_registry_items": [
    {
      "id": "IV.D150",
      "title": "Strong vacuum",
      "url": "/registry/object/IV.D150/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/StrongVacuum.lean#L264-L273",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/StrongVacuum.lean#L264-L273",
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
- Source path: [`TauLib/BookIV/Strong/StrongVacuum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/StrongVacuum.lean#L264-L273)
- Source range: L264-L273
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D150` — Strong vacuum

## Immediate Comment / Docstring

```lean
/-- [IV.D150] The strong vacuum Gamma_s^*: omega-limit (projective limit)
    of finite-stage vacua over n >= 3, in pro-objects of H_partial. -/
```

## Source Excerpt

```lean
structure StrongVacuumDef where
  /-- Construction: projective limit. -/
  construction : String := "varprojlim_{n>=3} Gamma_s^*[n]"
  /-- Category: pro-objects of boundary holonomy algebra. -/
  category : String := "pro-H_partial"
  /-- Activation depth. -/
  activation_depth : Nat := 3
  /-- Well-defined by truncation coherence. -/
  well_defined : Bool := true
  deriving Repr
```
