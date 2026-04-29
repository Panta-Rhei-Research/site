---
{
  "projection_kind": "taulib_declaration",
  "title": "TTMOp",
  "permalink": "/verify/taulib/docs/book-iii-spectrum-ttm/ttmop/",
  "summary_short": "`inductive` declaration in `TauLib.BookIII.Spectrum.TTM`.",
  "declaration_id": "TauLib.BookIII.Spectrum.TTM::TTMOp",
  "declaration_slug": "ttmop",
  "kind": "inductive",
  "name": "TTMOp",
  "module_name": "TauLib.BookIII.Spectrum.TTM",
  "module_url": "/verify/taulib/docs/book-iii-spectrum-ttm/",
  "source_line_start": 50,
  "source_line_end": 65,
  "registry_ids": [
    "I.D69"
  ],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectrum/TTM.lean#L50-L65",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectrum/TTM.lean#L50-L65",
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

- Module: [TauLib.BookIII.Spectrum.TTM](/verify/taulib/docs/book-iii-spectrum-ttm/)
- Source path: [`TauLib/BookIII/Spectrum/TTM.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectrum/TTM.lean#L50-L65)
- Source range: L50-L65
- Kind: `inductive`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [I.D69] TTM operations: the instruction set of the tau-Tower Machine.
    All operations are tau-native, built from the generators and ρ. -/
```

## Source Excerpt

```lean
inductive TTMOp where
  /-- r_i := rho(r_j) — successor via the progression operator -/
  | rho : Nat → Nat → TTMOp
  /-- r_i := sigma(r_j) — predecessor (truncated at 0) -/
  | sigma : Nat → Nat → TTMOp
  /-- r_i := r_j * r_k — multiplication -/
  | mul : Nat → Nat → Nat → TTMOp
  /-- r_i := r_j wedge r_k — minimum (lattice meet) -/
  | wedge : Nat → Nat → Nat → TTMOp
  /-- r_i := read(p_j) — read from port j into register i -/
  | readPort : Nat → Nat → TTMOp
  /-- write(p_j, r_i) — write register i to port j -/
  | writePort : Nat → Nat → TTMOp
  /-- no operation -/
  | noop : TTMOp
  deriving DecidableEq, Repr
```
