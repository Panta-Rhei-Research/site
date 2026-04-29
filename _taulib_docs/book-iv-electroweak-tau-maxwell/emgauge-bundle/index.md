---
{
  "projection_kind": "taulib_declaration",
  "title": "EMGaugeBundle",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/emgauge-bundle/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.TauMaxwell`.",
  "declaration_id": "TauLib.BookIV.Electroweak.TauMaxwell::EMGaugeBundle",
  "declaration_slug": "emgauge-bundle",
  "kind": "structure",
  "name": "EMGaugeBundle",
  "module_name": "TauLib.BookIV.Electroweak.TauMaxwell",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/",
  "source_line_start": 71,
  "source_line_end": 81,
  "registry_ids": [
    "IV.D98"
  ],
  "related_registry_items": [
    {
      "id": "IV.D98",
      "title": "EM Gauge Bundle",
      "url": "/registry/object/IV.D98/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauMaxwell.lean#L71-L81",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.TauMaxwell",
        "url": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauMaxwell.lean#L71-L81",
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

- Module: [TauLib.BookIV.Electroweak.TauMaxwell](/verify/taulib/docs/book-iv-electroweak-tau-maxwell/)
- Source path: [`TauLib/BookIV/Electroweak/TauMaxwell.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauMaxwell.lean#L71-L81)
- Source range: L71-L81
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D98` — EM Gauge Bundle

## Immediate Comment / Docstring

```lean
/-- [IV.D98] The EM gauge bundle: specialization of EMPrincipalBundle
    to the physical B-sector with U(1) structure group and T² base. -/
```

## Source Excerpt

```lean
structure EMGaugeBundle where
  /-- Structure group is U(1). -/
  group_is_u1 : Bool := true
  /-- Base is T². -/
  base_is_torus : Bool := true
  /-- Sector is B (EM). -/
  sector : Sector
  sector_eq : sector = .B
  /-- Chern class (integer topological invariant). -/
  chern_class : Int
  deriving Repr
```
