---
{
  "projection_kind": "taulib_declaration",
  "title": "FaceConflict",
  "permalink": "/verify/taulib/docs/book-v-cosmology-helium-fraction/face-conflict/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.HeliumFraction`.",
  "declaration_id": "TauLib.BookV.Cosmology.HeliumFraction::FaceConflict",
  "declaration_slug": "face-conflict",
  "kind": "structure",
  "name": "FaceConflict",
  "module_name": "TauLib.BookV.Cosmology.HeliumFraction",
  "module_url": "/verify/taulib/docs/book-v-cosmology-helium-fraction/",
  "source_line_start": 101,
  "source_line_end": 112,
  "registry_ids": [
    "V.D193"
  ],
  "related_registry_items": [
    {
      "id": "V.D193",
      "title": "Face-Conflict Probability",
      "url": "/registry/object/V.D193/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/HeliumFraction.lean#L101-L112",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/HeliumFraction.lean#L101-L112",
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
- Source path: [`TauLib/BookV/Cosmology/HeliumFraction.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/HeliumFraction.lean#L101-L112)
- Source range: L101-L112
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D193` — Face-Conflict Probability

## Immediate Comment / Docstring

```lean
/-- [V.D193] Face-conflict probability for phase-adjacent macrocells.
    P(conflict) = 1/3, proved by exhaustive enumeration:
    among 9 pairs (a₁,a₂) ∈ {0,1,2}², exactly 3 have a₂ < a₁. -/
```

## Source Excerpt

```lean
structure FaceConflict where
  /-- Number of conflict pairs (a₂ < a₁). -/
  conflict_count : Nat := 3
  /-- Total pairs. -/
  total_pairs : Nat := 9
  /-- Number of phase values per axis. -/
  phase_count : Nat := 3
  /-- Total = phase_count². -/
  total_is_sq : total_pairs = phase_count * phase_count
  /-- Conflict pairs: exactly those with a₂ < a₁. -/
  conflicts_enumerated : conflict_count = 3
  deriving Repr
```
