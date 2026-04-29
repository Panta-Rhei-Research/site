---
{
  "projection_kind": "taulib_declaration",
  "title": "MassHierarchyExponent",
  "permalink": "/verify/taulib/docs/book-v-coda-galpha-bridge/mass-hierarchy-exponent/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Coda.GAlphaBridge`.",
  "declaration_id": "TauLib.BookV.Coda.GAlphaBridge::MassHierarchyExponent",
  "declaration_slug": "mass-hierarchy-exponent",
  "kind": "structure",
  "name": "MassHierarchyExponent",
  "module_name": "TauLib.BookV.Coda.GAlphaBridge",
  "module_url": "/verify/taulib/docs/book-v-coda-galpha-bridge/",
  "source_line_start": 113,
  "source_line_end": 122,
  "registry_ids": [
    "V.T155"
  ],
  "related_registry_items": [
    {
      "id": "V.T155",
      "title": "Mass Hierarchy Exponent",
      "url": "/registry/object/V.T155/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/GAlphaBridge.lean#L113-L122",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Coda.GAlphaBridge",
        "url": "/verify/taulib/docs/book-v-coda-galpha-bridge/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/GAlphaBridge.lean#L113-L122",
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

- Module: [TauLib.BookV.Coda.GAlphaBridge](/verify/taulib/docs/book-v-coda-galpha-bridge/)
- Source path: [`TauLib/BookV/Coda/GAlphaBridge.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/GAlphaBridge.lean#L113-L122)
- Source range: L113-L122
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.T155` — Mass Hierarchy Exponent

## Immediate Comment / Docstring

```lean
/-- [V.T155] Mass hierarchy exponent: m_Pl/m_n ∝ α⁻⁹.
    Exponent 9 = 18/2: half the holonomy exponent (single-lobe
    contribution to the double-lobe winding number 18).

    - m_Pl = √(ℏc/G) ∝ α⁻⁹ · m_n (from G-α bridge)
    - The mass hierarchy is not mysterious: it is the 9th power of α
    - 9 = dim(τ³)² = 3² from the τ³ volume squared -/
```

## Source Excerpt

```lean
structure MassHierarchyExponent where
  /-- Single-lobe exponent. -/
  single_lobe_exp : Nat
  /-- Exponent is 9. -/
  exp_eq : single_lobe_exp = 9
  /-- Dimension of τ³. -/
  dim_tau3 : Nat := 3
  /-- Is half the holonomy exponent. -/
  is_half_holonomy : Bool := true
  deriving Repr
```
