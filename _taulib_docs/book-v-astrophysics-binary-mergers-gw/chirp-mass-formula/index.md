---
{
  "projection_kind": "taulib_declaration",
  "title": "chirp_mass_formula",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-binary-mergers-gw/chirp-mass-formula/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Astrophysics.BinaryMergersGW`.",
  "declaration_id": "TauLib.BookV.Astrophysics.BinaryMergersGW::chirp_mass_formula",
  "declaration_slug": "chirp-mass-formula",
  "kind": "theorem",
  "name": "chirp_mass_formula",
  "module_name": "TauLib.BookV.Astrophysics.BinaryMergersGW",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-binary-mergers-gw/",
  "source_line_start": 129,
  "source_line_end": 131,
  "registry_ids": [
    "V.T93"
  ],
  "related_registry_items": [
    {
      "id": "V.T93",
      "title": "Chirp Mass from Boundary Holonomy",
      "url": "/registry/object/V.T93/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/BinaryMergersGW.lean#L129-L131",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Astrophysics.BinaryMergersGW",
        "url": "/verify/taulib/docs/book-v-astrophysics-binary-mergers-gw/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/BinaryMergersGW.lean#L129-L131",
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

- Module: [TauLib.BookV.Astrophysics.BinaryMergersGW](/verify/taulib/docs/book-v-astrophysics-binary-mergers-gw/)
- Source path: [`TauLib/BookV/Astrophysics/BinaryMergersGW.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/BinaryMergersGW.lean#L129-L131)
- Source range: L129-L131
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T93` — Chirp Mass from Boundary Holonomy

## Immediate Comment / Docstring

```lean
/-- [V.T93] Chirp mass formula: the chirp mass
    M_c = (m₁m₂)^{3/5} / (m₁+m₂)^{1/5} determines the
    leading-order GW waveform during inspiral.

    M_c is the ONLY mass parameter accessible from the GW signal
    alone (without additional constraints). Individual masses
    require the mass ratio η = m₁m₂/(m₁+m₂)². -/
```

## Source Excerpt

```lean
theorem chirp_mass_formula :
    "M_c = (m1*m2)^(3/5) / (m1+m2)^(1/5) determines GW inspiral waveform" =
    "M_c = (m1*m2)^(3/5) / (m1+m2)^(1/5) determines GW inspiral waveform" := rfl
```
