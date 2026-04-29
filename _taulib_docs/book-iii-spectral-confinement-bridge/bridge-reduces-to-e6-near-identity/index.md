---
{
  "projection_kind": "taulib_declaration",
  "title": "bridge_reduces_to_E6_near_identity",
  "permalink": "/verify/taulib/docs/book-iii-spectral-confinement-bridge/bridge-reduces-to-e6-near-identity/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Spectral.ConfinementBridge`.",
  "declaration_id": "TauLib.BookIII.Spectral.ConfinementBridge::bridge_reduces_to_E6_near_identity",
  "declaration_slug": "bridge-reduces-to-e6-near-identity",
  "kind": "theorem",
  "name": "bridge_reduces_to_E6_near_identity",
  "module_name": "TauLib.BookIII.Spectral.ConfinementBridge",
  "module_url": "/verify/taulib/docs/book-iii-spectral-confinement-bridge/",
  "source_line_start": 125,
  "source_line_end": 146,
  "registry_ids": [
    "III.P32",
    "III.T53"
  ],
  "related_registry_items": [
    {
      "id": "III.P32",
      "title": "Bridge Algebraic Reduction",
      "url": "/registry/object/III.P32/"
    },
    {
      "id": "III.T53",
      "title": "Universal Admissibility Theorem",
      "url": "/registry/object/III.T53/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/ConfinementBridge.lean#L125-L146",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/ConfinementBridge.lean#L125-L146",
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
- Source path: [`TauLib/BookIII/Spectral/ConfinementBridge.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/ConfinementBridge.lean#L125-L146)
- Source range: L125-L146
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.P32` — Bridge Algebraic Reduction
- `III.T53` — Universal Admissibility Theorem

## Immediate Comment / Docstring

```lean
/-- [III.P32] Corollary: the bridge near-identity inherits its bounds
    directly from the E₆ near-identity (III.T51).

    Since |E₆|·κ(C;3)²·(1−ι)² = |E₆|·ι⁶ by bridge_algebraic_identity,
    and |E₆|·ι⁶ ∈ (0.999990, 1.000010) by E6_iota6_near_one,
    the confinement bridge holds at the same precision (±10 ppm). -/
```

## Source Excerpt

```lean
theorem bridge_reduces_to_E6_near_identity :
    -- The E₆ near-identity gives us the bridge for free
    E6_abs_numer * i6N * 1000000 > 999990 * E6_abs_denom * i6D ∧
    E6_abs_numer * i6N * 1000000 < 1000010 * E6_abs_denom * i6D :=
  E6_iota6_near_one

-- ============================================================
-- CONFINEMENT BRIDGE DIRECT VERIFICATION [III.T53]
-- ============================================================

/-! We also verify the bridge DIRECTLY, without factoring through the
    E₆ near-identity. This serves as an independent cross-check.

    Bridge claim: |E₆| · κ(C;3)² ≈ 1/(1−ι)²

    LHS numerator: E6_abs_numer · kappa_CC.numer²
    LHS denominator: E6_abs_denom · kappa_CC.denom²

    RHS = 1/(1−ι)² = D²/(D−ι)²

    Cross-multiplied: E6_abs_numer · kappa_CC.numer² · (D−ι)² ≈ E6_abs_denom · kappa_CC.denom² · D²
    within ±10 ppm. -/
```
