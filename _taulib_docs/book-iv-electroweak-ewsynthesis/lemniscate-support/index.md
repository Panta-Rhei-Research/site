---
{
  "projection_kind": "taulib_declaration",
  "title": "LemniscateSupport",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-ewsynthesis/lemniscate-support/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.EWSynthesis`.",
  "declaration_id": "TauLib.BookIV.Electroweak.EWSynthesis::LemniscateSupport",
  "declaration_slug": "lemniscate-support",
  "kind": "structure",
  "name": "LemniscateSupport",
  "module_name": "TauLib.BookIV.Electroweak.EWSynthesis",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-ewsynthesis/",
  "source_line_start": 279,
  "source_line_end": 286,
  "registry_ids": [
    "IV.P175"
  ],
  "related_registry_items": [
    {
      "id": "IV.P175",
      "title": "Three-Fold Structure of~mathbbL",
      "url": "/registry/object/IV.P175/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/EWSynthesis.lean#L279-L286",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.EWSynthesis",
        "url": "/verify/taulib/docs/book-iv-electroweak-ewsynthesis/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/EWSynthesis.lean#L279-L286",
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

- Module: [TauLib.BookIV.Electroweak.EWSynthesis](/verify/taulib/docs/book-iv-electroweak-ewsynthesis/)
- Source path: [`TauLib/BookIV/Electroweak/EWSynthesis.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/EWSynthesis.lean#L279-L286)
- Source range: L279-L286
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P175` — Three-Fold Structure of~mathbbL

## Immediate Comment / Docstring

```lean
/-- [IV.P175] The three structural supports of the lemniscate
    L = S¹ ∨ S¹ in the EW context:
    1. B-lobe (EM sector): photon propagation, α determination
    2. C-lobe (Strong sector): confinement, mass gap
    3. Crossing point (ω-sector): Higgs mechanism, mass assignment

    Each support corresponds to a distinct physical mechanism. -/
```

## Source Excerpt

```lean
structure LemniscateSupport where
  /-- Support label. -/
  label : String
  /-- Associated sector. -/
  sector : Sector
  /-- Physical mechanism. -/
  mechanism : String
  deriving Repr
```
