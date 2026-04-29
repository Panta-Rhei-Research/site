---
{
  "projection_kind": "taulib_declaration",
  "title": "pmns_angles",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/pmns-angles/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Electroweak.NeutrinoMode`.",
  "declaration_id": "TauLib.BookIV.Electroweak.NeutrinoMode::pmns_angles",
  "declaration_slug": "pmns-angles",
  "kind": "def",
  "name": "pmns_angles",
  "module_name": "TauLib.BookIV.Electroweak.NeutrinoMode",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/",
  "source_line_start": 435,
  "source_line_end": 438,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L435-L438",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L435-L438",
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
- Source path: [`TauLib/BookIV/Electroweak/NeutrinoMode.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L435-L438)
- Source range: L435-L438
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `V.P123` — PMNS Mixing Angle Prediction

## Immediate Comment / Docstring

```lean
/-- [V.P123] PMNS mixing angles from sigma-polarity eigenvectors.
    Sprint 4 lab results (p=3.7, q=4.8, r=2.8):
    - θ₁₃ ≈ 9.85° (PDG: 8.57°, deviation +1.3°, 15% — reasonable)
    - θ₁₂ ≈ 45.86° (PDG: 33.41° — fails, flavor-basis rotation needed)
    - θ₂₃ ≈ 80.01° (PDG: 49.2° — fails, flavor-basis rotation needed)
    Full PMNS requires A-sector rotation from (lobe₁, crossing, lobe₂)
    to (νe, νμ, ντ) flavor basis — open for Sprint 5. -/
```

## Source Excerpt

```lean
def pmns_angles : String :=
  "Sprint 4 (p=3.7,q=4.8,r=2.8): theta13=9.85 (PDG 8.57, +15%), " ++
  "theta12=45.86 (PDG 33.41, fails), theta23=80.01 (PDG 49.2, fails). " ++
  "Flavor rotation from A-sector coupling needed for theta12, theta23."
```
