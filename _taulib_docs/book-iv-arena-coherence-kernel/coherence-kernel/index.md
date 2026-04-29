---
{
  "projection_kind": "taulib_declaration",
  "title": "CoherenceKernel",
  "permalink": "/verify/taulib/docs/book-iv-arena-coherence-kernel/coherence-kernel/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Arena.CoherenceKernel`.",
  "declaration_id": "TauLib.BookIV.Arena.CoherenceKernel::CoherenceKernel",
  "declaration_slug": "coherence-kernel",
  "kind": "structure",
  "name": "CoherenceKernel",
  "module_name": "TauLib.BookIV.Arena.CoherenceKernel",
  "module_url": "/verify/taulib/docs/book-iv-arena-coherence-kernel/",
  "source_line_start": 78,
  "source_line_end": 87,
  "registry_ids": [
    "IV.D246"
  ],
  "related_registry_items": [
    {
      "id": "IV.D246",
      "title": "Coherence Kernel --- Physics Presentation",
      "url": "/registry/object/IV.D246/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/CoherenceKernel.lean#L78-L87",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Arena.CoherenceKernel",
        "url": "/verify/taulib/docs/book-iv-arena-coherence-kernel/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/CoherenceKernel.lean#L78-L87",
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

- Module: [TauLib.BookIV.Arena.CoherenceKernel](/verify/taulib/docs/book-iv-arena-coherence-kernel/)
- Source path: [`TauLib/BookIV/Arena/CoherenceKernel.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/CoherenceKernel.lean#L78-L87)
- Source range: L78-L87
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D246` — Coherence Kernel --- Physics Presentation

## Immediate Comment / Docstring

```lean
/-- [IV.D246] The coherence kernel K: the categorical core generating
    all physics. At E₁, K = {α,π,γ,η,ω} with canonical sector assignment
    and polarity signatures. Minimal generating set for the coupling ledger. -/
```

## Source Excerpt

```lean
structure CoherenceKernel where
  /-- Number of generators. -/
  gen_count : Nat
  gen_count_eq : gen_count = 5
  /-- Number of sectors covered (= gen_count for bijective assignment). -/
  sector_count : Nat
  sector_count_eq : sector_count = 5
  /-- Bijective (gen_count = sector_count). -/
  bijective : gen_count = sector_count
  deriving Repr
```
