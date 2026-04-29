---
{
  "projection_kind": "taulib_declaration",
  "title": "E4_qcoeff",
  "permalink": "/verify/taulib/docs/book-iii-spectral-confinement-bridge/e4-qcoeff/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Spectral.ConfinementBridge`.",
  "declaration_id": "TauLib.BookIII.Spectral.ConfinementBridge::E4_qcoeff",
  "declaration_slug": "e4-qcoeff",
  "kind": "def",
  "name": "E4_qcoeff",
  "module_name": "TauLib.BookIII.Spectral.ConfinementBridge",
  "module_url": "/verify/taulib/docs/book-iii-spectral-confinement-bridge/",
  "source_line_start": 226,
  "source_line_end": 226,
  "registry_ids": [
    "III.D80"
  ],
  "related_registry_items": [
    {
      "id": "III.D80",
      "title": "q-Expansion Coefficients",
      "url": "/registry/object/III.D80/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/ConfinementBridge.lean#L226-L226",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Spectral.ConfinementBridge",
        "url": "/verify/taulib/docs/book-iii-spectral-confinement-bridge/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/ConfinementBridge.lean#L226-L226",
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

- Module: [TauLib.BookIII.Spectral.ConfinementBridge](/verify/taulib/docs/book-iii-spectral-confinement-bridge/)
- Source path: [`TauLib/BookIII/Spectral/ConfinementBridge.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/ConfinementBridge.lean#L226-L226)
- Source range: L226-L226
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D80` — q-Expansion Coefficients

## Immediate Comment / Docstring

```lean
/-- [III.D80] The q-expansion coefficients that determine the residuals.
    E₄(τ) = 1 + 240·Σ σ₃(n)qⁿ
    E₆(τ) = 1 − 504·Σ σ₅(n)qⁿ

    The leading residuals at the S-dual point are:
    - E₄: +240 · q' ≈ +2.4 ppm  (positive: E₄·ι⁴ > 1)
    - E₆: −504 · q' ≈ −5.1 ppm  (negative: |E₆|·ι⁶ < 1 + correction)
    - Ratio: 744 · q' ≈ 7.5 ppm  (744 = j-invariant constant term) -/
```

## Source Excerpt

```lean
def E4_qcoeff : Int := 240
```
