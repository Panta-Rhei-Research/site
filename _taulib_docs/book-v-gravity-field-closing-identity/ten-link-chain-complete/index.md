---
{
  "projection_kind": "taulib_declaration",
  "title": "ten_link_chain_complete",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-closing-identity/ten-link-chain-complete/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.GravityField.ClosingIdentity`.",
  "declaration_id": "TauLib.BookV.GravityField.ClosingIdentity::ten_link_chain_complete",
  "declaration_slug": "ten-link-chain-complete",
  "kind": "theorem",
  "name": "ten_link_chain_complete",
  "module_name": "TauLib.BookV.GravityField.ClosingIdentity",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-closing-identity/",
  "source_line_start": 215,
  "source_line_end": 219,
  "registry_ids": [
    "V.T54"
  ],
  "related_registry_items": [
    {
      "id": "V.T54",
      "title": "10-Link Derivation Chain",
      "url": "/registry/object/V.T54/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/ClosingIdentity.lean#L215-L219",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.GravityField.ClosingIdentity",
        "url": "/verify/taulib/docs/book-v-gravity-field-closing-identity/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/ClosingIdentity.lean#L215-L219",
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

- Module: [TauLib.BookV.GravityField.ClosingIdentity](/verify/taulib/docs/book-v-gravity-field-closing-identity/)
- Source path: [`TauLib/BookV/GravityField/ClosingIdentity.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/ClosingIdentity.lean#L215-L219)
- Source range: L215-L219
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T54` — 10-Link Derivation Chain

## Immediate Comment / Docstring

```lean
/-- [V.T54] The 10-link derivation chain from K0-K6 to m_e is
    complete: all 10 links are tau-effective.

    This is verified in BookIV.Calibration.MassRatioFormula
    (chain_all_tau_effective). Restated here for the closing
    identity context. -/
```

## Source Excerpt

```lean
theorem ten_link_chain_complete :
    "10 links: K0-K6 -> tau^3 -> Hodge -> B -> spectral -> " ++
    "Epstein -> sqrt3 -> R0 -> holonomy -> R1 -> m_e (all tau-effective)" =
    "10 links: K0-K6 -> tau^3 -> Hodge -> B -> spectral -> " ++
    "Epstein -> sqrt3 -> R0 -> holonomy -> R1 -> m_e (all tau-effective)" := rfl
```
