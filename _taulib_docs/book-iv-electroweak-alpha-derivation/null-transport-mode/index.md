---
{
  "projection_kind": "taulib_declaration",
  "title": "NullTransportMode",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-alpha-derivation/null-transport-mode/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.AlphaDerivation`.",
  "declaration_id": "TauLib.BookIV.Electroweak.AlphaDerivation::NullTransportMode",
  "declaration_slug": "null-transport-mode",
  "kind": "structure",
  "name": "NullTransportMode",
  "module_name": "TauLib.BookIV.Electroweak.AlphaDerivation",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-alpha-derivation/",
  "source_line_start": 108,
  "source_line_end": 117,
  "registry_ids": [
    "IV.D105"
  ],
  "related_registry_items": [
    {
      "id": "IV.D105",
      "title": "Null Transport Mode",
      "url": "/registry/object/IV.D105/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L108-L117",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L108-L117",
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
- Source path: [`TauLib/BookIV/Electroweak/AlphaDerivation.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L108-L117)
- Source range: L108-L117
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D105` — Null Transport Mode

## Immediate Comment / Docstring

```lean
/-- [IV.D105] Null transport mode on τ¹: a mode with zero fiber
    obstruction that propagates purely along the base τ¹ at speed c.
    The photon is the B-sector null transport mode. -/
```

## Source Excerpt

```lean
structure NullTransportMode where
  /-- Propagation is along base τ¹ only. -/
  base_only : Bool := true
  /-- Fiber character is degenerate (0,0). -/
  fiber_degenerate : Bool := true
  /-- Speed equals c (base propagation speed). -/
  speed_is_c : Bool := true
  /-- Associated sector. -/
  sector : Sector
  deriving Repr
```
