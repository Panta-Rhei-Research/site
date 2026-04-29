---
{
  "projection_kind": "taulib_declaration",
  "title": "FermiConstant",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-weak-holonomy/fermi-constant/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.WeakHolonomy`.",
  "declaration_id": "TauLib.BookIV.Electroweak.WeakHolonomy::FermiConstant",
  "declaration_slug": "fermi-constant",
  "kind": "structure",
  "name": "FermiConstant",
  "module_name": "TauLib.BookIV.Electroweak.WeakHolonomy",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-weak-holonomy/",
  "source_line_start": 266,
  "source_line_end": 272,
  "registry_ids": [
    "IV.P57"
  ],
  "related_registry_items": [
    {
      "id": "IV.P57",
      "title": "Fermi Constant from Weak Coupling",
      "url": "/registry/object/IV.P57/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakHolonomy.lean#L266-L272",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.WeakHolonomy",
        "url": "/verify/taulib/docs/book-iv-electroweak-weak-holonomy/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakHolonomy.lean#L266-L272",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
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

- Module: [TauLib.BookIV.Electroweak.WeakHolonomy](/verify/taulib/docs/book-iv-electroweak-weak-holonomy/)
- Source path: [`TauLib/BookIV/Electroweak/WeakHolonomy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakHolonomy.lean#L266-L272)
- Source range: L266-L272
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P57` — Fermi Constant from Weak Coupling

## Immediate Comment / Docstring

```lean
/-- [IV.P57] The Fermi constant G_F arises from W exchange at low energy:
    G_F / sqrt(2) = g_wk^2 / (8 * M_W^2).
    G_F = 1.1663788 * 10^-5 GeV^-2.
    Encoded as scaled Nat pair. -/
```

## Source Excerpt

```lean
structure FermiConstant where
  /-- G_F numerator (scaled to 10^11). -/
  numer : Nat
  /-- G_F denominator. -/
  denom : Nat
  denom_pos : denom > 0
  deriving Repr
```
