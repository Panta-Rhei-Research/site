---
{
  "projection_kind": "taulib_declaration",
  "title": "WeakFineStructure",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-weak-holonomy/weak-fine-structure/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.WeakHolonomy`.",
  "declaration_id": "TauLib.BookIV.Electroweak.WeakHolonomy::WeakFineStructure",
  "declaration_slug": "weak-fine-structure",
  "kind": "structure",
  "name": "WeakFineStructure",
  "module_name": "TauLib.BookIV.Electroweak.WeakHolonomy",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-weak-holonomy/",
  "source_line_start": 218,
  "source_line_end": 224,
  "registry_ids": [
    "IV.T53"
  ],
  "related_registry_items": [
    {
      "id": "IV.T53",
      "title": "Weak Coupling from Sector Parameters",
      "url": "/registry/object/IV.T53/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakHolonomy.lean#L218-L224",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakHolonomy.lean#L218-L224",
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
- Source path: [`TauLib/BookIV/Electroweak/WeakHolonomy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakHolonomy.lean#L218-L224)
- Source range: L218-L224
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.T53` — Weak Coupling from Sector Parameters

## Immediate Comment / Docstring

```lean
/-- [IV.T53] Weak fine-structure constant alpha_wk: the A-sector
    self-coupling kappa(A;1) = iota_tau determines the weak coupling.
    alpha_wk = kappa(A;1)^2 / (4*pi) at leading order.
    We record alpha_wk as a scaled rational. -/
```

## Source Excerpt

```lean
structure WeakFineStructure where
  /-- Numerator (iota_tau squared, scaled). -/
  numer : Nat
  /-- Denominator (4*pi*denom^2, approximated). -/
  denom : Nat
  denom_pos : denom > 0
  deriving Repr
```
