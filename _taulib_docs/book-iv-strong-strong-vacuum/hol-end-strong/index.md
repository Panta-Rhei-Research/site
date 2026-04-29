---
{
  "projection_kind": "taulib_declaration",
  "title": "HolEndStrong",
  "permalink": "/verify/taulib/docs/book-iv-strong-strong-vacuum/hol-end-strong/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Strong.StrongVacuum`.",
  "declaration_id": "TauLib.BookIV.Strong.StrongVacuum::HolEndStrong",
  "declaration_slug": "hol-end-strong",
  "kind": "structure",
  "name": "HolEndStrong",
  "module_name": "TauLib.BookIV.Strong.StrongVacuum",
  "module_url": "/verify/taulib/docs/book-iv-strong-strong-vacuum/",
  "source_line_start": 307,
  "source_line_end": 316,
  "registry_ids": [
    "IV.D151"
  ],
  "related_registry_items": [
    {
      "id": "IV.D151",
      "title": "\\mathrm{HolEnd_τ(s)",
      "url": "/registry/object/IV.D151/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/StrongVacuum.lean#L307-L316",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/StrongVacuum.lean#L307-L316",
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
- Source path: [`TauLib/BookIV/Strong/StrongVacuum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/StrongVacuum.lean#L307-L316)
- Source range: L307-L316
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D151` — \mathrm{HolEnd_τ(s)

## Immediate Comment / Docstring

```lean
/-- [IV.D151] HolEnd_tau(s)[n]: space of strong-admissible boundary
    endomorphisms satisfying vacuum preservation (H-i),
    holonomy compatibility (H-ii), boundary coherence (H-iii). -/
```

## Source Excerpt

```lean
structure HolEndStrong where
  /-- Stage n. -/
  stage : Nat
  /-- (H-i) Vacuum preservation. -/
  vacuum_preserving : Bool := true
  /-- (H-ii) Holonomy compatibility. -/
  holonomy_compatible : Bool := true
  /-- (H-iii) Boundary coherence. -/
  boundary_coherent : Bool := true
  deriving Repr
```
