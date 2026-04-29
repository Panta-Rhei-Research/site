---
{
  "projection_kind": "taulib_declaration",
  "title": "canonical_kernel",
  "permalink": "/verify/taulib/docs/book-iv-arena-coherence-kernel/canonical-kernel/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Arena.CoherenceKernel`.",
  "declaration_id": "TauLib.BookIV.Arena.CoherenceKernel::canonical_kernel",
  "declaration_slug": "canonical-kernel",
  "kind": "def",
  "name": "canonical_kernel",
  "module_name": "TauLib.BookIV.Arena.CoherenceKernel",
  "module_url": "/verify/taulib/docs/book-iv-arena-coherence-kernel/",
  "source_line_start": 90,
  "source_line_end": 95,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/CoherenceKernel.lean#L90-L95",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/CoherenceKernel.lean#L90-L95",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
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
- Source path: [`TauLib/BookIV/Arena/CoherenceKernel.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/CoherenceKernel.lean#L90-L95)
- Source range: L90-L95
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The canonical coherence kernel at E₁. -/
```

## Source Excerpt

```lean
def canonical_kernel : CoherenceKernel where
  gen_count := 5
  gen_count_eq := rfl
  sector_count := 5
  sector_count_eq := rfl
  bijective := rfl
```
