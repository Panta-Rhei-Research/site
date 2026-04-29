---
{
  "projection_kind": "taulib_declaration",
  "title": "neutrino_weak_only",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/neutrino-weak-only/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Electroweak.NeutrinoMode`.",
  "declaration_id": "TauLib.BookIV.Electroweak.NeutrinoMode::neutrino_weak_only",
  "declaration_slug": "neutrino-weak-only",
  "kind": "theorem",
  "name": "neutrino_weak_only",
  "module_name": "TauLib.BookIV.Electroweak.NeutrinoMode",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/",
  "source_line_start": 173,
  "source_line_end": 177,
  "registry_ids": [
    "IV.T59"
  ],
  "related_registry_items": [
    {
      "id": "IV.T59",
      "title": "Neutrino Interaction Channels",
      "url": "/registry/object/IV.T59/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L173-L177",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L173-L177",
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
- Source path: [`TauLib/BookIV/Electroweak/NeutrinoMode.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L173-L177)
- Source range: L173-L177
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.T59` — Neutrino Interaction Channels

## Immediate Comment / Docstring

```lean
/-- [IV.T59] Neutrinos interact only via the weak force: they have
    zero electric charge (no EM coupling), zero color charge
    (no strong coupling), and negligible gravitational coupling
    (mass too small). Only the A-sector (weak) couples. -/
```

## Source Excerpt

```lean
theorem neutrino_weak_only :
    nu_e.weak_only = true ∧ nu_e.charge = 0 ∧ nu_e.color_neutral = true ∧
    nu_mu.weak_only = true ∧ nu_mu.charge = 0 ∧ nu_mu.color_neutral = true ∧
    nu_tau.weak_only = true ∧ nu_tau.charge = 0 ∧ nu_tau.color_neutral = true := by
  exact ⟨rfl, rfl, rfl, rfl, rfl, rfl, rfl, rfl, rfl⟩
```
