---
{
  "projection_kind": "taulib_declaration",
  "title": "SpontaneousMagnetization",
  "permalink": "/verify/taulib/docs/book-iv-many-body-magnetism/spontaneous-magnetization/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.ManyBody.Magnetism`.",
  "declaration_id": "TauLib.BookIV.ManyBody.Magnetism::SpontaneousMagnetization",
  "declaration_slug": "spontaneous-magnetization",
  "kind": "structure",
  "name": "SpontaneousMagnetization",
  "module_name": "TauLib.BookIV.ManyBody.Magnetism",
  "module_url": "/verify/taulib/docs/book-iv-many-body-magnetism/",
  "source_line_start": 97,
  "source_line_end": 108,
  "registry_ids": [
    "IV.P226"
  ],
  "related_registry_items": [
    {
      "id": "IV.P226",
      "title": "Spontaneous Magnetization on T²",
      "url": "/registry/object/IV.P226/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/Magnetism.lean#L97-L108",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.ManyBody.Magnetism",
        "url": "/verify/taulib/docs/book-iv-many-body-magnetism/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/Magnetism.lean#L97-L108",
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

- Module: [TauLib.BookIV.ManyBody.Magnetism](/verify/taulib/docs/book-iv-many-body-magnetism/)
- Source path: [`TauLib/BookIV/ManyBody/Magnetism.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/Magnetism.lean#L97-L108)
- Source range: L97-L108
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P226` — Spontaneous Magnetization on T²

## Immediate Comment / Docstring

```lean
/-- [IV.P226] Spontaneous magnetization on T²:
    - Above T_C: ⟨M⟩ = 0 (paramagnetic)
    - Below T_C: ⟨|M|⟩ > 0 (ferromagnetic, Z₂ broken)
    - T_C determined by sinh(2J/k_BT_C) = 1 (Kramers-Wannier duality) -/
```

## Source Excerpt

```lean
structure SpontaneousMagnetization where
  /-- Phase transition exists. -/
  phase_transition : Bool := true
  /-- Above T_C: disordered. -/
  above_tc_disordered : Bool := true
  /-- Below T_C: Z₂ broken. -/
  below_tc_broken : Bool := true
  /-- T_C from Kramers-Wannier self-duality. -/
  tc_from_duality : Bool := true
  /-- Onsager solution applies on T². -/
  onsager_applies : Bool := true
  deriving Repr
```
