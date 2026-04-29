---
{
  "projection_kind": "taulib_declaration",
  "title": "Tau1Base",
  "permalink": "/verify/taulib/docs/book-iv-arena-tau3-arena/tau1-base/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Arena.Tau3Arena`.",
  "declaration_id": "TauLib.BookIV.Arena.Tau3Arena::Tau1Base",
  "declaration_slug": "tau1-base",
  "kind": "structure",
  "name": "Tau1Base",
  "module_name": "TauLib.BookIV.Arena.Tau3Arena",
  "module_url": "/verify/taulib/docs/book-iv-arena-tau3-arena/",
  "source_line_start": 41,
  "source_line_end": 52,
  "registry_ids": [
    "IV.D252"
  ],
  "related_registry_items": [
    {
      "id": "IV.D252",
      "title": "Base tau^1 --- physical reading",
      "url": "/registry/object/IV.D252/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/Tau3Arena.lean#L41-L52",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/Tau3Arena.lean#L41-L52",
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
- Source path: [`TauLib/BookIV/Arena/Tau3Arena.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/Tau3Arena.lean#L41-L52)
- Source range: L41-L52
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D252` — Base tau^1 --- physical reading

## Immediate Comment / Docstring

```lean
/-- [IV.D252] Base τ¹ = ⟨α, π⟩: the temporal base circle carrying
    gravity (D-sector, α) and weak force (A-sector, π).
    Physically: 1 temporal dimension. -/
```

## Source Excerpt

```lean
structure Tau1Base where
  /-- Base generators (exactly 2). -/
  gen_count : Nat
  /-- Two base generators. -/
  gen_count_eq : gen_count = 2
  /-- Gravity generator. -/
  gravity_gen : Generator
  gravity_is_alpha : gravity_gen = .alpha
  /-- Weak generator. -/
  weak_gen : Generator
  weak_is_pi : weak_gen = .pi
  deriving Repr
```
