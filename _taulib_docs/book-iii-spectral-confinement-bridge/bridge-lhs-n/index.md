---
{
  "projection_kind": "taulib_declaration",
  "title": "bridge_lhs_N",
  "permalink": "/verify/taulib/docs/book-iii-spectral-confinement-bridge/bridge-lhs-n/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Spectral.ConfinementBridge`.",
  "declaration_id": "TauLib.BookIII.Spectral.ConfinementBridge::bridge_lhs_N",
  "declaration_slug": "bridge-lhs-n",
  "kind": "def",
  "name": "bridge_lhs_N",
  "module_name": "TauLib.BookIII.Spectral.ConfinementBridge",
  "module_url": "/verify/taulib/docs/book-iii-spectral-confinement-bridge/",
  "source_line_start": 149,
  "source_line_end": 149,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/ConfinementBridge.lean#L149-L149",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/ConfinementBridge.lean#L149-L149",
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
- Source path: [`TauLib/BookIII/Spectral/ConfinementBridge.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/ConfinementBridge.lean#L149-L149)
- Source range: L149-L149
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Bridge LHS numerator: |E₆| · κ(C;3)² numerator. -/
```

## Source Excerpt

```lean
private def bridge_lhs_N : Nat := E6_abs_numer * kappa_CC.numer * kappa_CC.numer
```
