---
{
  "projection_kind": "taulib_declaration",
  "title": "DictionaryLimits",
  "permalink": "/verify/taulib/docs/book-iv-particles-spectrum-complete/dictionary-limits/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.SpectrumComplete`.",
  "declaration_id": "TauLib.BookIV.Particles.SpectrumComplete::DictionaryLimits",
  "declaration_slug": "dictionary-limits",
  "kind": "structure",
  "name": "DictionaryLimits",
  "module_name": "TauLib.BookIV.Particles.SpectrumComplete",
  "module_url": "/verify/taulib/docs/book-iv-particles-spectrum-complete/",
  "source_line_start": 188,
  "source_line_end": 195,
  "registry_ids": [
    "IV.R153"
  ],
  "related_registry_items": [
    {
      "id": "IV.R153",
      "title": "Dictionary limits",
      "url": "/registry/object/IV.R153/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/SpectrumComplete.lean#L188-L195",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Particles.SpectrumComplete",
        "url": "/verify/taulib/docs/book-iv-particles-spectrum-complete/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/SpectrumComplete.lean#L188-L195",
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

- Module: [TauLib.BookIV.Particles.SpectrumComplete](/verify/taulib/docs/book-iv-particles-spectrum-complete/)
- Source path: [`TauLib/BookIV/Particles/SpectrumComplete.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/SpectrumComplete.lean#L188-L195)
- Source range: L188-L195
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.R153` — Dictionary limits

## Immediate Comment / Docstring

```lean
/-- [IV.R153] The τ-to-SM translation dictionary covers sector decomposition,
    coupling ledger, QM infrastructure, and particle content but has limits:

    No SM counterpart for: H_∂[ω], breathing operator, defect functional.
    No τ counterpart for: virtual particles, path integral, RG flow, gravitons. -/
```

## Source Excerpt

```lean
structure DictionaryLimits where
  /-- Tau concepts without SM counterpart. -/
  tau_only : List String :=
    ["H_partial[omega]", "breathing operator", "defect functional"]
  /-- SM concepts without tau counterpart. -/
  sm_only : List String :=
    ["virtual particles", "path integral measure", "RG flow", "gravitons as particles"]
  deriving Repr
```
