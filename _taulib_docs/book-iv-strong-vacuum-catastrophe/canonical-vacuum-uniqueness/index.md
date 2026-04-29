---
{
  "projection_kind": "taulib_declaration",
  "title": "CanonicalVacuumUniqueness",
  "permalink": "/verify/taulib/docs/book-iv-strong-vacuum-catastrophe/canonical-vacuum-uniqueness/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Strong.VacuumCatastrophe`.",
  "declaration_id": "TauLib.BookIV.Strong.VacuumCatastrophe::CanonicalVacuumUniqueness",
  "declaration_slug": "canonical-vacuum-uniqueness",
  "kind": "structure",
  "name": "CanonicalVacuumUniqueness",
  "module_name": "TauLib.BookIV.Strong.VacuumCatastrophe",
  "module_url": "/verify/taulib/docs/book-iv-strong-vacuum-catastrophe/",
  "source_line_start": 105,
  "source_line_end": 112,
  "registry_ids": [
    "IV.P120"
  ],
  "related_registry_items": [
    {
      "id": "IV.P120",
      "title": "Canonical vacuum uniqueness",
      "url": "/registry/object/IV.P120/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/VacuumCatastrophe.lean#L105-L112",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Strong.VacuumCatastrophe",
        "url": "/verify/taulib/docs/book-iv-strong-vacuum-catastrophe/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/VacuumCatastrophe.lean#L105-L112",
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

- Module: [TauLib.BookIV.Strong.VacuumCatastrophe](/verify/taulib/docs/book-iv-strong-vacuum-catastrophe/)
- Source path: [`TauLib/BookIV/Strong/VacuumCatastrophe.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/VacuumCatastrophe.lean#L105-L112)
- Source range: L105-L112
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P120` — Canonical vacuum uniqueness

## Immediate Comment / Docstring

```lean
/-- [IV.P120] Each sector vacuum is the UNIQUE minimizer of its defect
    functional, not a representative of an equivalence class:
    - Omega^*_EM (B-sector)
    - Omega^*_wk (A-sector)
    - Gamma^*_s  (C-sector, strong vacuum)
    - nabla^*_GR (D-sector, gravitational vacuum)

    Uniqueness follows from NFMin tie-breaking over finite sets. -/
```

## Source Excerpt

```lean
structure CanonicalVacuumUniqueness where
  /-- Number of sector vacua. -/
  num_vacua : Nat := 4
  /-- Each is unique (not up to equivalence). -/
  each_unique : Bool := true
  /-- Mechanism: NFMin over finite admissible sets. -/
  mechanism : String := "NFMin over finite Adm_S[n]"
  deriving Repr
```
