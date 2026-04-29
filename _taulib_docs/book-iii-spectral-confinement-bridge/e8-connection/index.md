---
{
  "projection_kind": "taulib_declaration",
  "title": "e8_connection",
  "permalink": "/verify/taulib/docs/book-iii-spectral-confinement-bridge/e8-connection/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Spectral.ConfinementBridge`.",
  "declaration_id": "TauLib.BookIII.Spectral.ConfinementBridge::e8_connection",
  "declaration_slug": "e8-connection",
  "kind": "theorem",
  "name": "e8_connection",
  "module_name": "TauLib.BookIII.Spectral.ConfinementBridge",
  "module_url": "/verify/taulib/docs/book-iii-spectral-confinement-bridge/",
  "source_line_start": 233,
  "source_line_end": 257,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/ConfinementBridge.lean#L233-L257",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/ConfinementBridge.lean#L233-L257",
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
- Source path: [`TauLib/BookIII/Spectral/ConfinementBridge.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/ConfinementBridge.lean#L233-L257)
- Source range: L233-L257
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- 744 = dim(E₈ roots) + 504: the E₈ connection. -/
```

## Source Excerpt

```lean
theorem e8_connection : (240 : Nat) + 504 = 744 := ratio_coeff_is_744

-- ============================================================
-- OQ.07 + OQ.09 RESOLUTION SUMMARY
-- ============================================================

/-!
## Resolution of OQ.07 and OQ.09

**OQ.07 (C-sector/SU(3) bridge):** RESOLVED.
  The confinement bridge E₆·κ(C;3)² ≈ −1/(1−ι)² holds at ±10 ppm
  (confinement_bridge). It reduces to the E₆ near-identity by pure
  algebra (bridge_algebraic_identity).

**OQ.09 (E₄/E₆ fixed point):** RESOLVED.
  The S-duality transport (sduality_E4_sign_positive, sduality_E6_sign_negative)
  provides the structural explanation:
  - E₄·ι⁴ = 1 + 240q' (positive sign from i⁴ = 1)
  - E₆·ι⁶ = −1 + 504q' (negative sign from i⁶ = −1)
  - Residuals are exponentially suppressed (q' ≈ 10⁻⁸)

**Status upgrade:** Both OQ.07 and OQ.09 move from OPEN → τ-EFFECTIVE.
  The S-duality transport is an EXACT modular identity (not conjectural).
  The residual is controlled by q' < e^{−18} (sdual_exponent_large).
-/
```
