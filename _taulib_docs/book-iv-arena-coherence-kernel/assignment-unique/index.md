---
{
  "projection_kind": "taulib_declaration",
  "title": "assignment_unique",
  "permalink": "/verify/taulib/docs/book-iv-arena-coherence-kernel/assignment-unique/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Arena.CoherenceKernel`.",
  "declaration_id": "TauLib.BookIV.Arena.CoherenceKernel::assignment_unique",
  "declaration_slug": "assignment-unique",
  "kind": "theorem",
  "name": "assignment_unique",
  "module_name": "TauLib.BookIV.Arena.CoherenceKernel",
  "module_url": "/verify/taulib/docs/book-iv-arena-coherence-kernel/",
  "source_line_start": 127,
  "source_line_end": 136,
  "registry_ids": [
    "IV.P146"
  ],
  "related_registry_items": [
    {
      "id": "IV.P146",
      "title": "Uniqueness of Assignment",
      "url": "/registry/object/IV.P146/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/CoherenceKernel.lean#L127-L136",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/CoherenceKernel.lean#L127-L136",
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
- Source path: [`TauLib/BookIV/Arena/CoherenceKernel.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/CoherenceKernel.lean#L127-L136)
- Source range: L127-L136
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.P146` — Uniqueness of Assignment

## Immediate Comment / Docstring

```lean
/-- [IV.P146] Uniqueness of generator–sector assignment:
    any assignment Ψ agreeing on polarity and depth must equal Φ.
    Proved by exhaustive case analysis on generator × sector. -/
```

## Source Excerpt

```lean
theorem assignment_unique (Psi : Generator → Sector)
    (h_pol : ∀ g, (sector_physics (Psi g)).polarity = gen_polarity g)
    (h_dep : ∀ g, (sector_physics (Psi g)).depth = gen_depth g) :
    ∀ g, Psi g = GenSectorAssignment g := by
  intro g
  have hp := h_pol g; have hd := h_dep g
  -- Rewrite polarity/depth to simple match expressions
  rw [sp_polarity] at hp; rw [sp_depth] at hd
  simp only [gen_polarity, gen_depth, GenSectorAssignment, sp_polarity, sp_depth] at hp hd ⊢
  cases g <;> cases hPsi : (Psi _) <;> simp_all
```
