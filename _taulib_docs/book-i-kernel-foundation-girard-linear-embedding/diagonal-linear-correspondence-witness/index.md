---
{
  "projection_kind": "taulib_declaration",
  "title": "diagonal_linear_correspondence_witness",
  "permalink": "/verify/taulib/docs/book-i-kernel-foundation-girard-linear-embedding/diagonal-linear-correspondence-witness/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.KernelFoundation.GirardLinearEmbedding`.",
  "declaration_id": "TauLib.BookI.KernelFoundation.GirardLinearEmbedding::diagonal_linear_correspondence_witness",
  "declaration_slug": "diagonal-linear-correspondence-witness",
  "kind": "theorem",
  "name": "diagonal_linear_correspondence_witness",
  "module_name": "TauLib.BookI.KernelFoundation.GirardLinearEmbedding",
  "module_url": "/verify/taulib/docs/book-i-kernel-foundation-girard-linear-embedding/",
  "source_line_start": 247,
  "source_line_end": 252,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/KernelFoundation/GirardLinearEmbedding.lean#L247-L252",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.KernelFoundation.GirardLinearEmbedding",
        "url": "/verify/taulib/docs/book-i-kernel-foundation-girard-linear-embedding/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/KernelFoundation/GirardLinearEmbedding.lean#L247-L252",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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

- Module: [TauLib.BookI.KernelFoundation.GirardLinearEmbedding](/verify/taulib/docs/book-i-kernel-foundation-girard-linear-embedding/)
- Source path: [`TauLib/BookI/KernelFoundation/GirardLinearEmbedding.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/KernelFoundation/GirardLinearEmbedding.lean#L247-L252)
- Source range: L247-L252
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Paper §3 Def `diagonal-linear-correspondence` — bijection
    witness via existing `Tau.MetaLogic` infrastructure**.

    Three-part correspondence:
    - K5.1 ↔ no contraction
    - K5.2 ↔ linear resource use
    - K5.3 ↔ bounded finite context

    Direct cite of `Tau.MetaLogic.diag_linear_roundtrip` +
    `linear_diag_roundtrip` (existing). -/
```

## Source Excerpt

```lean
theorem diagonal_linear_correspondence_witness :
    -- Round-trip in one direction
    (∀ d : DiagonalAspect, linear_to_diag (diag_to_linear d) = d) ∧
    -- Round-trip in the other direction
    (∀ l : LinearAspect, diag_to_linear (linear_to_diag l) = l) :=
  ⟨diag_linear_roundtrip, linear_diag_roundtrip⟩
```
