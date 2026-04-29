---
{
  "projection_kind": "taulib_declaration",
  "title": "SynchronicityAsKernelInvariant",
  "permalink": "/verify/taulib/docs/book-vii-meta-registers/synchronicity-as-kernel-invariant/",
  "summary_short": "`structure` declaration in `TauLib.BookVII.Meta.Registers`.",
  "declaration_id": "TauLib.BookVII.Meta.Registers::SynchronicityAsKernelInvariant",
  "declaration_slug": "synchronicity-as-kernel-invariant",
  "kind": "structure",
  "name": "SynchronicityAsKernelInvariant",
  "module_name": "TauLib.BookVII.Meta.Registers",
  "module_url": "/verify/taulib/docs/book-vii-meta-registers/",
  "source_line_start": 478,
  "source_line_end": 485,
  "registry_ids": [
    "VII.D21"
  ],
  "related_registry_items": [
    {
      "id": "VII.D21",
      "title": "Synchronicity as Kernel Invariant",
      "url": "/registry/object/VII.D21/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L478-L485",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L478-L485",
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
- Source path: [`TauLib/BookVII/Meta/Registers.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L478-L485)
- Source range: L478-L485
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VII.D21` — Synchronicity as Kernel Invariant

## Immediate Comment / Docstring

```lean
/-- [VII.D21] Synchronicity as Kernel Invariant (ch14). **CONJECTURAL.**
    Cross-register correlation pattern: events aligned across Reg_E
    and Reg_C without causal mediation. Modelled as kernel invariant
    under the register projection. Conjectural because cross-register
    correlation involves Reg_C content beyond Reg_D. -/
```

## Source Excerpt

```lean
structure SynchronicityAsKernelInvariant where
  /-- Kernel-level invariant. -/
  kernel_invariant : Bool := true
  /-- Cross-register: correlates E and C. -/
  cross_register : Bool := true
  /-- Non-causal: no mediation pathway. -/
  non_causal : Bool := true
  deriving Repr
```
