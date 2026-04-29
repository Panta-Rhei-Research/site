---
{
  "projection_kind": "taulib_declaration",
  "title": "ThresholdUniquenessFiveSixths",
  "permalink": "/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/threshold-uniqueness-five-sixths/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.BBNBaryogenesis`.",
  "declaration_id": "TauLib.BookV.Cosmology.BBNBaryogenesis::ThresholdUniquenessFiveSixths",
  "declaration_slug": "threshold-uniqueness-five-sixths",
  "kind": "structure",
  "name": "ThresholdUniquenessFiveSixths",
  "module_name": "TauLib.BookV.Cosmology.BBNBaryogenesis",
  "module_url": "/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/",
  "source_line_start": 420,
  "source_line_end": 433,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BBNBaryogenesis.lean#L420-L433",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.BBNBaryogenesis",
        "url": "/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BBNBaryogenesis.lean#L420-L433",
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

- Module: [TauLib.BookV.Cosmology.BBNBaryogenesis](/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/)
- Source path: [`TauLib/BookV/Cosmology/BBNBaryogenesis.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BBNBaryogenesis.lean#L420-L433)
- Source range: L420-L433
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [V.T180 upgrade] The (5/6) factor is uniquely forced:

    1. Canonical ladder has exactly 6 thresholds (V.D58)
    2. Exactly 1 is resonant: L_B (baryogenesis), where the
       ω-crossing mediates baryon-number-violating processes
    3. ω is resonant because ω = γ ∩ η is the self-coupling
       singularity of L (the crossing point p_ω)
    4. No other threshold is resonant: the remaining 5 involve
       single-sector crossings or composite transitions without
       the ω self-coupling property
    5. Therefore 5/6 = (non-resonant)/(total) is uniquely forced -/
```

## Source Excerpt

```lean
structure ThresholdUniquenessFiveSixths where
  /-- Total canonical thresholds. -/
  total_thresholds : Nat := 6
  /-- Resonant thresholds (ω-crossing only). -/
  resonant_count : Nat := 1
  /-- Non-resonant thresholds. -/
  nonresonant_count : Nat := 5
  /-- ω-crossing is the unique self-coupling singularity. -/
  omega_unique_singularity : Bool := true
  /-- Partition: non-resonant + resonant = total. -/
  partition : nonresonant_count + resonant_count = total_thresholds
  /-- Uniqueness: exactly 1 resonant. -/
  uniqueness : resonant_count = 1
  deriving Repr
```
