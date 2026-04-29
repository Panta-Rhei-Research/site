---
{
  "projection_kind": "taulib_declaration",
  "title": "VacuumPlaquetteForm",
  "permalink": "/verify/taulib/docs/book-iv-strong-yang-mills-gap/vacuum-plaquette-form/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Strong.YangMillsGap`.",
  "declaration_id": "TauLib.BookIV.Strong.YangMillsGap::VacuumPlaquetteForm",
  "declaration_slug": "vacuum-plaquette-form",
  "kind": "structure",
  "name": "VacuumPlaquetteForm",
  "module_name": "TauLib.BookIV.Strong.YangMillsGap",
  "module_url": "/verify/taulib/docs/book-iv-strong-yang-mills-gap/",
  "source_line_start": 135,
  "source_line_end": 144,
  "registry_ids": [
    "IV.D173"
  ],
  "related_registry_items": [
    {
      "id": "IV.D173",
      "title": "Canonical strong vacuum, plaquette form",
      "url": "/registry/object/IV.D173/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/YangMillsGap.lean#L135-L144",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Strong.YangMillsGap",
        "url": "/verify/taulib/docs/book-iv-strong-yang-mills-gap/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/YangMillsGap.lean#L135-L144",
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

- Module: [TauLib.BookIV.Strong.YangMillsGap](/verify/taulib/docs/book-iv-strong-yang-mills-gap/)
- Source path: [`TauLib/BookIV/Strong/YangMillsGap.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/YangMillsGap.lean#L135-L144)
- Source range: L135-L144
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D173` — Canonical strong vacuum, plaquette form

## Immediate Comment / Docstring

```lean
/-- [IV.D173] Gamma_s^*[n] in plaquette form:
    argmin of V_n^s with NF code tie-breaking.
    Equivalent to the gap-loop definition from ch37. -/
```

## Source Excerpt

```lean
structure VacuumPlaquetteForm where
  /-- Stage n. -/
  stage : Nat
  /-- Argmin of plaquette defect. -/
  is_argmin : Bool := true
  /-- NF tie-breaking. -/
  nf_tiebreak : Bool := true
  /-- Equivalent to gap-loop vacuum. -/
  equivalent_to_loop_vacuum : Bool := true
  deriving Repr
```
