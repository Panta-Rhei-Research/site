---
{
  "projection_kind": "taulib_declaration",
  "title": "neutrino_cf_asymmetry",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/neutrino-cf-asymmetry/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Electroweak.NeutrinoMode`.",
  "declaration_id": "TauLib.BookIV.Electroweak.NeutrinoMode::neutrino_cf_asymmetry",
  "declaration_slug": "neutrino-cf-asymmetry",
  "kind": "def",
  "name": "neutrino_cf_asymmetry",
  "module_name": "TauLib.BookIV.Electroweak.NeutrinoMode",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/",
  "source_line_start": 590,
  "source_line_end": 592,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L590-L592",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L590-L592",
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
- Source path: [`TauLib/BookIV/Electroweak/NeutrinoMode.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L590-L592)
- Source range: L590-L592
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- CF-motivated asymmetry in σ-polarity exponents.
    a₂=13 in CF(ι_τ⁻¹)=[2;1,13,3,...] → Δpq=14/13, Δpr=12/13.
    CF candidate gives ratio 34.28 (+52356 ppm) — conjectural.
    Grid optimum: (Δpq=1.16, Δpr=0.87) at +7.4 ppm (V.T175). -/
```

## Source Excerpt

```lean
def neutrino_cf_asymmetry : String :=
  "CF(ι_τ⁻¹) a₂=13: Δpq=14/13, Δpr=12/13; asymmetry=2/13=0.154. " ++
  "CF candidate fails at +52356 ppm. Grid optimum (1.16,0.87) at +7.4 ppm (tau-effective)."
```
