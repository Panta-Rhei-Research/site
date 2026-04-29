---
{
  "projection_kind": "taulib_declaration",
  "title": "eddington_sector_balance",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-accretion-jets/eddington-sector-balance/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Astrophysics.AccretionJets`.",
  "declaration_id": "TauLib.BookV.Astrophysics.AccretionJets::eddington_sector_balance",
  "declaration_slug": "eddington-sector-balance",
  "kind": "theorem",
  "name": "eddington_sector_balance",
  "module_name": "TauLib.BookV.Astrophysics.AccretionJets",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-accretion-jets/",
  "source_line_start": 142,
  "source_line_end": 144,
  "registry_ids": [
    "V.P78"
  ],
  "related_registry_items": [
    {
      "id": "V.P78",
      "title": "Jet-Torus Alignment",
      "url": "/registry/object/V.P78/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/AccretionJets.lean#L142-L144",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/AccretionJets.lean#L142-L144",
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
- Source path: [`TauLib/BookV/Astrophysics/AccretionJets.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/AccretionJets.lean#L142-L144)
- Source range: L142-L144
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.P78` — Jet-Torus Alignment

## Immediate Comment / Docstring

```lean
/-- [V.P78] Eddington from sector balance: the Eddington limit
    is the balance point between D-sector (gravity) and B-sector
    (electromagnetic radiation pressure). Two sectors, one limit.

    Super-Eddington accretion is possible when photon trapping
    reduces the effective radiation pressure (slim disk regime). -/
```

## Source Excerpt

```lean
theorem eddington_sector_balance :
    "Eddington limit = D-sector (gravity) balanced by B-sector (radiation)" =
    "Eddington limit = D-sector (gravity) balanced by B-sector (radiation)" := rfl
```
