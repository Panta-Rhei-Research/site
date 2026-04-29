---
{
  "projection_kind": "taulib_declaration",
  "title": "passage_count",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-exponent-derivation/passage-count/",
  "summary_short": "`def` declaration in `TauLib.BookV.GravityField.ExponentDerivation`.",
  "declaration_id": "TauLib.BookV.GravityField.ExponentDerivation::passage_count",
  "declaration_slug": "passage-count",
  "kind": "def",
  "name": "passage_count",
  "module_name": "TauLib.BookV.GravityField.ExponentDerivation",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-exponent-derivation/",
  "source_line_start": 169,
  "source_line_end": 169,
  "registry_ids": [
    "V.T82"
  ],
  "related_registry_items": [
    {
      "id": "V.T82",
      "title": "Kepler's First Law --- V.T34",
      "url": "/registry/object/V.T82/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/ExponentDerivation.lean#L169-L169",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.GravityField.ExponentDerivation",
        "url": "/verify/taulib/docs/book-v-gravity-field-exponent-derivation/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/ExponentDerivation.lean#L169-L169",
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

- Module: [TauLib.BookV.GravityField.ExponentDerivation](/verify/taulib/docs/book-v-gravity-field-exponent-derivation/)
- Source path: [`TauLib/BookV/GravityField/ExponentDerivation.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/ExponentDerivation.lean#L169-L169)
- Source range: L169-L169
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `V.T82` — Kepler's First Law --- V.T34

## Immediate Comment / Docstring

```lean
/-- [V.T82] The 18 holonomy passages through the boundary algebra.

    Structure: 2 fiber cycles × 3 layers × 3 solenoidal winding modes.

    Each passage contributes one factor of α (EM boundary coupling).
    Total: α^18.

    The Feynman vertex picture: 36 = 2 × 18 vertices (two per passage),
    each contributing √α, giving (√α)^36 = α^18. -/
```

## Source Excerpt

```lean
def passage_count : Nat := canonical_factors.product
```
