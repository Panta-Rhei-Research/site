---
{
  "projection_kind": "taulib_declaration",
  "title": "StrongConfigSpace",
  "permalink": "/verify/taulib/docs/book-iv-strong-yang-mills-gap/strong-config-space/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Strong.YangMillsGap`.",
  "declaration_id": "TauLib.BookIV.Strong.YangMillsGap::StrongConfigSpace",
  "declaration_slug": "strong-config-space",
  "kind": "structure",
  "name": "StrongConfigSpace",
  "module_name": "TauLib.BookIV.Strong.YangMillsGap",
  "module_url": "/verify/taulib/docs/book-iv-strong-yang-mills-gap/",
  "source_line_start": 57,
  "source_line_end": 66,
  "registry_ids": [
    "IV.D169"
  ],
  "related_registry_items": [
    {
      "id": "IV.D169",
      "title": "Strong configuration space",
      "url": "/registry/object/IV.D169/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/YangMillsGap.lean#L57-L66",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/YangMillsGap.lean#L57-L66",
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
- Source path: [`TauLib/BookIV/Strong/YangMillsGap.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/YangMillsGap.lean#L57-L66)
- Source range: L57-L66
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D169` — Strong configuration space

## Immediate Comment / Docstring

```lean
/-- [IV.D169] Strong configuration space C_s[n]:
    quotient of strongly admissible endomorphisms at stage n
    by the equivalence relation induced by the strong vacuum. -/
```

## Source Excerpt

```lean
structure StrongConfigSpace where
  /-- Stage n. -/
  stage : Nat
  /-- Quotient by vacuum equivalence. -/
  is_quotient : Bool := true
  /-- Finite at each stage. -/
  finite : Bool := true
  /-- NF-enumerable. -/
  nf_enumerable : Bool := true
  deriving Repr
```
