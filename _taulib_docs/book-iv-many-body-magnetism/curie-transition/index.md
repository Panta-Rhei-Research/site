---
{
  "projection_kind": "taulib_declaration",
  "title": "CurieTransition",
  "permalink": "/verify/taulib/docs/book-iv-many-body-magnetism/curie-transition/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.ManyBody.Magnetism`.",
  "declaration_id": "TauLib.BookIV.ManyBody.Magnetism::CurieTransition",
  "declaration_slug": "curie-transition",
  "kind": "structure",
  "name": "CurieTransition",
  "module_name": "TauLib.BookIV.ManyBody.Magnetism",
  "module_url": "/verify/taulib/docs/book-iv-many-body-magnetism/",
  "source_line_start": 207,
  "source_line_end": 218,
  "registry_ids": [
    "IV.T209"
  ],
  "related_registry_items": [
    {
      "id": "IV.T209",
      "title": "Curie Transition as T² Symmetry Breaking",
      "url": "/registry/object/IV.T209/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/Magnetism.lean#L207-L218",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.ManyBody.Magnetism",
        "url": "/verify/taulib/docs/book-iv-many-body-magnetism/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/Magnetism.lean#L207-L218",
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

- Module: [TauLib.BookIV.ManyBody.Magnetism](/verify/taulib/docs/book-iv-many-body-magnetism/)
- Source path: [`TauLib/BookIV/ManyBody/Magnetism.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/Magnetism.lean#L207-L218)
- Source range: L207-L218
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.T209` — Curie Transition as T² Symmetry Breaking

## Immediate Comment / Docstring

```lean
/-- [IV.T209] **Curie transition as T² symmetry breaking.**
    Second-order phase transition in defect-tuple framework:
    - Order parameter φ = ⟨M⟩/M_sat (global d₄ coherence)
    - Below T_C: φ ≠ 0 (Z₂ or SO(3) broken)
    - Above T_C: φ = 0 (restored)
    - At T_C: φ vanishes continuously, χ diverges
    Critical exponents from universality class (Ising/Heisenberg). -/
```

## Source Excerpt

```lean
structure CurieTransition where
  /-- Second-order phase transition. -/
  second_order : Bool := true
  /-- Order parameter = d₄ coherence. -/
  order_param_d4 : Bool := true
  /-- Z₂ symmetry broken below T_C. -/
  z2_broken : Bool := true
  /-- Susceptibility diverges at T_C. -/
  susceptibility_diverges : Bool := true
  /-- Universality class determines exponents. -/
  universality : Bool := true
  deriving Repr
```
