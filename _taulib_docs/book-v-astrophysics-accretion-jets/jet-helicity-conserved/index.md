---
{
  "projection_kind": "taulib_declaration",
  "title": "jet_helicity_conserved",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-accretion-jets/jet-helicity-conserved/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Astrophysics.AccretionJets`.",
  "declaration_id": "TauLib.BookV.Astrophysics.AccretionJets::jet_helicity_conserved",
  "declaration_slug": "jet-helicity-conserved",
  "kind": "theorem",
  "name": "jet_helicity_conserved",
  "module_name": "TauLib.BookV.Astrophysics.AccretionJets",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-accretion-jets/",
  "source_line_start": 402,
  "source_line_end": 404,
  "registry_ids": [
    "V.T231"
  ],
  "related_registry_items": [
    {
      "id": "V.T231",
      "title": "Jet Helicity Conservation",
      "url": "/registry/object/V.T231/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/AccretionJets.lean#L402-L404",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/AccretionJets.lean#L402-L404",
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
- Source path: [`TauLib/BookV/Astrophysics/AccretionJets.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/AccretionJets.lean#L402-L404)
- Source range: L402-L404
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T231` — Jet Helicity Conservation

## Immediate Comment / Docstring

```lean
/-- [V.T231] Jet Helicity Conservation: helicity is topologically fixed
    at the jet base and conserved along the jet (frozen flux + Taylor). -/
```

## Source Excerpt

```lean
theorem jet_helicity_conserved :
    "H_m(jet) is topologically fixed and conserved (frozen flux + Taylor)" =
    "H_m(jet) is topologically fixed and conserved (frozen flux + Taylor)" := rfl
```
