---
{
  "projection_kind": "taulib_declaration",
  "title": "PMNSAnglePrediction",
  "permalink": "/corpus/taulib/docs/book-iv-electroweak-neutrino-mode/pmnsangle-prediction/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.NeutrinoMode`.",
  "declaration_id": "TauLib.BookIV.Electroweak.NeutrinoMode::PMNSAnglePrediction",
  "declaration_slug": "pmnsangle-prediction",
  "kind": "structure",
  "name": "PMNSAnglePrediction",
  "module_name": "TauLib.BookIV.Electroweak.NeutrinoMode",
  "module_url": "/corpus/taulib/docs/book-iv-electroweak-neutrino-mode/",
  "source_line_start": 444,
  "source_line_end": 453,
  "registry_ids": [
    "V.P123"
  ],
  "related_registry_items": [
    {
      "id": "V.P123",
      "title": "PMNS Mixing Angle Prediction",
      "url": "/registry/object/V.P123/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L444-L453",
  "formal_status": "defined",
  "declaration_role": "type/data schema",
  "formal_status_label": "type/data schema",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.NeutrinoMode",
        "url": "/corpus/taulib/docs/book-iv-electroweak-neutrino-mode/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L444-L453",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
      "role": "type/data schema",
      "status": "type/data schema"
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

- Module: [TauLib.BookIV.Electroweak.NeutrinoMode](/corpus/taulib/docs/book-iv-electroweak-neutrino-mode/)
- Source path: [`TauLib/BookIV/Electroweak/NeutrinoMode.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L444-L453)
- Source range: L444-L453
- Kind: `structure`
- Public role: `type/data schema`
- Formal status hint: `type/data schema`

## Registry Links

- `V.P123` — PMNS Mixing Angle Prediction

## Immediate Comment / Docstring

```lean
/-- [V.P123] PMNS angle prediction structure.
    Three mixing angles from σ-polarity eigenvectors;
    θ₁₃ ≈ 9.85° is the most reliable bare prediction.
    Full PMNS requires A-sector flavor rotation (IV.T153). -/
```

## Source Excerpt

```lean
structure PMNSAnglePrediction where
  /-- Number of mixing angles in PMNS. -/
  n_angles : Nat
  /-- Three mixing angles. -/
  angles_eq : n_angles = 3
  /-- Flavor rotation from A-sector needed for θ₁₂, θ₂₃. -/
  requires_flavor_rotation : Bool := true
  /-- θ₁₃ ≈ 9.85° is reasonable (15% from PDG 8.57°). -/
  theta13_reasonable : Bool := true
  deriving Repr
```
