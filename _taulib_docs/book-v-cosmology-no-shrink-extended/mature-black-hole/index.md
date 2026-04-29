---
{
  "projection_kind": "taulib_declaration",
  "title": "MatureBlackHole",
  "permalink": "/verify/taulib/docs/book-v-cosmology-no-shrink-extended/mature-black-hole/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.NoShrinkExtended`.",
  "declaration_id": "TauLib.BookV.Cosmology.NoShrinkExtended::MatureBlackHole",
  "declaration_slug": "mature-black-hole",
  "kind": "structure",
  "name": "MatureBlackHole",
  "module_name": "TauLib.BookV.Cosmology.NoShrinkExtended",
  "module_url": "/verify/taulib/docs/book-v-cosmology-no-shrink-extended/",
  "source_line_start": 72,
  "source_line_end": 89,
  "registry_ids": [
    "V.D173"
  ],
  "related_registry_items": [
    {
      "id": "V.D173",
      "title": "Mature Black Hole",
      "url": "/registry/object/V.D173/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/NoShrinkExtended.lean#L72-L89",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.NoShrinkExtended",
        "url": "/verify/taulib/docs/book-v-cosmology-no-shrink-extended/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/NoShrinkExtended.lean#L72-L89",
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

- Module: [TauLib.BookV.Cosmology.NoShrinkExtended](/verify/taulib/docs/book-v-cosmology-no-shrink-extended/)
- Source path: [`TauLib/BookV/Cosmology/NoShrinkExtended.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/NoShrinkExtended.lean#L72-L89)
- Source range: L72-L89
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D173` — Mature Black Hole

## Immediate Comment / Docstring

```lean
/-- [V.D173] Mature black hole: a BH that has reached both geometric
    stabilization (linking class ρ-invariant) and defect vanishing
    (S_def^BH(M) = 0). Maturity is reached at finite depth.

    Properties:
    - The linking class no longer changes under ρ
    - The defect functional is at its minimum (zero)
    - Mass is above Chandrasekhar limit -/
```

## Source Excerpt

```lean
structure MatureBlackHole where
  /-- The BH event. -/
  event : BlackHoleTopologicalEvent
  /-- Maturity depth. -/
  maturity_depth : Nat
  /-- Maturity at finite depth. -/
  maturity_pos : maturity_depth > 0
  /-- Maturity is at or after birth. -/
  after_birth : maturity_depth ≥ event.birth_depth
  /-- Linking class is ρ-invariant. -/
  rho_invariant : Bool := true
  /-- Defect is zero. -/
  defect_zero : Bool := true
  /-- Mass index (above Chandrasekhar). -/
  mass_index : Nat
  /-- Mass positive. -/
  mass_pos : mass_index > 0
  deriving Repr
```
