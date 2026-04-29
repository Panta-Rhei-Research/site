---
{
  "projection_kind": "taulib_declaration",
  "title": "bridge_algebraic_identity",
  "permalink": "/verify/taulib/docs/book-iii-spectral-confinement-bridge/bridge-algebraic-identity/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Spectral.ConfinementBridge`.",
  "declaration_id": "TauLib.BookIII.Spectral.ConfinementBridge::bridge_algebraic_identity",
  "declaration_slug": "bridge-algebraic-identity",
  "kind": "theorem",
  "name": "bridge_algebraic_identity",
  "module_name": "TauLib.BookIII.Spectral.ConfinementBridge",
  "module_url": "/verify/taulib/docs/book-iii-spectral-confinement-bridge/",
  "source_line_start": 105,
  "source_line_end": 117,
  "registry_ids": [
    "III.P32"
  ],
  "related_registry_items": [
    {
      "id": "III.P32",
      "title": "Bridge Algebraic Reduction",
      "url": "/registry/object/III.P32/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/ConfinementBridge.lean#L105-L117",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/ConfinementBridge.lean#L105-L117",
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

- Module: [TauLib.BookIII.Spectral.ConfinementBridge](/verify/taulib/docs/book-iii-spectral-confinement-bridge/)
- Source path: [`TauLib/BookIII/Spectral/ConfinementBridge.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/ConfinementBridge.lean#L105-L117)
- Source range: L105-L117
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.P32` — Bridge Algebraic Reduction

## Immediate Comment / Docstring

```lean
/-- [III.P32] The confinement bridge reduces to the E₆ near-identity.

    Algebraically: |E₆|·κ(C;3)²·(1−ι)² = |E₆|·ι⁶.
    Since κ(C;3)² numerator = (ι³·D)² and κ(C;3)² denominator = (D³·(D−ι))²,
    we have κ(C;3)²·(1−ι)² = ι⁶/D⁶ × D²/(D−ι)² × (D−ι)²/D² = ι⁶/D⁶.

    Cross-multiplied verification:
    kappa_CC.numer² · (D−ι)² · D⁶ = ι⁶ · kappa_CC.denom² · D² -/
```

## Source Excerpt

```lean
theorem bridge_algebraic_identity :
    -- κ(C;3).numer = ι³ · D,  κ(C;3).denom = D³ · (D−ι)
    -- κ(C;3)² · (D−ι)² / D² = ι⁶ / D⁶
    -- Equivalently: κ(C;3).numer² · (D−ι)² · D⁶ = ι⁶ · D² · κ(C;3).denom²
    -- But we verify a simpler form: the product |E₆|·κ²·(1−ι)² equals |E₆|·ι⁶
    -- which just means κ² · (1−ι)² = ι⁶ (up to denominator normalization)
    -- i.e., kappa_CC.numer² · oneMinusIota² · i6D = i6N · kappa_CC.denom²
    -- where i6N = ι⁶, i6D = D⁶
    -- Note: oneMinusIota = D − ι, and we need (D−ι)² as Nat
    kappa_CC.numer * kappa_CC.numer * (iotaD - iota) * (iotaD - iota) *
      iota_sixth_denom =
    iota_sixth_numer * kappa_CC.denom * kappa_CC.denom * iotaD * iotaD := by
  native_decide
```
