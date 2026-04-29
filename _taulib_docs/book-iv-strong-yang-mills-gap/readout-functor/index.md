---
{
  "projection_kind": "taulib_declaration",
  "title": "ReadoutFunctor",
  "permalink": "/verify/taulib/docs/book-iv-strong-yang-mills-gap/readout-functor/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Strong.YangMillsGap`.",
  "declaration_id": "TauLib.BookIV.Strong.YangMillsGap::ReadoutFunctor",
  "declaration_slug": "readout-functor",
  "kind": "structure",
  "name": "ReadoutFunctor",
  "module_name": "TauLib.BookIV.Strong.YangMillsGap",
  "module_url": "/verify/taulib/docs/book-iv-strong-yang-mills-gap/",
  "source_line_start": 339,
  "source_line_end": 350,
  "registry_ids": [
    "IV.D178"
  ],
  "related_registry_items": [
    {
      "id": "IV.D178",
      "title": "Readout functor (conjectural)",
      "url": "/registry/object/IV.D178/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/YangMillsGap.lean#L339-L350",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Strong.YangMillsGap",
        "url": "/verify/taulib/docs/book-iv-strong-yang-mills-gap/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/YangMillsGap.lean#L339-L350",
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

- Module: [TauLib.BookIV.Strong.YangMillsGap](/verify/taulib/docs/book-iv-strong-yang-mills-gap/)
- Source path: [`TauLib/BookIV/Strong/YangMillsGap.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/YangMillsGap.lean#L339-L350)
- Source range: L339-L350
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D178` — Readout functor (conjectural)

## Immediate Comment / Docstring

```lean
/-- [IV.D178] Readout functor R: Spec_tau(C) -> Spec_YM(SU(3))
    from the tau-spectrum of the C-sector to the physical spectrum
    of SU(3) Yang-Mills on R^4. Conjectural: bridges tau-internal
    mass gap to the Millennium Problem's R^4 formulation. -/
```

## Source Excerpt

```lean
structure ReadoutFunctor where
  /-- Source: tau C-sector spectrum. -/
  source : String := "Spec_tau(C)"
  /-- Target: SU(3) Yang-Mills spectrum on R^4. -/
  target : String := "Spec_YM(SU(3)) on R^4"
  /-- Scope: conjectural. -/
  scope : String := "conjectural"
  /-- Must preserve gap positivity. -/
  gap_preserving : Bool := true
  /-- Must preserve spectral ordering. -/
  ordering_preserving : Bool := true
  deriving Repr
```
