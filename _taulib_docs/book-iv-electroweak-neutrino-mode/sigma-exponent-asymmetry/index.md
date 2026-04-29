---
{
  "projection_kind": "taulib_declaration",
  "title": "SigmaExponentAsymmetry",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/sigma-exponent-asymmetry/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.NeutrinoMode`.",
  "declaration_id": "TauLib.BookIV.Electroweak.NeutrinoMode::SigmaExponentAsymmetry",
  "declaration_slug": "sigma-exponent-asymmetry",
  "kind": "structure",
  "name": "SigmaExponentAsymmetry",
  "module_name": "TauLib.BookIV.Electroweak.NeutrinoMode",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/",
  "source_line_start": 639,
  "source_line_end": 648,
  "registry_ids": [
    "V.P128"
  ],
  "related_registry_items": [
    {
      "id": "V.P128",
      "title": "Asymmetry in sigma-Exponents: Delta_pq - Delta_pr approx 2/13 (CF-structural candidate)",
      "url": "/registry/object/V.P128/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L639-L648",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L639-L648",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
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
- Source path: [`TauLib/BookIV/Electroweak/NeutrinoMode.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L639-L648)
- Source range: L639-L648
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.P128` — Asymmetry in sigma-Exponents: Delta_pq - Delta_pr approx 2/13 (CF-structural candidate)

## Immediate Comment / Docstring

```lean
/-- [V.P128] Asymmetry δ = Δpq - Δpr = 0.29 empirical.
    CF candidate: δ_CF = 2/a₂ = 2/13 ≈ 0.154 (underestimates by ×2, conjectural). -/
```

## Source Excerpt

```lean
structure SigmaExponentAsymmetry where
  /-- CF coefficient a₂ = 13 from CF(ι_τ⁻¹) = [2;1,13,3,...]. -/
  cf_coefficient : Nat := 13
  /-- Numerator of CF candidate: 2/a₂. -/
  asymmetry_numerator : Nat := 2
  /-- Asymmetry is CF-structural (from continued fraction). -/
  is_cf_structural : Bool := true
  /-- CF candidate is approximate (2/13 ≈ 0.154 vs empirical 0.29). -/
  cf_approximate : Bool := true
  deriving Repr
```
