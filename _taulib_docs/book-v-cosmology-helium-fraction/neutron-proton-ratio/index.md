---
{
  "projection_kind": "taulib_declaration",
  "title": "NeutronProtonRatio",
  "permalink": "/verify/taulib/docs/book-v-cosmology-helium-fraction/neutron-proton-ratio/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.HeliumFraction`.",
  "declaration_id": "TauLib.BookV.Cosmology.HeliumFraction::NeutronProtonRatio",
  "declaration_slug": "neutron-proton-ratio",
  "kind": "structure",
  "name": "NeutronProtonRatio",
  "module_name": "TauLib.BookV.Cosmology.HeliumFraction",
  "module_url": "/verify/taulib/docs/book-v-cosmology-helium-fraction/",
  "source_line_start": 222,
  "source_line_end": 227,
  "registry_ids": [
    "V.D196"
  ],
  "related_registry_items": [
    {
      "id": "V.D196",
      "title": "Neutron-to-Proton Ratio from Y_p",
      "url": "/registry/object/V.D196/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/HeliumFraction.lean#L222-L227",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.HeliumFraction",
        "url": "/verify/taulib/docs/book-v-cosmology-helium-fraction/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/HeliumFraction.lean#L222-L227",
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

- Module: [TauLib.BookV.Cosmology.HeliumFraction](/verify/taulib/docs/book-v-cosmology-helium-fraction/)
- Source path: [`TauLib/BookV/Cosmology/HeliumFraction.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/HeliumFraction.lean#L222-L227)
- Source range: L222-L227
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D196` — Neutron-to-Proton Ratio from Y_p

## Immediate Comment / Docstring

```lean
/-- [V.D196] Neutron-to-proton ratio n/p = 10/71 from Y_p = 20/81.
    Derivation: Y_p = 2(n/p)/(1+n/p) = 20/81
    → 162·n/p = 20·(1 + n/p) → 142·n/p = 20 → n/p = 10/71. -/
```

## Source Excerpt

```lean
structure NeutronProtonRatio where
  /-- Numerator. -/
  np_num : Nat := 10
  /-- Denominator. -/
  np_den : Nat := 71
  deriving Repr
```
