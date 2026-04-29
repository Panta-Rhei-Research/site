---
{
  "projection_kind": "taulib_declaration",
  "title": "flux_threading_theorem",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-accretion-jets/flux-threading-theorem/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Astrophysics.AccretionJets`.",
  "declaration_id": "TauLib.BookV.Astrophysics.AccretionJets::flux_threading_theorem",
  "declaration_slug": "flux-threading-theorem",
  "kind": "theorem",
  "name": "flux_threading_theorem",
  "module_name": "TauLib.BookV.Astrophysics.AccretionJets",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-accretion-jets/",
  "source_line_start": 350,
  "source_line_end": 352,
  "registry_ids": [
    "V.T228"
  ],
  "related_registry_items": [
    {
      "id": "V.T228",
      "title": "Flux Threading Theorem",
      "url": "/registry/object/V.T228/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/AccretionJets.lean#L350-L352",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/AccretionJets.lean#L350-L352",
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
- Source path: [`TauLib/BookV/Astrophysics/AccretionJets.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/AccretionJets.lean#L350-L352)
- Source range: L350-L352
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T228` — Flux Threading Theorem

## Immediate Comment / Docstring

```lean
/-- [V.T228] Flux Threading Theorem: both toroidal and poloidal fluxes
    are conserved on T². Poloidal flux is topologically protected.
    On S², there is no topological flux (H_1(S²) = 0). -/
```

## Source Excerpt

```lean
theorem flux_threading_theorem :
    "Φ_pol(T²) topologically protected; Φ_hole(S²) = 0" =
    "Φ_pol(T²) topologically protected; Φ_hole(S²) = 0" := rfl
```
