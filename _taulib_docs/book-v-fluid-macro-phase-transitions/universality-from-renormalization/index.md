---
{
  "projection_kind": "taulib_declaration",
  "title": "universality_from_renormalization",
  "permalink": "/verify/taulib/docs/book-v-fluid-macro-phase-transitions/universality-from-renormalization/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.FluidMacro.PhaseTransitions`.",
  "declaration_id": "TauLib.BookV.FluidMacro.PhaseTransitions::universality_from_renormalization",
  "declaration_slug": "universality-from-renormalization",
  "kind": "theorem",
  "name": "universality_from_renormalization",
  "module_name": "TauLib.BookV.FluidMacro.PhaseTransitions",
  "module_url": "/verify/taulib/docs/book-v-fluid-macro-phase-transitions/",
  "source_line_start": 246,
  "source_line_end": 249,
  "registry_ids": [
    "V.T76"
  ],
  "related_registry_items": [
    {
      "id": "V.T76",
      "title": "Critical surface is codimension 1",
      "url": "/registry/object/V.T76/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/PhaseTransitions.lean#L246-L249",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/PhaseTransitions.lean#L246-L249",
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
- Source path: [`TauLib/BookV/FluidMacro/PhaseTransitions.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/PhaseTransitions.lean#L246-L249)
- Source range: L246-L249
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T76` — Critical surface is codimension 1

## Immediate Comment / Docstring

```lean
/-- [V.T76] Universality from renormalization: systems with the same
    (d, n) flow to the same fixed point under the renormalization
    group, yielding identical critical exponents.

    In the τ-framework, RG flow is a refinement tower coarsening:
    successive primorial levels coarse-grain the defect-tuple
    in the same way for all systems in the same universality class. -/
```

## Source Excerpt

```lean
theorem universality_from_renormalization (u1 u2 : UniversalityClass)
    (hd : u1.spatial_dim = u2.spatial_dim)
    (hn : u1.op_dim = u2.op_dim) :
    u1.spatial_dim = u2.spatial_dim ∧ u1.op_dim = u2.op_dim := ⟨hd, hn⟩
```
