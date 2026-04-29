---
{
  "projection_kind": "taulib_declaration",
  "title": "assignment_surjective",
  "permalink": "/verify/taulib/docs/book-iv-arena-coherence-kernel/assignment-surjective/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Arena.CoherenceKernel`.",
  "declaration_id": "TauLib.BookIV.Arena.CoherenceKernel::assignment_surjective",
  "declaration_slug": "assignment-surjective",
  "kind": "theorem",
  "name": "assignment_surjective",
  "module_name": "TauLib.BookIV.Arena.CoherenceKernel",
  "module_url": "/verify/taulib/docs/book-iv-arena-coherence-kernel/",
  "source_line_start": 62,
  "source_line_end": 69,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/CoherenceKernel.lean#L62-L69",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/CoherenceKernel.lean#L62-L69",
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

- Module: [TauLib.BookIV.Arena.CoherenceKernel](/verify/taulib/docs/book-iv-arena-coherence-kernel/)
- Source path: [`TauLib/BookIV/Arena/CoherenceKernel.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/CoherenceKernel.lean#L62-L69)
- Source range: L62-L69
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Φ hits all 5 sectors (surjective). -/
```

## Source Excerpt

```lean
theorem assignment_surjective (s : Sector) :
    ∃ g : Generator, GenSectorAssignment g = s := by
  cases s with
  | D => exact ⟨.alpha, rfl⟩
  | A => exact ⟨.pi, rfl⟩
  | B => exact ⟨.gamma, rfl⟩
  | C => exact ⟨.eta, rfl⟩
  | Omega => exact ⟨.omega, rfl⟩
```
