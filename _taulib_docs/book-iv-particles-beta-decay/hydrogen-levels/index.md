---
{
  "projection_kind": "taulib_declaration",
  "title": "HydrogenLevels",
  "permalink": "/verify/taulib/docs/book-iv-particles-beta-decay/hydrogen-levels/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.BetaDecay`.",
  "declaration_id": "TauLib.BookIV.Particles.BetaDecay::HydrogenLevels",
  "declaration_slug": "hydrogen-levels",
  "kind": "structure",
  "name": "HydrogenLevels",
  "module_name": "TauLib.BookIV.Particles.BetaDecay",
  "module_url": "/verify/taulib/docs/book-iv-particles-beta-decay/",
  "source_line_start": 157,
  "source_line_end": 164,
  "registry_ids": [
    "IV.T85"
  ],
  "related_registry_items": [
    {
      "id": "IV.T85",
      "title": "Hydrogen energy levels",
      "url": "/registry/object/IV.T85/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/BetaDecay.lean#L157-L164",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/BetaDecay.lean#L157-L164",
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
- Source path: [`TauLib/BookIV/Particles/BetaDecay.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/BetaDecay.lean#L157-L164)
- Source range: L157-L164
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.T85` — Hydrogen energy levels

## Immediate Comment / Docstring

```lean
/-- [IV.T85] E_n = −α_em² · m_e · c² / (2n²) = −13.6 eV/n²
    for n = 1, 2, 3, ...

    Both α_em and m_e determined by ι_τ.
    Ground state: E₁ ≈ −13.606 eV.

    Energy in meV (×1000 for ground state = 13606). -/
```

## Source Excerpt

```lean
structure HydrogenLevels where
  /-- Ground state energy magnitude (meV). -/
  E1_meV : Nat := 13606
  /-- Fully determined by ι_τ. -/
  iota_determined : Bool := true
  /-- Scaling: 1/n² for principal quantum number n. -/
  scaling : String := "E_n = E_1 / n^2"
  deriving Repr
```
