---
{
  "projection_kind": "taulib_declaration",
  "title": "EddingtonLimitData",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-accretion-jets/eddington-limit-data/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Astrophysics.AccretionJets`.",
  "declaration_id": "TauLib.BookV.Astrophysics.AccretionJets::EddingtonLimitData",
  "declaration_slug": "eddington-limit-data",
  "kind": "structure",
  "name": "EddingtonLimitData",
  "module_name": "TauLib.BookV.Astrophysics.AccretionJets",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-accretion-jets/",
  "source_line_start": 125,
  "source_line_end": 134,
  "registry_ids": [
    "V.D130"
  ],
  "related_registry_items": [
    {
      "id": "V.D130",
      "title": "Jet Axis (Topological Channel)",
      "url": "/registry/object/V.D130/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/AccretionJets.lean#L125-L134",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Astrophysics.AccretionJets",
        "url": "/verify/taulib/docs/book-v-astrophysics-accretion-jets/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/AccretionJets.lean#L125-L134",
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

- Module: [TauLib.BookV.Astrophysics.AccretionJets](/verify/taulib/docs/book-v-astrophysics-accretion-jets/)
- Source path: [`TauLib/BookV/Astrophysics/AccretionJets.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/AccretionJets.lean#L125-L134)
- Source range: L125-L134
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D130` — Jet Axis (Topological Channel)

## Immediate Comment / Docstring

```lean
/-- [V.D130] Eddington limit data: the maximum luminosity at which
    radiation pressure (B-sector) balances gravity (D-sector).

    L_Edd = 4πGMm_pc / σ_T ≈ 1.26 × 10³⁸ (M/M_☉) erg/s. -/
```

## Source Excerpt

```lean
structure EddingtonLimitData where
  /-- Mass of the accreting object (tenths of solar mass). -/
  mass_tenth_solar : Nat
  /-- Mass positive. -/
  mass_pos : mass_tenth_solar > 0
  /-- Eddington luminosity (10³⁸ erg/s, scaled × 100). -/
  l_edd_scaled : Nat
  /-- Whether the source is super-Eddington. -/
  is_super_eddington : Bool
  deriving Repr
```
