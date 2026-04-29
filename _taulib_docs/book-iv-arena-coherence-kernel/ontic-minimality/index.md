---
{
  "projection_kind": "taulib_declaration",
  "title": "ontic_minimality",
  "permalink": "/verify/taulib/docs/book-iv-arena-coherence-kernel/ontic-minimality/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Arena.CoherenceKernel`.",
  "declaration_id": "TauLib.BookIV.Arena.CoherenceKernel::ontic_minimality",
  "declaration_slug": "ontic-minimality",
  "kind": "theorem",
  "name": "ontic_minimality",
  "module_name": "TauLib.BookIV.Arena.CoherenceKernel",
  "module_url": "/verify/taulib/docs/book-iv-arena-coherence-kernel/",
  "source_line_start": 151,
  "source_line_end": 167,
  "registry_ids": [
    "IV.D248"
  ],
  "related_registry_items": [
    {
      "id": "IV.D248",
      "title": "Ontic Minimality",
      "url": "/registry/object/IV.D248/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/CoherenceKernel.lean#L151-L167",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/CoherenceKernel.lean#L151-L167",
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
- Source path: [`TauLib/BookIV/Arena/CoherenceKernel.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/CoherenceKernel.lean#L151-L167)
- Source range: L151-L167
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.D248` — Ontic Minimality

## Immediate Comment / Docstring

```lean
/-- [IV.D248] Ontic minimality: each generator is the unique preimage
    of its sector under Φ, so removing any one loses a sector. -/
```

## Source Excerpt

```lean
theorem ontic_minimality :
    GenSectorAssignment .alpha = .D ∧ GenSectorAssignment .pi ≠ .D ∧
    GenSectorAssignment .gamma ≠ .D ∧ GenSectorAssignment .eta ≠ .D ∧
    GenSectorAssignment .omega ≠ .D ∧
    GenSectorAssignment .pi = .A ∧ GenSectorAssignment .alpha ≠ .A ∧
    GenSectorAssignment .gamma ≠ .A ∧ GenSectorAssignment .eta ≠ .A ∧
    GenSectorAssignment .omega ≠ .A ∧
    GenSectorAssignment .gamma = .B ∧ GenSectorAssignment .alpha ≠ .B ∧
    GenSectorAssignment .pi ≠ .B ∧ GenSectorAssignment .eta ≠ .B ∧
    GenSectorAssignment .omega ≠ .B ∧
    GenSectorAssignment .eta = .C ∧ GenSectorAssignment .alpha ≠ .C ∧
    GenSectorAssignment .pi ≠ .C ∧ GenSectorAssignment .gamma ≠ .C ∧
    GenSectorAssignment .omega ≠ .C ∧
    GenSectorAssignment .omega = .Omega ∧ GenSectorAssignment .alpha ≠ .Omega ∧
    GenSectorAssignment .pi ≠ .Omega ∧ GenSectorAssignment .gamma ≠ .Omega ∧
    GenSectorAssignment .eta ≠ .Omega := by
  simp [GenSectorAssignment]
```
