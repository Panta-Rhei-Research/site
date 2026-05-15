---
{
  "projection_kind": "taulib_declaration",
  "title": "parity_bridge_check",
  "permalink": "/corpus/taulib/docs/book-iii-sectors-parity-bridge/parity-bridge-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Sectors.ParityBridge`.",
  "declaration_id": "TauLib.BookIII.Sectors.ParityBridge::parity_bridge_check",
  "declaration_slug": "parity-bridge-check",
  "kind": "def",
  "name": "parity_bridge_check",
  "module_name": "TauLib.BookIII.Sectors.ParityBridge",
  "module_url": "/corpus/taulib/docs/book-iii-sectors-parity-bridge/",
  "source_line_start": 39,
  "source_line_end": 46,
  "registry_ids": [
    "III.T07"
  ],
  "related_registry_items": [
    {
      "id": "III.T07",
      "title": "Parity Bridge Theorem",
      "url": "/registry/object/III.T07/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Sectors/ParityBridge.lean#L39-L46",
  "formal_status": "defined",
  "declaration_role": "data/computed value",
  "formal_status_label": "data/computed value",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Sectors.ParityBridge",
        "url": "/corpus/taulib/docs/book-iii-sectors-parity-bridge/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Sectors/ParityBridge.lean#L39-L46",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "role": "data/computed value",
      "status": "data/computed value"
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

- Module: [TauLib.BookIII.Sectors.ParityBridge](/corpus/taulib/docs/book-iii-sectors-parity-bridge/)
- Source path: [`TauLib/BookIII/Sectors/ParityBridge.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Sectors/ParityBridge.lean#L39-L46)
- Source range: L39-L46
- Kind: `def`
- Public role: `data/computed value`
- Formal status hint: `data/computed value`

## Registry Links

- `III.T07` — Parity Bridge Theorem

## Immediate Comment / Docstring

```lean
/-- [III.T07] Parity Bridge check: the A-sector (π-generator) is the
    unique primitive sector with balanced spectral polarity, enabling
    the E₁→E₂ transition (physics → computation). -/
```

## Source Excerpt

```lean
def parity_bridge_check (bound db : TauIdx) : Bool :=
  -- Condition 1: A-sector is balanced (unique)
  balanced_uniqueness_check bound &&
  -- Condition 2: E₁→E₂ enrichment functor check passes
  enrichment_functor_check .E1 bound db &&
  -- Condition 3: E₂ layer is valid and non-empty
  layer_valid_at .E2 bound db &&
  existence_checker .E2 bound db
```
