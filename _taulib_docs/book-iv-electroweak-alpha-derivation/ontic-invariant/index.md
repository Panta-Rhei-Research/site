---
{
  "projection_kind": "taulib_declaration",
  "title": "OnticInvariant",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-alpha-derivation/ontic-invariant/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.AlphaDerivation`.",
  "declaration_id": "TauLib.BookIV.Electroweak.AlphaDerivation::OnticInvariant",
  "declaration_slug": "ontic-invariant",
  "kind": "structure",
  "name": "OnticInvariant",
  "module_name": "TauLib.BookIV.Electroweak.AlphaDerivation",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-alpha-derivation/",
  "source_line_start": 198,
  "source_line_end": 206,
  "registry_ids": [
    "IV.T50"
  ],
  "related_registry_items": [
    {
      "id": "IV.T50",
      "title": "No-Running Principle for alpha_em",
      "url": "/registry/object/IV.T50/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L198-L206",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.AlphaDerivation",
        "url": "/verify/taulib/docs/book-iv-electroweak-alpha-derivation/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L198-L206",
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

- Module: [TauLib.BookIV.Electroweak.AlphaDerivation](/verify/taulib/docs/book-iv-electroweak-alpha-derivation/)
- Source path: [`TauLib/BookIV/Electroweak/AlphaDerivation.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L198-L206)
- Source range: L198-L206
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.T50` — No-Running Principle for alpha_em

## Immediate Comment / Docstring

```lean
/-- [IV.T50] α_τ is an ontic invariant: it depends only on ι_τ and
    geometric constants (π, e). It is NOT a free parameter of the
    theory. The value 1/137.036... is structurally determined. -/
```

## Source Excerpt

```lean
structure OnticInvariant where
  /-- Depends only on ι_τ. -/
  depends_on_iota : Bool := true
  /-- No free parameters. -/
  free_parameters : Nat
  free_eq : free_parameters = 0
  /-- Structurally determined (not tuned). -/
  structurally_determined : Bool := true
  deriving Repr
```
