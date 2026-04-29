---
{
  "projection_kind": "taulib_declaration",
  "title": "CommitmentRegister",
  "permalink": "/verify/taulib/docs/book-vii-meta-registers/commitment-register/",
  "summary_short": "`structure` declaration in `TauLib.BookVII.Meta.Registers`.",
  "declaration_id": "TauLib.BookVII.Meta.Registers::CommitmentRegister",
  "declaration_slug": "commitment-register",
  "kind": "structure",
  "name": "CommitmentRegister",
  "module_name": "TauLib.BookVII.Meta.Registers",
  "module_url": "/verify/taulib/docs/book-vii-meta-registers/",
  "source_line_start": 97,
  "source_line_end": 104,
  "registry_ids": [
    "VII.D04"
  ],
  "related_registry_items": [
    {
      "id": "VII.D04",
      "title": "Commitment Register",
      "url": "/registry/object/VII.D04/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L97-L104",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVII.Meta.Registers",
        "url": "/verify/taulib/docs/book-vii-meta-registers/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L97-L104",
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

- Module: [TauLib.BookVII.Meta.Registers](/verify/taulib/docs/book-vii-meta-registers/)
- Source path: [`TauLib/BookVII/Meta/Registers.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L97-L104)
- Source range: L97-L104
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VII.D04` — Commitment Register

## Immediate Comment / Docstring

```lean
/-- [VII.D04] Commitment Register: functor Reg_C : K_τ → Stance.
    Coherence criterion: stance-stability (persistence under reflective scrutiny). -/
```

## Source Excerpt

```lean
structure CommitmentRegister where
  register_type : RegisterType
  type_eq : register_type = .commitment
  /-- Performative: content constituted by stance-taking. -/
  performative : Bool := true
  /-- Reflectively stable: persists under scrutiny. -/
  reflectively_stable : Bool := true
  deriving Repr
```
