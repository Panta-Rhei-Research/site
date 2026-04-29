---
{
  "projection_kind": "taulib_declaration",
  "title": "GapQuantumDef",
  "permalink": "/verify/taulib/docs/book-iv-strong-yang-mills-gap/gap-quantum-def/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Strong.YangMillsGap`.",
  "declaration_id": "TauLib.BookIV.Strong.YangMillsGap::GapQuantumDef",
  "declaration_slug": "gap-quantum-def",
  "kind": "structure",
  "name": "GapQuantumDef",
  "module_name": "TauLib.BookIV.Strong.YangMillsGap",
  "module_url": "/verify/taulib/docs/book-iv-strong-yang-mills-gap/",
  "source_line_start": 235,
  "source_line_end": 242,
  "registry_ids": [
    "IV.D177"
  ],
  "related_registry_items": [
    {
      "id": "IV.D177",
      "title": "Gap quantum",
      "url": "/registry/object/IV.D177/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/YangMillsGap.lean#L235-L242",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/YangMillsGap.lean#L235-L242",
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
- Source path: [`TauLib/BookIV/Strong/YangMillsGap.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/YangMillsGap.lean#L235-L242)
- Source range: L235-L242
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D177` — Gap quantum

## Immediate Comment / Docstring

```lean
/-- [IV.D177] g[omega] := varprojlim_{n>=3} g_n, the profinite
    gap quantum. Its spectral weight lambda_omega^s(g[omega]) :=
    lim delta_n^s is the mass gap of the strong sector. -/
```

## Source Excerpt

```lean
structure GapQuantumDef where
  /-- Projective limit of finite-stage gap modes. -/
  construction : String := "varprojlim_{n>=3} g_n"
  /-- Spectral weight is the omega-limit of gaps. -/
  spectral_weight : String := "lim delta_n^s"
  /-- Represents the lightest glueball in the C-sector. -/
  physical_interpretation : String := "lightest glueball"
  deriving Repr
```
