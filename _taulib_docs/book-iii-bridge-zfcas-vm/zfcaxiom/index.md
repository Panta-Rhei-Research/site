---
{
  "projection_kind": "taulib_declaration",
  "title": "ZFCAxiom",
  "permalink": "/verify/taulib/docs/book-iii-bridge-zfcas-vm/zfcaxiom/",
  "summary_short": "`inductive` declaration in `TauLib.BookIII.Bridge.ZFCasVM`.",
  "declaration_id": "TauLib.BookIII.Bridge.ZFCasVM::ZFCAxiom",
  "declaration_slug": "zfcaxiom",
  "kind": "inductive",
  "name": "ZFCAxiom",
  "module_name": "TauLib.BookIII.Bridge.ZFCasVM",
  "module_url": "/verify/taulib/docs/book-iii-bridge-zfcas-vm/",
  "source_line_start": 45,
  "source_line_end": 55,
  "registry_ids": [
    "III.D67"
  ],
  "related_registry_items": [
    {
      "id": "III.D67",
      "title": "ZFC as E₂ VM",
      "url": "/registry/object/III.D67/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/ZFCasVM.lean#L45-L55",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Bridge.ZFCasVM",
        "url": "/verify/taulib/docs/book-iii-bridge-zfcas-vm/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/ZFCasVM.lean#L45-L55",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "inductive",
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

- Module: [TauLib.BookIII.Bridge.ZFCasVM](/verify/taulib/docs/book-iii-bridge-zfcas-vm/)
- Source path: [`TauLib/BookIII/Bridge/ZFCasVM.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/ZFCasVM.lean#L45-L55)
- Source range: L45-L55
- Kind: `inductive`
- Formal status hint: `defined`

## Registry Links

- `III.D67` — ZFC as E₂ VM

## Immediate Comment / Docstring

```lean
/-- [III.D67] The ZFC axioms modeled as operations on tau-addresses.
    Each axiom corresponds to a modular operation at primorial level k. -/
```

## Source Excerpt

```lean
inductive ZFCAxiom where
  | extensionality : ZFCAxiom    -- sets equal iff same elements
  | pairing : ZFCAxiom           -- {a, b} exists
  | union : ZFCAxiom             -- ∪S exists
  | powerset : ZFCAxiom          -- P(S) exists
  | infinity : ZFCAxiom          -- infinite set exists
  | separation : ZFCAxiom        -- {x in S | phi(x)} exists
  | replacement : ZFCAxiom       -- image of S under F exists
  | foundation : ZFCAxiom        -- no infinite descending ∈-chain
  | choice : ZFCAxiom            -- choice function exists
  deriving Repr, DecidableEq, BEq
```
