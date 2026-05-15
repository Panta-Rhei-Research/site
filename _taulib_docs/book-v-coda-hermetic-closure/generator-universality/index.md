---
{
  "projection_kind": "taulib_declaration",
  "title": "GeneratorUniversality",
  "permalink": "/corpus/taulib/docs/book-v-coda-hermetic-closure/generator-universality/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Coda.HermeticClosure`.",
  "declaration_id": "TauLib.BookV.Coda.HermeticClosure::GeneratorUniversality",
  "declaration_slug": "generator-universality",
  "kind": "structure",
  "name": "GeneratorUniversality",
  "module_name": "TauLib.BookV.Coda.HermeticClosure",
  "module_url": "/corpus/taulib/docs/book-v-coda-hermetic-closure/",
  "source_line_start": 240,
  "source_line_end": 253,
  "registry_ids": [
    "V.P119"
  ],
  "related_registry_items": [
    {
      "id": "V.P119",
      "title": "Generator universality",
      "url": "/registry/object/V.P119/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/HermeticClosure.lean#L240-L253",
  "formal_status": "defined",
  "declaration_role": "type/data schema",
  "formal_status_label": "type/data schema",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Coda.HermeticClosure",
        "url": "/corpus/taulib/docs/book-v-coda-hermetic-closure/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/HermeticClosure.lean#L240-L253",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
      "role": "type/data schema",
      "status": "type/data schema"
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

- Module: [TauLib.BookV.Coda.HermeticClosure](/corpus/taulib/docs/book-v-coda-hermetic-closure/)
- Source path: [`TauLib/BookV/Coda/HermeticClosure.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/HermeticClosure.lean#L240-L253)
- Source range: L240-L253
- Kind: `structure`
- Public role: `type/data schema`
- Formal status hint: `type/data schema`

## Registry Links

- `V.P119` — Generator universality

## Immediate Comment / Docstring

```lean
/-- [V.P119] Generator universality: each generator acts on H_∂[ω]
    at every scale. No RG flow of generator itself; effective coupling
    is depth-dependent.

    The generators {α, π, γ, η, ω} are universal characters on L.
    They do not run with energy scale (unlike QFT couplings). The
    *effective* coupling κ(X;n) at depth n changes because the
    threshold admissibility changes, not because X itself runs. -/
```

## Source Excerpt

```lean
structure GeneratorUniversality where
  /-- Number of universal generators. -/
  n_generators : Nat
  /-- Five generators. -/
  gens_eq : n_generators = 5
  /-- No RG flow of generators. -/
  no_rg_flow : Bool := true
  /-- Coupling is depth-dependent. -/
  depth_dependent : Bool := true
  /-- Base generators (α, π). -/
  base_count : Nat := 2
  /-- Fiber generators (γ, η, ω). -/
  fiber_count : Nat := 3
  deriving Repr
```
