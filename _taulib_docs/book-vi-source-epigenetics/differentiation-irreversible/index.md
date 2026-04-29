---
{
  "projection_kind": "taulib_declaration",
  "title": "DifferentiationIrreversible",
  "permalink": "/verify/taulib/docs/book-vi-source-epigenetics/differentiation-irreversible/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Source.Epigenetics`.",
  "declaration_id": "TauLib.BookVI.Source.Epigenetics::DifferentiationIrreversible",
  "declaration_slug": "differentiation-irreversible",
  "kind": "structure",
  "name": "DifferentiationIrreversible",
  "module_name": "TauLib.BookVI.Source.Epigenetics",
  "module_url": "/verify/taulib/docs/book-vi-source-epigenetics/",
  "source_line_start": 247,
  "source_line_end": 256,
  "registry_ids": [
    "VI.T47"
  ],
  "related_registry_items": [
    {
      "id": "VI.T47",
      "title": "Differentiation Is Irreversible",
      "url": "/registry/object/VI.T47/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Source/Epigenetics.lean#L247-L256",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.Source.Epigenetics",
        "url": "/verify/taulib/docs/book-vi-source-epigenetics/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Source/Epigenetics.lean#L247-L256",
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

- Module: [TauLib.BookVI.Source.Epigenetics](/verify/taulib/docs/book-vi-source-epigenetics/)
- Source path: [`TauLib/BookVI/Source/Epigenetics.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Source/Epigenetics.lean#L247-L256)
- Source range: L247-L256
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.T47` — Differentiation Is Irreversible

## Immediate Comment / Docstring

```lean
/-- [VI.T47] Differentiation Is Irreversible Under Normal Conditions.
    Each step in the refinement tower restricts chromatin (VI.D81, monotone),
    and SelfDesc maintenance (VI.T03) preserves the restriction.
    Therefore descent through the Waddington landscape is irreversible
    under normal cellular conditions.
    Scope: τ-effective. -/
```

## Source Excerpt

```lean
structure DifferentiationIrreversible where
  /-- Chromatin restriction is monotone (VI.D81). -/
  monotone_restriction : Bool := true
  /-- SelfDesc maintains restriction (VI.T03). -/
  selfdesc_maintains : Bool := true
  /-- Descent is irreversible under normal conditions. -/
  irreversible : Bool := true
  /-- Scope: τ-effective. -/
  scope : String := "tau-effective"
  deriving Repr
```
