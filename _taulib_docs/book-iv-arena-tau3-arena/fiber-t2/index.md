---
{
  "projection_kind": "taulib_declaration",
  "title": "FiberT2",
  "permalink": "/verify/taulib/docs/book-iv-arena-tau3-arena/fiber-t2/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Arena.Tau3Arena`.",
  "declaration_id": "TauLib.BookIV.Arena.Tau3Arena::FiberT2",
  "declaration_slug": "fiber-t2",
  "kind": "structure",
  "name": "FiberT2",
  "module_name": "TauLib.BookIV.Arena.Tau3Arena",
  "module_url": "/verify/taulib/docs/book-iv-arena-tau3-arena/",
  "source_line_start": 70,
  "source_line_end": 83,
  "registry_ids": [
    "IV.D253"
  ],
  "related_registry_items": [
    {
      "id": "IV.D253",
      "title": "Fiber T^2 --- physical reading",
      "url": "/registry/object/IV.D253/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/Tau3Arena.lean#L70-L83",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Arena.Tau3Arena",
        "url": "/verify/taulib/docs/book-iv-arena-tau3-arena/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/Tau3Arena.lean#L70-L83",
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

- Module: [TauLib.BookIV.Arena.Tau3Arena](/verify/taulib/docs/book-iv-arena-tau3-arena/)
- Source path: [`TauLib/BookIV/Arena/Tau3Arena.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/Tau3Arena.lean#L70-L83)
- Source range: L70-L83
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D253` — Fiber T^2 --- physical reading

## Immediate Comment / Docstring

```lean
/-- [IV.D253] Fiber T² = ⟨γ, η, ω⟩: the spatial fiber torus carrying
    EM (B-sector, γ), strong (C-sector, η), and Higgs (ω-sector).
    Physically: 3 spatial dimensions. -/
```

## Source Excerpt

```lean
structure FiberT2 where
  /-- Fiber generators (exactly 3). -/
  gen_count : Nat
  gen_count_eq : gen_count = 3
  /-- EM generator. -/
  em_gen : Generator
  em_is_gamma : em_gen = .gamma
  /-- Strong generator. -/
  strong_gen : Generator
  strong_is_eta : strong_gen = .eta
  /-- Higgs generator (crossing). -/
  higgs_gen : Generator
  higgs_is_omega : higgs_gen = .omega
  deriving Repr
```
