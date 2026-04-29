---
{
  "projection_kind": "taulib_declaration",
  "title": "PracticalRegister",
  "permalink": "/verify/taulib/docs/book-vii-meta-registers/practical-register/",
  "summary_short": "`structure` declaration in `TauLib.BookVII.Meta.Registers`.",
  "declaration_id": "TauLib.BookVII.Meta.Registers::PracticalRegister",
  "declaration_slug": "practical-register",
  "kind": "structure",
  "name": "PracticalRegister",
  "module_name": "TauLib.BookVII.Meta.Registers",
  "module_url": "/verify/taulib/docs/book-vii-meta-registers/",
  "source_line_start": 75,
  "source_line_end": 82,
  "registry_ids": [
    "VII.D02"
  ],
  "related_registry_items": [
    {
      "id": "VII.D02",
      "title": "Practical Register",
      "url": "/registry/object/VII.D02/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L75-L82",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L75-L82",
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
- Source path: [`TauLib/BookVII/Meta/Registers.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L75-L82)
- Source range: L75-L82
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VII.D02` — Practical Register

## Immediate Comment / Docstring

```lean
/-- [VII.D02] Practical Register: functor Reg_P : K_τ → Norm.
    Coherence criterion: normative consistency (no contradictory obligations). -/
```

## Source Excerpt

```lean
structure PracticalRegister where
  register_type : RegisterType
  type_eq : register_type = .practical
  /-- Action-guiding: yields imperatives. -/
  action_guiding : Bool := true
  /-- Universalizable: passes sheaf-gluing condition. -/
  universalizable : Bool := true
  deriving Repr
```
