---
{
  "projection_kind": "taulib_declaration",
  "title": "NonOnticEntity",
  "permalink": "/verify/taulib/docs/book-iv-particles-spectrum-complete/non-ontic-entity/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.SpectrumComplete`.",
  "declaration_id": "TauLib.BookIV.Particles.SpectrumComplete::NonOnticEntity",
  "declaration_slug": "non-ontic-entity",
  "kind": "structure",
  "name": "NonOnticEntity",
  "module_name": "TauLib.BookIV.Particles.SpectrumComplete",
  "module_url": "/verify/taulib/docs/book-iv-particles-spectrum-complete/",
  "source_line_start": 131,
  "source_line_end": 136,
  "registry_ids": [
    "IV.R151"
  ],
  "related_registry_items": [
    {
      "id": "IV.R151",
      "title": "Non-ontic entities list",
      "url": "/registry/object/IV.R151/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/SpectrumComplete.lean#L131-L136",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/SpectrumComplete.lean#L131-L136",
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
- Source path: [`TauLib/BookIV/Particles/SpectrumComplete.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/SpectrumComplete.lean#L131-L136)
- Source range: L131-L136
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.R151` — Non-ontic entities list

## Immediate Comment / Docstring

```lean
/-- [IV.R151] Non-ontic entities: computational devices useful in
    orthodox calculations but NOT representing τ³ objects. -/
```

## Source Excerpt

```lean
structure NonOnticEntity where
  /-- Entity name. -/
  name : String
  /-- Why non-ontic. -/
  reason : String
  deriving Repr
```
