---
{
  "projection_kind": "taulib_declaration",
  "title": "confinement_bridge_lower",
  "permalink": "/verify/taulib/docs/book-iii-spectral-confinement-bridge/confinement-bridge-lower/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Spectral.ConfinementBridge`.",
  "declaration_id": "TauLib.BookIII.Spectral.ConfinementBridge::confinement_bridge_lower",
  "declaration_slug": "confinement-bridge-lower",
  "kind": "theorem",
  "name": "confinement_bridge_lower",
  "module_name": "TauLib.BookIII.Spectral.ConfinementBridge",
  "module_url": "/verify/taulib/docs/book-iii-spectral-confinement-bridge/",
  "source_line_start": 161,
  "source_line_end": 163,
  "registry_ids": [
    "III.T54"
  ],
  "related_registry_items": [
    {
      "id": "III.T54",
      "title": "Confinement Bridge Identity",
      "url": "/registry/object/III.T54/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/ConfinementBridge.lean#L161-L163",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/ConfinementBridge.lean#L161-L163",
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
- Source path: [`TauLib/BookIII/Spectral/ConfinementBridge.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/ConfinementBridge.lean#L161-L163)
- Source range: L161-L163
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.T54` — Confinement Bridge Identity

## Immediate Comment / Docstring

```lean
/-- [III.T54] Confinement Bridge: |E₆| · κ(C;3)² ≈ 1/(1−ι_τ)² within ±10 ppm.

    This is the DIRECT form of the bridge, verified by cross-multiplication.
    By bridge_algebraic_identity, this is equivalent to E6_iota6_near_one. -/
```

## Source Excerpt

```lean
theorem confinement_bridge_lower :
    bridge_lhs_N * bridge_rhs_D * 1000000 > 999990 * bridge_lhs_D * bridge_rhs_N := by
  native_decide
```
