---
{
  "projection_kind": "taulib_declaration",
  "title": "mass_hierarchy",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/mass-hierarchy/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Electroweak.NeutrinoMode`.",
  "declaration_id": "TauLib.BookIV.Electroweak.NeutrinoMode::mass_hierarchy",
  "declaration_slug": "mass-hierarchy",
  "kind": "theorem",
  "name": "mass_hierarchy",
  "module_name": "TauLib.BookIV.Electroweak.NeutrinoMode",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/",
  "source_line_start": 188,
  "source_line_end": 191,
  "registry_ids": [
    "IV.P66"
  ],
  "related_registry_items": [
    {
      "id": "IV.P66",
      "title": "Mass Eigenvalue Ratios",
      "url": "/registry/object/IV.P66/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L188-L191",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L188-L191",
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

- Module: [TauLib.BookIV.Electroweak.NeutrinoMode](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/)
- Source path: [`TauLib/BookIV/Electroweak/NeutrinoMode.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L188-L191)
- Source range: L188-L191
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.P66` — Mass Eigenvalue Ratios

## Immediate Comment / Docstring

```lean
/-- [IV.P66] Neutrino mass hierarchy: m3 >> m2 >> m1.
    In the tau-framework, this is encoded by decreasing mass exponents:
    nu_tau (exponent 13) > nu_mu (14) > nu_e (15), where larger
    exponent means smaller mass (since iota_tau < 1).
    The "normal ordering" corresponds to exponent ordering. -/
```

## Source Excerpt

```lean
theorem mass_hierarchy :
    nu_tau.mass_exponent < nu_mu.mass_exponent ∧
    nu_mu.mass_exponent < nu_e.mass_exponent := by
  simp [nu_tau, nu_mu, nu_e]
```
