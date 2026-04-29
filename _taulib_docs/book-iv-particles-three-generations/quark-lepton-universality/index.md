---
{
  "projection_kind": "taulib_declaration",
  "title": "QuarkLeptonUniversality",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/quark-lepton-universality/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::QuarkLeptonUniversality",
  "declaration_slug": "quark-lepton-universality",
  "kind": "structure",
  "name": "QuarkLeptonUniversality",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 723,
  "source_line_end": 730,
  "registry_ids": [
    "IV.P187"
  ],
  "related_registry_items": [
    {
      "id": "IV.P187",
      "title": "Quark-Lepton Universality: Exponent Step ≈ −2.7",
      "url": "/registry/object/IV.P187/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L723-L730",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L723-L730",
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
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L723-L730)
- Source range: L723-L730
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P187` — Quark-Lepton Universality: Exponent Step ≈ −2.7

## Immediate Comment / Docstring

```lean
/-- [IV.P187] Quark-lepton universality: exponent step Δp ≈ −2.7 in both
    quark s/d (step = −2.797) and lepton τ/μ (step = −2.626) sectors.
    Difference 0.171 exceeds strict 0.1 threshold → approximate only. -/
```

## Source Excerpt

```lean
structure QuarkLeptonUniversality where
  /-- Approximate step exponent (×1000): −2.7 → 2700. -/
  step_x1000 : Nat := 2700
  /-- Number of sectors matching pattern (quark + lepton = 2). -/
  n_matching_sectors : Nat := 2
  /-- Step difference (×1000): 0.171 → 171 (exceeds 0.1 threshold = 100). -/
  step_diff_x1000 : Nat := 171
  deriving Repr
```
