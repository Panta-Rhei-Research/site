---
{
  "projection_kind": "taulib_declaration",
  "title": "OnticCriterion",
  "permalink": "/verify/taulib/docs/book-iv-particles-spectrum-complete/ontic-criterion/",
  "summary_short": "`inductive` declaration in `TauLib.BookIV.Particles.SpectrumComplete`.",
  "declaration_id": "TauLib.BookIV.Particles.SpectrumComplete::OnticCriterion",
  "declaration_slug": "ontic-criterion",
  "kind": "inductive",
  "name": "OnticCriterion",
  "module_name": "TauLib.BookIV.Particles.SpectrumComplete",
  "module_url": "/verify/taulib/docs/book-iv-particles-spectrum-complete/",
  "source_line_start": 48,
  "source_line_end": 57,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/SpectrumComplete.lean#L48-L57",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/SpectrumComplete.lean#L48-L57",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "inductive",
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
- Source path: [`TauLib/BookIV/Particles/SpectrumComplete.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/SpectrumComplete.lean#L48-L57)
- Source range: L48-L57
- Kind: `inductive`
- Formal status hint: `defined`

## Registry Links

- `IV.D209` — Ontic entity

## Immediate Comment / Docstring

```lean
/-- [IV.D209] An entity is ontic in Category τ if it satisfies at least
    one of four criteria. -/
```

## Source Excerpt

```lean
inductive OnticCriterion where
  /-- Well-defined mode on fiber T² (particle). -/
  | fiberMode
  /-- Well-defined mode on base τ¹ (temporal/gravitational). -/
  | baseMode
  /-- Well-defined crossing mode at ω = γ ∩ η (Higgs-type). -/
  | crossingMode
  /-- Finite composite of ontic modes (hadrons, nuclei, atoms). -/
  | finiteComposite
  deriving Repr, DecidableEq, BEq
```
