---
{
  "projection_kind": "taulib_declaration",
  "title": "YMSectorCoupling",
  "permalink": "/verify/taulib/docs/book-iv-strong-yang-mills-gap/ymsector-coupling/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Strong.YangMillsGap`.",
  "declaration_id": "TauLib.BookIV.Strong.YangMillsGap::YMSectorCoupling",
  "declaration_slug": "ymsector-coupling",
  "kind": "structure",
  "name": "YMSectorCoupling",
  "module_name": "TauLib.BookIV.Strong.YangMillsGap",
  "module_url": "/verify/taulib/docs/book-iv-strong-yang-mills-gap/",
  "source_line_start": 202,
  "source_line_end": 209,
  "registry_ids": [
    "IV.D176"
  ],
  "related_registry_items": [
    {
      "id": "IV.D176",
      "title": "YM sector coupling",
      "url": "/registry/object/IV.D176/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/YangMillsGap.lean#L202-L209",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/YangMillsGap.lean#L202-L209",
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
- Source path: [`TauLib/BookIV/Strong/YangMillsGap.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/YangMillsGap.lean#L202-L209)
- Source range: L202-L209
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D176` — YM sector coupling

## Immediate Comment / Docstring

```lean
/-- [IV.D176] mu_YM(k): ratio of B-product to C-product of the
    split-complex zeta function at primorial depth k (III.D46).
    Measures bipolar asymmetry between the two lobe sectors. -/
```

## Source Excerpt

```lean
structure YMSectorCoupling where
  /-- Primorial depth k. -/
  depth : Nat
  /-- Ratio of B-product to C-product. -/
  is_ratio : Bool := true
  /-- From split-complex zeta (III.D46). -/
  source : String := "split-complex zeta function III.D46"
  deriving Repr
```
