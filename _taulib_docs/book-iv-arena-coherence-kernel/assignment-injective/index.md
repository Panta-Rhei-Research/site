---
{
  "projection_kind": "taulib_declaration",
  "title": "assignment_injective",
  "permalink": "/corpus/taulib/docs/book-iv-arena-coherence-kernel/assignment-injective/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Arena.CoherenceKernel`.",
  "declaration_id": "TauLib.BookIV.Arena.CoherenceKernel::assignment_injective",
  "declaration_slug": "assignment-injective",
  "kind": "theorem",
  "name": "assignment_injective",
  "module_name": "TauLib.BookIV.Arena.CoherenceKernel",
  "module_url": "/corpus/taulib/docs/book-iv-arena-coherence-kernel/",
  "source_line_start": 48,
  "source_line_end": 59,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/CoherenceKernel.lean#L48-L59",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Arena.CoherenceKernel",
        "url": "/corpus/taulib/docs/book-iv-arena-coherence-kernel/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/CoherenceKernel.lean#L48-L59",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "role": "proof obligation",
      "status": "formal proof obligation checked"
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

- Module: [TauLib.BookIV.Arena.CoherenceKernel](/corpus/taulib/docs/book-iv-arena-coherence-kernel/)
- Source path: [`TauLib/BookIV/Arena/CoherenceKernel.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/CoherenceKernel.lean#L48-L59)
- Source range: L48-L59
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Φ maps each generator to a distinct sector (injective). -/
```

## Source Excerpt

```lean
theorem assignment_injective :
    GenSectorAssignment .alpha ≠ GenSectorAssignment .pi ∧
    GenSectorAssignment .alpha ≠ GenSectorAssignment .gamma ∧
    GenSectorAssignment .alpha ≠ GenSectorAssignment .eta ∧
    GenSectorAssignment .alpha ≠ GenSectorAssignment .omega ∧
    GenSectorAssignment .pi ≠ GenSectorAssignment .gamma ∧
    GenSectorAssignment .pi ≠ GenSectorAssignment .eta ∧
    GenSectorAssignment .pi ≠ GenSectorAssignment .omega ∧
    GenSectorAssignment .gamma ≠ GenSectorAssignment .eta ∧
    GenSectorAssignment .gamma ≠ GenSectorAssignment .omega ∧
    GenSectorAssignment .eta ≠ GenSectorAssignment .omega := by
  simp [GenSectorAssignment]
```
