---
{
  "projection_kind": "taulib_declaration",
  "title": "ReadoutFunctor",
  "permalink": "/verify/taulib/docs/book-vii-meta-registers/readout-functor/",
  "summary_short": "`structure` declaration in `TauLib.BookVII.Meta.Registers`.",
  "declaration_id": "TauLib.BookVII.Meta.Registers::ReadoutFunctor",
  "declaration_slug": "readout-functor",
  "kind": "structure",
  "name": "ReadoutFunctor",
  "module_name": "TauLib.BookVII.Meta.Registers",
  "module_url": "/verify/taulib/docs/book-vii-meta-registers/",
  "source_line_start": 511,
  "source_line_end": 520,
  "registry_ids": [
    "VII.D22"
  ],
  "related_registry_items": [
    {
      "id": "VII.D22",
      "title": "Readout Functor",
      "url": "/registry/object/VII.D22/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L511-L520",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L511-L520",
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
- Source path: [`TauLib/BookVII/Meta/Registers.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L511-L520)
- Source range: L511-L520
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VII.D22` — Readout Functor

## Immediate Comment / Docstring

```lean
/-- [VII.D22] Readout Functor (ch15). Generic readout functor
    Reg_X : K_τ → Cod_X mapping kernel objects to register-specific
    codomain. Each register (E, P, D, C) has its own readout. -/
```

## Source Excerpt

```lean
structure ReadoutFunctor where
  /-- Well-defined on kernel objects. -/
  well_defined : Bool := true
  /-- Preserves structural morphisms. -/
  functorial : Bool := true
  /-- Codomain is register-specific. -/
  typed_codomain : Bool := true
  /-- Readout count: 4 readout functors. -/
  readout_count : Nat := 4
  deriving Repr
```
