---
{
  "projection_kind": "taulib_declaration",
  "title": "cosmological_bound",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/cosmological-bound/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Electroweak.NeutrinoMode`.",
  "declaration_id": "TauLib.BookIV.Electroweak.NeutrinoMode::cosmological_bound",
  "declaration_slug": "cosmological-bound",
  "kind": "def",
  "name": "cosmological_bound",
  "module_name": "TauLib.BookIV.Electroweak.NeutrinoMode",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/",
  "source_line_start": 413,
  "source_line_end": 415,
  "registry_ids": [
    "V.T166"
  ],
  "related_registry_items": [
    {
      "id": "V.T166",
      "title": "Cosmological Bound Satisfaction",
      "url": "/registry/object/V.T166/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L413-L415",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.NeutrinoMode",
        "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L413-L415",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
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

- Module: [TauLib.BookIV.Electroweak.NeutrinoMode](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/)
- Source path: [`TauLib/BookIV/Electroweak/NeutrinoMode.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L413-L415)
- Source range: L413-L415
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `V.T166` — Cosmological Bound Satisfaction

## Immediate Comment / Docstring

```lean
/-- [V.T166] With Sprint 3 best-fit, the cosmological bound is satisfied:
    Σmν = 0.089 eV < 0.12 eV (Planck 2018). -/
```

## Source Excerpt

```lean
def cosmological_bound : String :=
  "Sprint 3 best-fit (3.7,4.8,2.8): Sigma_m_nu = 0.089 eV < 0.12 eV (Planck). " ++
  "Masses: m1=0.017 eV, m2=0.019 eV, m3=0.053 eV. Bound satisfied."
```
