---
{
  "projection_kind": "taulib_declaration",
  "title": "tau_arithmetic_is_address_resolution",
  "permalink": "/verify/taulib/docs/book-i-addressability-address-resolution/tau-arithmetic-is-address-resolution/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Addressability.AddressResolution`.",
  "declaration_id": "TauLib.BookI.Addressability.AddressResolution::tau_arithmetic_is_address_resolution",
  "declaration_slug": "tau-arithmetic-is-address-resolution",
  "kind": "theorem",
  "name": "tau_arithmetic_is_address_resolution",
  "module_name": "TauLib.BookI.Addressability.AddressResolution",
  "module_url": "/verify/taulib/docs/book-i-addressability-address-resolution/",
  "source_line_start": 137,
  "source_line_end": 143,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Addressability/AddressResolution.lean#L137-L143",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Addressability.AddressResolution",
        "url": "/verify/taulib/docs/book-i-addressability-address-resolution/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Addressability/AddressResolution.lean#L137-L143",
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

- Module: [TauLib.BookI.Addressability.AddressResolution](/verify/taulib/docs/book-i-addressability-address-resolution/)
- Source path: [`TauLib/BookI/Addressability/AddressResolution.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Addressability/AddressResolution.lean#L137-L143)
- Source range: L137-L143
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Corollary** (Category τ has no equations in the classical sense):
    every claim "a equals b in Category τ" is an *operational*
    address-resolution claim — finitely-witnessed NF comparison.

    This is the meta-logical content of the H7 address-resolution
    paradigm: classical equational reasoning emerges as the
    extensional shadow of NF address-resolution. -/
```

## Source Excerpt

```lean
theorem tau_arithmetic_is_address_resolution :
    ∀ (a b : Program),
      tauEq a b
        ↔ ((normalize a).rhoCount = (normalize b).rhoCount
           ∧ seedAgree (normalize a).seedMap (normalize b).seedMap) := by
  intro a b
  rfl
```
