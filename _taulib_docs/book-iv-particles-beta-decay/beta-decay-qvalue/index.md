---
{
  "projection_kind": "taulib_declaration",
  "title": "BetaDecayQValue",
  "permalink": "/verify/taulib/docs/book-iv-particles-beta-decay/beta-decay-qvalue/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.BetaDecay`.",
  "declaration_id": "TauLib.BookIV.Particles.BetaDecay::BetaDecayQValue",
  "declaration_slug": "beta-decay-qvalue",
  "kind": "structure",
  "name": "BetaDecayQValue",
  "module_name": "TauLib.BookIV.Particles.BetaDecay",
  "module_url": "/verify/taulib/docs/book-iv-particles-beta-decay/",
  "source_line_start": 84,
  "source_line_end": 95,
  "registry_ids": [
    "IV.P125"
  ],
  "related_registry_items": [
    {
      "id": "IV.P125",
      "title": "Beta-decay Q-value",
      "url": "/registry/object/IV.P125/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/BetaDecay.lean#L84-L95",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Particles.BetaDecay",
        "url": "/verify/taulib/docs/book-iv-particles-beta-decay/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/BetaDecay.lean#L84-L95",
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

- Module: [TauLib.BookIV.Particles.BetaDecay](/verify/taulib/docs/book-iv-particles-beta-decay/)
- Source path: [`TauLib/BookIV/Particles/BetaDecay.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/BetaDecay.lean#L84-L95)
- Source range: L84-L95
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P125` — Beta-decay Q-value

## Immediate Comment / Docstring

```lean
/-- [IV.P125] Q_β = (δ_A − m_e)c² where both δ_A and m_e are determined
    by ι_τ through the mass ratio chain.

    Values in keV:
    - δ_A ≈ 1293 keV (proton-neutron mass difference)
    - m_e ≈ 511 keV (electron mass)
    - Q_β ≈ 782 keV
    - Experimental: Q_β = 782.333(4) keV -/
```

## Source Excerpt

```lean
structure BetaDecayQValue where
  /-- δ_A in keV. -/
  delta_A_keV : Nat := 1293
  /-- m_e in keV. -/
  m_e_keV : Nat := 511
  /-- Q_β predicted in keV. -/
  q_predicted_keV : Nat := 782
  /-- Q_β experimental in keV (×1000). -/
  q_exp_keV_x1000 : Nat := 782333
  /-- Agreement: sub-percent. -/
  sub_percent : Bool := true
  deriving Repr
```
