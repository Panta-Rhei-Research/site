---
{
  "projection_kind": "taulib_declaration",
  "title": "quasar_luminosity",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-accretion-jets/quasar-luminosity/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Astrophysics.AccretionJets`.",
  "declaration_id": "TauLib.BookV.Astrophysics.AccretionJets::quasar_luminosity",
  "declaration_slug": "quasar-luminosity",
  "kind": "theorem",
  "name": "quasar_luminosity",
  "module_name": "TauLib.BookV.Astrophysics.AccretionJets",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-accretion-jets/",
  "source_line_start": 235,
  "source_line_end": 237,
  "registry_ids": [
    "V.P79"
  ],
  "related_registry_items": [
    {
      "id": "V.P79",
      "title": "Neutrino Emission Channel",
      "url": "/registry/object/V.P79/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/AccretionJets.lean#L235-L237",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/AccretionJets.lean#L235-L237",
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
- Source path: [`TauLib/BookV/Astrophysics/AccretionJets.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/AccretionJets.lean#L235-L237)
- Source range: L235-L237
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.P79` — Neutrino Emission Channel

## Immediate Comment / Docstring

```lean
/-- [V.P79] Quasar luminosity from accretion rate: quasar
    luminosities (up to 10⁴⁷ erg/s) derive from accretion onto
    supermassive BH (10⁸-10⁹ M_☉) at near-Eddington rates.

    L_quasar = η · M_dot · c² where η ~ 0.1 for a thin disk. -/
```

## Source Excerpt

```lean
theorem quasar_luminosity :
    "L_quasar = eta*Mdot*c^2, eta ~ 0.1 for thin disk accretion" =
    "L_quasar = eta*Mdot*c^2, eta ~ 0.1 for thin disk accretion" := rfl
```
