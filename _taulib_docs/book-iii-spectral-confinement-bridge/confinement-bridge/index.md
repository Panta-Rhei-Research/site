---
{
  "projection_kind": "taulib_declaration",
  "title": "confinement_bridge",
  "permalink": "/verify/taulib/docs/book-iii-spectral-confinement-bridge/confinement-bridge/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Spectral.ConfinementBridge`.",
  "declaration_id": "TauLib.BookIII.Spectral.ConfinementBridge::confinement_bridge",
  "declaration_slug": "confinement-bridge",
  "kind": "theorem",
  "name": "confinement_bridge",
  "module_name": "TauLib.BookIII.Spectral.ConfinementBridge",
  "module_url": "/verify/taulib/docs/book-iii-spectral-confinement-bridge/",
  "source_line_start": 169,
  "source_line_end": 185,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/ConfinementBridge.lean#L169-L185",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/ConfinementBridge.lean#L169-L185",
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
- Source path: [`TauLib/BookIII/Spectral/ConfinementBridge.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/ConfinementBridge.lean#L169-L185)
- Source range: L169-L185
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.T54` — Confinement Bridge Identity

## Immediate Comment / Docstring

```lean
No immediate Lean doc/comment block was detected for this declaration.
```

## Source Excerpt

```lean
theorem confinement_bridge :
    bridge_lhs_N * bridge_rhs_D * 1000000 > 999990 * bridge_lhs_D * bridge_rhs_N ∧
    bridge_lhs_N * bridge_rhs_D * 1000000 < 1000010 * bridge_lhs_D * bridge_rhs_N :=
  ⟨confinement_bridge_lower, confinement_bridge_upper⟩

-- ============================================================
-- S-DUALITY TRANSPORT [III.T54]
-- ============================================================

/-! The S-duality transport explains WHY the near-identities hold.

    Key quantity: the S-dual nome q' = e^{−2π/ι_τ} ≈ 10⁻⁸.

    Since ι_τ = 341304/10⁶ < 1, the S-dual point i/ι_τ has large
    imaginary part (≈ 2.93), making q' exponentially small.

    We verify: 2π/ι_τ > 18 (so q' < e^{−18} < 1.6×10⁻⁸). -/
```
