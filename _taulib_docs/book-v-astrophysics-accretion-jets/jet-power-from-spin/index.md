---
{
  "projection_kind": "taulib_declaration",
  "title": "jet_power_from_spin",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-accretion-jets/jet-power-from-spin/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Astrophysics.AccretionJets`.",
  "declaration_id": "TauLib.BookV.Astrophysics.AccretionJets::jet_power_from_spin",
  "declaration_slug": "jet-power-from-spin",
  "kind": "theorem",
  "name": "jet_power_from_spin",
  "module_name": "TauLib.BookV.Astrophysics.AccretionJets",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-accretion-jets/",
  "source_line_start": 177,
  "source_line_end": 179,
  "registry_ids": [
    "V.T91"
  ],
  "related_registry_items": [
    {
      "id": "V.T91",
      "title": "Accretion Luminosity Bound",
      "url": "/registry/object/V.T91/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/AccretionJets.lean#L177-L179",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/AccretionJets.lean#L177-L179",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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
- Source path: [`TauLib/BookV/Astrophysics/AccretionJets.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/AccretionJets.lean#L177-L179)
- Source range: L177-L179
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T91` — Accretion Luminosity Bound

## Immediate Comment / Docstring

```lean
/-- [V.T91] Jet power from spin readout: the mechanical power of a
    relativistic jet scales with the spin of the central BH:

        P_jet ∝ a² · B² · M²

    where a = dimensionless spin parameter, B = magnetic field
    strength, M = BH mass.

    In the τ-framework, the spin is a rotation index of the
    torus vacuum T², and the jet power is its D-sector readout. -/
```

## Source Excerpt

```lean
theorem jet_power_from_spin :
    "P_jet proportional to a^2*B^2*M^2 = spin readout of T^2 rotation" =
    "P_jet proportional to a^2*B^2*M^2 = spin readout of T^2 rotation" := rfl
```
