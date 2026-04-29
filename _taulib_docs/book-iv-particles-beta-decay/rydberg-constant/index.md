---
{
  "projection_kind": "taulib_declaration",
  "title": "RydbergConstant",
  "permalink": "/verify/taulib/docs/book-iv-particles-beta-decay/rydberg-constant/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.BetaDecay`.",
  "declaration_id": "TauLib.BookIV.Particles.BetaDecay::RydbergConstant",
  "declaration_slug": "rydberg-constant",
  "kind": "structure",
  "name": "RydbergConstant",
  "module_name": "TauLib.BookIV.Particles.BetaDecay",
  "module_url": "/verify/taulib/docs/book-iv-particles-beta-decay/",
  "source_line_start": 181,
  "source_line_end": 188,
  "registry_ids": [
    "IV.D199"
  ],
  "related_registry_items": [
    {
      "id": "IV.D199",
      "title": "Rydberg constant",
      "url": "/registry/object/IV.D199/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/BetaDecay.lean#L181-L188",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Particles.BetaDecay",
        "url": "/verify/taulib/docs/book-iv-particles-beta-decay/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/BetaDecay.lean#L181-L188",
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

- Module: [TauLib.BookIV.Particles.BetaDecay](/verify/taulib/docs/book-iv-particles-beta-decay/)
- Source path: [`TauLib/BookIV/Particles/BetaDecay.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/BetaDecay.lean#L181-L188)
- Source range: L181-L188
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D199` — Rydberg constant

## Immediate Comment / Docstring

```lean
/-- [IV.D199] R_∞ = α_em² · m_e · c / (2ℏ)
    encodes hydrogen levels: E_n = −hcR_∞/n².

    A derived quantity in Category τ since both α_em and m_e are
    ι_τ-determined. Parameter-free prediction.

    CODATA: R_∞ = 10,973,731.568157(12) m⁻¹. -/
```

## Source Excerpt

```lean
structure RydbergConstant where
  /-- CODATA value (m⁻¹, integer part). -/
  codata_int : Nat := 10973731
  /-- τ-predicted value (m⁻¹, integer part, approximate). -/
  tau_predicted_int : Nat := 10973731
  /-- Parameter-free. -/
  parameter_free : Bool := true
  deriving Repr
```
