---
{
  "projection_kind": "taulib_declaration",
  "title": "transition_positive",
  "permalink": "/verify/taulib/docs/book-v-fluid-macro-phase-transitions/transition-positive/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.FluidMacro.PhaseTransitions`.",
  "declaration_id": "TauLib.BookV.FluidMacro.PhaseTransitions::transition_positive",
  "declaration_slug": "transition-positive",
  "kind": "theorem",
  "name": "transition_positive",
  "module_name": "TauLib.BookV.FluidMacro.PhaseTransitions",
  "module_url": "/verify/taulib/docs/book-v-fluid-macro-phase-transitions/",
  "source_line_start": 438,
  "source_line_end": 445,
  "registry_ids": [
    "V.R471"
  ],
  "related_registry_items": [
    {
      "id": "V.R471",
      "title": "Condensed Matter Bridge Status (OQ-C6)",
      "url": "/registry/object/V.R471/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/PhaseTransitions.lean#L438-L445",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.FluidMacro.PhaseTransitions",
        "url": "/verify/taulib/docs/book-v-fluid-macro-phase-transitions/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/PhaseTransitions.lean#L438-L445",
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

- Module: [TauLib.BookV.FluidMacro.PhaseTransitions](/verify/taulib/docs/book-v-fluid-macro-phase-transitions/)
- Source path: [`TauLib/BookV/FluidMacro/PhaseTransitions.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/PhaseTransitions.lean#L438-L445)
- Source range: L438-L445
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.R471` — Condensed Matter Bridge Status (OQ-C6)

## Immediate Comment / Docstring

```lean
/-- The transition fraction is positive. -/
```

## Source Excerpt

```lean
theorem transition_positive : (0 : Nat) < 341 := by omega

-- [V.R471] OQ-C6 Status: PARTIAL.
-- Defect-tuple crossings apply to real condensed-matter systems.
-- ρ_cc ≈ 0.5ρ₀ is within standard range (0.3–0.7ρ₀).
-- Remaining: crust fraction overshoots; no gap calculation.

end Tau.BookV.FluidMacro
```
