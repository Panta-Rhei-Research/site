---
{
  "projection_kind": "taulib_declaration",
  "title": "TailStabilization",
  "permalink": "/verify/taulib/docs/book-iv-strong-vacuum-catastrophe/tail-stabilization/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Strong.VacuumCatastrophe`.",
  "declaration_id": "TauLib.BookIV.Strong.VacuumCatastrophe::TailStabilization",
  "declaration_slug": "tail-stabilization",
  "kind": "structure",
  "name": "TailStabilization",
  "module_name": "TauLib.BookIV.Strong.VacuumCatastrophe",
  "module_url": "/verify/taulib/docs/book-iv-strong-vacuum-catastrophe/",
  "source_line_start": 224,
  "source_line_end": 235,
  "registry_ids": [
    "IV.T79"
  ],
  "related_registry_items": [
    {
      "id": "IV.T79",
      "title": "Tail stabilization of vacuum energy",
      "url": "/registry/object/IV.T79/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/VacuumCatastrophe.lean#L224-L235",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/VacuumCatastrophe.lean#L224-L235",
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
- Source path: [`TauLib/BookIV/Strong/VacuumCatastrophe.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/VacuumCatastrophe.lean#L224-L235)
- Source range: L224-L235
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.T79` — Tail stabilization of vacuum energy

## Immediate Comment / Docstring

```lean
/-- [IV.T79] Tail stabilization of vacuum energy: there exists a
    stabilization horizon N_s such that VacE_s[n+1] = VacE_s[n]
    for all n >= N_s.

    The omega-germ limit VacE_s[omega] = VacE_s[N_s] is a finite
    element of the boundary algebra, not a divergent limit.

    This is not fine-tuning: N_s is determined by the sector's
    activation depth and the rate of spectral tightening. -/
```

## Source Excerpt

```lean
structure TailStabilization where
  /-- Stabilization horizon exists. -/
  horizon_exists : Bool := true
  /-- Beyond horizon: vacuum energy is constant. -/
  constant_beyond : Bool := true
  /-- Omega-germ limit equals value at horizon. -/
  limit_equals_horizon : Bool := true
  /-- Not fine-tuning: horizon determined by structure. -/
  not_fine_tuning : Bool := true
  /-- Source: spectral tightening + finite mode count. -/
  source : String := "spectral tightening + finite earned mode count"
  deriving Repr
```
