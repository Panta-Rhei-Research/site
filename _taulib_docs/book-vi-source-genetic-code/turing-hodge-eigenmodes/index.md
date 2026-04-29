---
{
  "projection_kind": "taulib_declaration",
  "title": "TuringHodgeEigenmodes",
  "permalink": "/verify/taulib/docs/book-vi-source-genetic-code/turing-hodge-eigenmodes/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Source.GeneticCode`.",
  "declaration_id": "TauLib.BookVI.Source.GeneticCode::TuringHodgeEigenmodes",
  "declaration_slug": "turing-hodge-eigenmodes",
  "kind": "structure",
  "name": "TuringHodgeEigenmodes",
  "module_name": "TauLib.BookVI.Source.GeneticCode",
  "module_url": "/verify/taulib/docs/book-vi-source-genetic-code/",
  "source_line_start": 140,
  "source_line_end": 149,
  "registry_ids": [
    "VI.T21"
  ],
  "related_registry_items": [
    {
      "id": "VI.T21",
      "title": "Turing Patterns as Hodge Eigenmode Instantiations",
      "url": "/registry/object/VI.T21/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Source/GeneticCode.lean#L140-L149",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.Source.GeneticCode",
        "url": "/verify/taulib/docs/book-vi-source-genetic-code/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Source/GeneticCode.lean#L140-L149",
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

- Module: [TauLib.BookVI.Source.GeneticCode](/verify/taulib/docs/book-vi-source-genetic-code/)
- Source path: [`TauLib/BookVI/Source/GeneticCode.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Source/GeneticCode.lean#L140-L149)
- Source range: L140-L149
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.T21` — Turing Patterns as Hodge Eigenmode Instantiations

## Immediate Comment / Docstring

```lean
/-- [VI.T21] Turing Patterns as Hodge Eigenmode Instantiations.
    Morphogenetic patterns = eigenfunctions of the Hodge Laplacian Δ_H.
    Reaction from τ¹ base, diffusion from T² fiber.
    Authority: Book III, Part IV (Hodge force); Book II, Ch 116 (τ-Hodge). -/
```

## Source Excerpt

```lean
structure TuringHodgeEigenmodes where
  /-- Reaction source: τ¹ (base, temporal). -/
  reaction_source : String := "tau1_base"
  /-- Diffusion domain: T² (fiber, spatial). -/
  diffusion_domain : String := "T2_fiber"
  /-- Governed by Hodge Laplacian Δ_H. -/
  hodge_laplacian : Bool := true
  /-- Scope: τ-effective. -/
  scope : String := "tau-effective"
  deriving Repr
```
