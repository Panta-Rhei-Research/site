---
{
  "projection_kind": "taulib_declaration",
  "title": "GravitationalTension",
  "permalink": "/verify/taulib/docs/book-v-cosmology-bhbirth-topology/gravitational-tension/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.BHBirthTopology`.",
  "declaration_id": "TauLib.BookV.Cosmology.BHBirthTopology::GravitationalTension",
  "declaration_slug": "gravitational-tension",
  "kind": "structure",
  "name": "GravitationalTension",
  "module_name": "TauLib.BookV.Cosmology.BHBirthTopology",
  "module_url": "/verify/taulib/docs/book-v-cosmology-bhbirth-topology/",
  "source_line_start": 64,
  "source_line_end": 73,
  "registry_ids": [
    "V.D163"
  ],
  "related_registry_items": [
    {
      "id": "V.D163",
      "title": "Gravitational Tension",
      "url": "/registry/object/V.D163/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BHBirthTopology.lean#L64-L73",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.BHBirthTopology",
        "url": "/verify/taulib/docs/book-v-cosmology-bhbirth-topology/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BHBirthTopology.lean#L64-L73",
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

- Module: [TauLib.BookV.Cosmology.BHBirthTopology](/verify/taulib/docs/book-v-cosmology-bhbirth-topology/)
- Source path: [`TauLib/BookV/Cosmology/BHBirthTopology.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BHBirthTopology.lean#L64-L73)
- Source range: L64-L73
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D163` — Gravitational Tension

## Immediate Comment / Docstring

```lean
/-- [V.D163] Gravitational tension at region U in τ³:
    G(U) = κ(D;1) · ||T[χ]|_U||

    κ(D;1) = 1 − ι_τ ≈ 0.6585 (D-sector self-coupling).
    T[χ] = boundary character stress-energy. -/
```

## Source Excerpt

```lean
structure GravitationalTension where
  /-- Tension numerator (scaled). -/
  tension_numer : Nat
  /-- Tension denominator. -/
  tension_denom : Nat
  /-- Denominator positive. -/
  denom_pos : tension_denom > 0
  /-- Region identifier. -/
  region_id : String := "U"
  deriving Repr
```
