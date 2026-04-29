---
{
  "projection_kind": "taulib_declaration",
  "title": "OntologicalLine",
  "permalink": "/verify/taulib/docs/book-iv-particles-spectrum-complete/ontological-line/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.SpectrumComplete`.",
  "declaration_id": "TauLib.BookIV.Particles.SpectrumComplete::OntologicalLine",
  "declaration_slug": "ontological-line",
  "kind": "structure",
  "name": "OntologicalLine",
  "module_name": "TauLib.BookIV.Particles.SpectrumComplete",
  "module_url": "/verify/taulib/docs/book-iv-particles-spectrum-complete/",
  "source_line_start": 161,
  "source_line_end": 172,
  "registry_ids": [
    "IV.R152"
  ],
  "related_registry_items": [
    {
      "id": "IV.R152",
      "title": "Where the ontological line falls",
      "url": "/registry/object/IV.R152/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/SpectrumComplete.lean#L161-L172",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/SpectrumComplete.lean#L161-L172",
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
- Source path: [`TauLib/BookIV/Particles/SpectrumComplete.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/SpectrumComplete.lean#L161-L172)
- Source range: L161-L172
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.R152` — Where the ontological line falls

## Immediate Comment / Docstring

```lean
/-- [IV.R152] The ontic/non-ontic distinction is not philosophical
    preference but a mathematical consequence of the τ³ fibration.
    An entity is ontic iff it can be constructed as a mode, character,
    or finite composite on τ³ = τ¹ ×_f T². -/
```

## Source Excerpt

```lean
structure OntologicalLine where
  /-- Mathematical, not philosophical. -/
  mathematical : Bool := true
  /-- Criterion: constructible on τ³. -/
  criterion : String := "constructible as mode/character/composite on tau^3"
  /-- Resolves wave function reality. -/
  resolves_wf : Bool := true
  /-- Resolves virtual particle reality. -/
  resolves_virtual : Bool := true
  /-- Resolves spacetime reality. -/
  resolves_spacetime : Bool := true
  deriving Repr
```
