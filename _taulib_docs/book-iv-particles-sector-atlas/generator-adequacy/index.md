---
{
  "projection_kind": "taulib_declaration",
  "title": "GeneratorAdequacy",
  "permalink": "/verify/taulib/docs/book-iv-particles-sector-atlas/generator-adequacy/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.SectorAtlas`.",
  "declaration_id": "TauLib.BookIV.Particles.SectorAtlas::GeneratorAdequacy",
  "declaration_slug": "generator-adequacy",
  "kind": "structure",
  "name": "GeneratorAdequacy",
  "module_name": "TauLib.BookIV.Particles.SectorAtlas",
  "module_url": "/verify/taulib/docs/book-iv-particles-sector-atlas/",
  "source_line_start": 163,
  "source_line_end": 172,
  "registry_ids": [
    "IV.T82"
  ],
  "related_registry_items": [
    {
      "id": "IV.T82",
      "title": "Generator adequacy and minimality",
      "url": "/registry/object/IV.T82/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/SectorAtlas.lean#L163-L172",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Particles.SectorAtlas",
        "url": "/verify/taulib/docs/book-iv-particles-sector-atlas/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/SectorAtlas.lean#L163-L172",
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

- Module: [TauLib.BookIV.Particles.SectorAtlas](/verify/taulib/docs/book-iv-particles-sector-atlas/)
- Source path: [`TauLib/BookIV/Particles/SectorAtlas.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/SectorAtlas.lean#L163-L172)
- Source range: L163-L172
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.T82` — Generator adequacy and minimality

## Immediate Comment / Docstring

```lean
/-- [IV.T82] The 9 canonical generators generate the entire boundary
    holonomy algebra H_∂[ω], and no proper subset suffices.
    Every polynomial expression in these 9 yields a physical observable.
    Adequacy: span = H_∂[ω]. Minimality: removal of any one breaks span. -/
```

## Source Excerpt

```lean
structure GeneratorAdequacy where
  /-- Total generators. -/
  total : Nat := 9
  /-- Adequate: they generate H_∂[ω]. -/
  adequate : Bool := true
  /-- Minimal: no proper subset suffices. -/
  minimal : Bool := true
  /-- Every polynomial is a physical observable. -/
  all_observable : Bool := true
  deriving Repr
```
