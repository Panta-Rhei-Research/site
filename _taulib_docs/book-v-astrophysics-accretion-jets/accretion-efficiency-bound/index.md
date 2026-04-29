---
{
  "projection_kind": "taulib_declaration",
  "title": "accretion_efficiency_bound",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-accretion-jets/accretion-efficiency-bound/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Astrophysics.AccretionJets`.",
  "declaration_id": "TauLib.BookV.Astrophysics.AccretionJets::accretion_efficiency_bound",
  "declaration_slug": "accretion-efficiency-bound",
  "kind": "theorem",
  "name": "accretion_efficiency_bound",
  "module_name": "TauLib.BookV.Astrophysics.AccretionJets",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-accretion-jets/",
  "source_line_start": 255,
  "source_line_end": 256,
  "registry_ids": [
    "V.T92"
  ],
  "related_registry_items": [
    {
      "id": "V.T92",
      "title": "AGN Unification Theorem",
      "url": "/registry/object/V.T92/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/AccretionJets.lean#L255-L256",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/AccretionJets.lean#L255-L256",
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
- Source path: [`TauLib/BookV/Astrophysics/AccretionJets.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/AccretionJets.lean#L255-L256)
- Source range: L255-L256
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T92` — AGN Unification Theorem

## Immediate Comment / Docstring

```lean
/-- [V.T92] Accretion efficiency bound: gravitational accretion
    efficiency (up to ~40% for max spin) greatly exceeds nuclear
    fusion efficiency (~0.7%).

    This is the most efficient energy extraction mechanism and
    explains why quasars outshine their host galaxies despite
    accreting modest mass rates. -/
```

## Source Excerpt

```lean
theorem accretion_efficiency_bound :
    nuclear_efficiency < max_accretion_efficiency := by native_decide
```
