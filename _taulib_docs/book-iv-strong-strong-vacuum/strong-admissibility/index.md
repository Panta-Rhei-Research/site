---
{
  "projection_kind": "taulib_declaration",
  "title": "StrongAdmissibility",
  "permalink": "/verify/taulib/docs/book-iv-strong-strong-vacuum/strong-admissibility/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Strong.StrongVacuum`.",
  "declaration_id": "TauLib.BookIV.Strong.StrongVacuum::StrongAdmissibility",
  "declaration_slug": "strong-admissibility",
  "kind": "structure",
  "name": "StrongAdmissibility",
  "module_name": "TauLib.BookIV.Strong.StrongVacuum",
  "module_url": "/verify/taulib/docs/book-iv-strong-strong-vacuum/",
  "source_line_start": 208,
  "source_line_end": 215,
  "registry_ids": [
    "IV.D148"
  ],
  "related_registry_items": [
    {
      "id": "IV.D148",
      "title": "Strong admissibility",
      "url": "/registry/object/IV.D148/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/StrongVacuum.lean#L208-L215",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/StrongVacuum.lean#L208-L215",
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
- Source path: [`TauLib/BookIV/Strong/StrongVacuum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/StrongVacuum.lean#L208-L215)
- Source range: L208-L215
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D148` — Strong admissibility

## Immediate Comment / Docstring

```lean
/-- [IV.D148] Strong admissibility: f in S_n is strongly admissible if
    (SA-i) preserves eta-sector chi_minus decomposition,
    (SA-ii) respects gap-class loops,
    (SA-iii) is boundary-coherent with the refinement tower. -/
```

## Source Excerpt

```lean
structure StrongAdmissibility where
  /-- (SA-i) Preserves chi_minus decomposition. -/
  preserves_chi_minus : Bool := true
  /-- (SA-ii) Respects gap-class loops. -/
  respects_gap_class : Bool := true
  /-- (SA-iii) Boundary-coherent with refinement. -/
  boundary_coherent : Bool := true
  deriving Repr
```
