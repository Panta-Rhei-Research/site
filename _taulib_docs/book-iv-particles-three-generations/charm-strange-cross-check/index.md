---
{
  "projection_kind": "taulib_declaration",
  "title": "CharmStrangeCrossCheck",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/charm-strange-cross-check/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::CharmStrangeCrossCheck",
  "declaration_slug": "charm-strange-cross-check",
  "kind": "structure",
  "name": "CharmStrangeCrossCheck",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 2521,
  "source_line_end": 2530,
  "registry_ids": [
    "IV.D375"
  ],
  "related_registry_items": [
    {
      "id": "IV.D375",
      "title": "m_c/m_s Cross-Check",
      "url": "/registry/object/IV.D375/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2521-L2530",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2521-L2530",
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
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2521-L2530)
- Source range: L2521-L2530
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D375` — m_c/m_s Cross-Check

## Immediate Comment / Docstring

```lean
/-- [IV.D375] m_c/m_s cross-check: τ-chain ratio vs PDG.
    m_c(τ)/m_s(τ) = 13.62 vs naïve PDG 13.63.
    FLAG (same scale): 11.74 ± 0.05 (16% discrepancy from scale mismatch). -/
```

## Source Excerpt

```lean
structure CharmStrangeCrossCheck where
  /-- τ-chain ratio (×100). -/
  ratio_x100 : Nat := 1362
  /-- Naïve PDG ratio (×100). -/
  pdg_naive_x100 : Nat := 1363
  /-- FLAG same-scale ratio (×100). -/
  flag_ratio_x100 : Nat := 1174
  /-- Internal consistency: τ-chain matches naïve PDG. -/
  internal_consistent : Bool := true
  deriving Repr
```
