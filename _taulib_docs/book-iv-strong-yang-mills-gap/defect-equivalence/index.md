---
{
  "projection_kind": "taulib_declaration",
  "title": "DefectEquivalence",
  "permalink": "/verify/taulib/docs/book-iv-strong-yang-mills-gap/defect-equivalence/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Strong.YangMillsGap`.",
  "declaration_id": "TauLib.BookIV.Strong.YangMillsGap::DefectEquivalence",
  "declaration_slug": "defect-equivalence",
  "kind": "structure",
  "name": "DefectEquivalence",
  "module_name": "TauLib.BookIV.Strong.YangMillsGap",
  "module_url": "/verify/taulib/docs/book-iv-strong-yang-mills-gap/",
  "source_line_start": 119,
  "source_line_end": 124,
  "registry_ids": [
    "IV.P103"
  ],
  "related_registry_items": [
    {
      "id": "IV.P103",
      "title": "Equivalence of defect formulations",
      "url": "/registry/object/IV.P103/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/YangMillsGap.lean#L119-L124",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/YangMillsGap.lean#L119-L124",
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
- Source path: [`TauLib/BookIV/Strong/YangMillsGap.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/YangMillsGap.lean#L119-L124)
- Source range: L119-L124
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P103` — Equivalence of defect formulations

## Immediate Comment / Docstring

```lean
/-- [IV.P103] The two defect formulations determine the same vacuum:
    argmin V_n^s = Gamma_s^*[n] = argmin Delta_n^s. -/
```

## Source Excerpt

```lean
structure DefectEquivalence where
  /-- Same vacuum from both formulations. -/
  same_vacuum : Bool := true
  /-- Gap loops decompose into plaquettes. -/
  loop_plaquette_decomposition : Bool := true
  deriving Repr
```
