---
{
  "projection_kind": "taulib_declaration",
  "title": "OnticEntity",
  "permalink": "/verify/taulib/docs/book-iv-particles-spectrum-complete/ontic-entity/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.SpectrumComplete`.",
  "declaration_id": "TauLib.BookIV.Particles.SpectrumComplete::OnticEntity",
  "declaration_slug": "ontic-entity",
  "kind": "structure",
  "name": "OnticEntity",
  "module_name": "TauLib.BookIV.Particles.SpectrumComplete",
  "module_url": "/verify/taulib/docs/book-iv-particles-spectrum-complete/",
  "source_line_start": 60,
  "source_line_end": 69,
  "registry_ids": [
    "IV.D209"
  ],
  "related_registry_items": [
    {
      "id": "IV.D209",
      "title": "Ontic entity",
      "url": "/registry/object/IV.D209/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/SpectrumComplete.lean#L60-L69",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/SpectrumComplete.lean#L60-L69",
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
- Source path: [`TauLib/BookIV/Particles/SpectrumComplete.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/SpectrumComplete.lean#L60-L69)
- Source range: L60-L69
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D209` — Ontic entity

## Immediate Comment / Docstring

```lean
/-- [IV.D209] An ontic entity in Category τ. -/
```

## Source Excerpt

```lean
structure OnticEntity where
  /-- Entity name. -/
  name : String
  /-- Primary ontic criterion. -/
  criterion : OnticCriterion
  /-- Sector(s). -/
  sectors : List Sector
  /-- Is stable? -/
  stable : Bool
  deriving Repr
```
