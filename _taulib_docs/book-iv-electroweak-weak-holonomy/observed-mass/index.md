---
{
  "projection_kind": "taulib_declaration",
  "title": "ObservedMass",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-weak-holonomy/observed-mass/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.WeakHolonomy`.",
  "declaration_id": "TauLib.BookIV.Electroweak.WeakHolonomy::ObservedMass",
  "declaration_slug": "observed-mass",
  "kind": "structure",
  "name": "ObservedMass",
  "module_name": "TauLib.BookIV.Electroweak.WeakHolonomy",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-weak-holonomy/",
  "source_line_start": 178,
  "source_line_end": 186,
  "registry_ids": [
    "IV.D120"
  ],
  "related_registry_items": [
    {
      "id": "IV.D120",
      "title": "W Boson Parameters",
      "url": "/registry/object/IV.D120/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakHolonomy.lean#L178-L186",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakHolonomy.lean#L178-L186",
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
- Source path: [`TauLib/BookIV/Electroweak/WeakHolonomy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakHolonomy.lean#L178-L186)
- Source range: L178-L186
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D120` — W Boson Parameters

## Immediate Comment / Docstring

```lean
/-- [IV.D120] W boson observed mass: M_W = 80379 MeV (PDG 2022).
    Encoded as a rational pair (numer/denom) in MeV. -/
```

## Source Excerpt

```lean
structure ObservedMass where
  /-- Particle name. -/
  name : String
  /-- Mass numerator in MeV. -/
  mass_numer : Nat
  /-- Mass denominator (for sub-MeV precision). -/
  mass_denom : Nat
  denom_pos : mass_denom > 0
  deriving Repr
```
