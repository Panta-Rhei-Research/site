---
{
  "projection_kind": "taulib_declaration",
  "title": "OpeningRegime",
  "permalink": "/verify/taulib/docs/book-v-temporal-high-energy/opening-regime/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Temporal.HighEnergy`.",
  "declaration_id": "TauLib.BookV.Temporal.HighEnergy::OpeningRegime",
  "declaration_slug": "opening-regime",
  "kind": "structure",
  "name": "OpeningRegime",
  "module_name": "TauLib.BookV.Temporal.HighEnergy",
  "module_url": "/verify/taulib/docs/book-v-temporal-high-energy/",
  "source_line_start": 124,
  "source_line_end": 133,
  "registry_ids": [
    "V.D25"
  ],
  "related_registry_items": [
    {
      "id": "V.D25",
      "title": "Opening Regime",
      "url": "/registry/object/V.D25/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/HighEnergy.lean#L124-L133",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Temporal.HighEnergy",
        "url": "/verify/taulib/docs/book-v-temporal-high-energy/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/HighEnergy.lean#L124-L133",
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

- Module: [TauLib.BookV.Temporal.HighEnergy](/verify/taulib/docs/book-v-temporal-high-energy/)
- Source path: [`TauLib/BookV/Temporal/HighEnergy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/HighEnergy.lean#L124-L133)
- Source range: L124-L133
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D25` — Opening Regime

## Immediate Comment / Docstring

```lean
/-- [V.D25] Opening regime interval: [n_ign, n_open) — the period of
    rapid equilibration between sectors.

    Characteristics:
    - All 5 sectors present but near-maximally coupled
    - Refinement progression rate is high (rapid advance)
    - τ-Einstein equation has unique solution at each depth
    - Corresponds to inflationary / GUT epoch in orthodox cosmology -/
```

## Source Excerpt

```lean
structure OpeningRegime where
  /-- Start of the opening regime (ignition depth). -/
  n_start : Nat
  /-- End of the opening regime (opening depth). -/
  n_end : Nat
  /-- Start is positive. -/
  start_pos : n_start > 0
  /-- Regime is nonempty (end > start). -/
  nonempty : n_end > n_start
  deriving Repr
```
