---
{
  "projection_kind": "taulib_declaration",
  "title": "TTM",
  "permalink": "/verify/taulib/docs/book-iii-spectrum-ttm/ttm/",
  "summary_short": "`structure` declaration in `TauLib.BookIII.Spectrum.TTM`.",
  "declaration_id": "TauLib.BookIII.Spectrum.TTM::TTM",
  "declaration_slug": "ttm",
  "kind": "structure",
  "name": "TTM",
  "module_name": "TauLib.BookIII.Spectrum.TTM",
  "module_url": "/verify/taulib/docs/book-iii-spectrum-ttm/",
  "source_line_start": 117,
  "source_line_end": 128,
  "registry_ids": [
    "I.D69"
  ],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectrum/TTM.lean#L117-L128",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Spectrum.TTM",
        "url": "/verify/taulib/docs/book-iii-spectrum-ttm/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectrum/TTM.lean#L117-L128",
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

- Module: [TauLib.BookIII.Spectrum.TTM](/verify/taulib/docs/book-iii-spectrum-ttm/)
- Source path: [`TauLib/BookIII/Spectrum/TTM.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectrum/TTM.lean#L117-L128)
- Source range: L117-L128
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [I.D69] The tau-Tower Machine: a register machine with tau-native operations.
    Bounded multiplicity (m registers + b_0 ports), unbounded magnitude. -/
```

## Source Excerpt

```lean
structure TTM where
  /-- Number of registers (m >= 1) -/
  num_registers : Nat
  /-- Number of ports (b_0 >= 0) -/
  num_ports : Nat
  /-- Transition rules -/
  rules : List TTMRule
  /-- Initial control state -/
  init_state : TauIdx
  /-- Accepting (halting) states -/
  accept_states : List TauIdx
  deriving Repr
```
