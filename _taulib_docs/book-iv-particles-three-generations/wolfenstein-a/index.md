---
{
  "projection_kind": "taulib_declaration",
  "title": "WolfensteinA",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/wolfenstein-a/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::WolfensteinA",
  "declaration_slug": "wolfenstein-a",
  "kind": "structure",
  "name": "WolfensteinA",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 1259,
  "source_line_end": 1268,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1259-L1268",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Particles.ThreeGenerations",
        "url": "/verify/taulib/docs/book-iv-particles-three-generations/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1259-L1268",
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

- Module: [TauLib.BookIV.Particles.ThreeGenerations](/verify/taulib/docs/book-iv-particles-three-generations/)
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1259-L1268)
- Source range: L1259-L1268
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- A = 1-(3/2)ι_τ² = 0.82527 at -887.3 ppm from PDG A=0.826.
    Improved from sqrt(1-ι_τ) at -17433 ppm (Wave 4B) by factor ~20. -/
```

## Source Excerpt

```lean
structure WolfensteinA where
  /-- Coefficient numerator: 3 in 3/2. -/
  coeff_numer : Nat := 3
  /-- Coefficient denominator: 2 in 3/2. -/
  coeff_denom : Nat := 2
  /-- Power of ι_τ in formula A = 1−(3/2)ι_τ². -/
  iota_power : Nat := 2
  /-- Deviation from PDG in ppm. -/
  deviation_ppm : Nat := 887
  deriving Repr
```
