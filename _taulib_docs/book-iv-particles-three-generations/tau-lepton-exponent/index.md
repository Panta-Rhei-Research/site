---
{
  "projection_kind": "taulib_declaration",
  "title": "TauLeptonExponent",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/tau-lepton-exponent/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::TauLeptonExponent",
  "declaration_slug": "tau-lepton-exponent",
  "kind": "structure",
  "name": "TauLeptonExponent",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 220,
  "source_line_end": 227,
  "registry_ids": [
    "IV.P123"
  ],
  "related_registry_items": [
    {
      "id": "IV.P123",
      "title": "Tau lepton mass exponent",
      "url": "/registry/object/IV.P123/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L220-L227",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L220-L227",
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
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L220-L227)
- Source range: L220-L227
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P123` — Tau lepton mass exponent

## Immediate Comment / Docstring

```lean
/-- [IV.P123] m_τ/m_e = ι_τ^(-15/2)(1 + δ_τ) where δ_τ ≈ +0.09 is O(α).
    Bare topological exponent: 15/2 = 7.5.
    The full-lemniscate winding mode produces the heaviest charged lepton. -/
```

## Source Excerpt

```lean
structure TauLeptonExponent where
  /-- Bare exponent (×2 to avoid fractions). -/
  bare_exp_x2 : Nat := 15
  /-- Effective exponent (×100). -/
  effective_exp_x100 : Nat := 759
  /-- Mode class: full lemniscate. -/
  mode_class : LemniscateModeClass := .fullLemniscate
  deriving Repr
```
