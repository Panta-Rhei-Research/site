---
{
  "projection_kind": "taulib_declaration",
  "title": "InflatonNoGo",
  "permalink": "/verify/taulib/docs/book-v-cosmology-inflation-regime/inflaton-no-go/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.InflationRegime`.",
  "declaration_id": "TauLib.BookV.Cosmology.InflationRegime::InflatonNoGo",
  "declaration_slug": "inflaton-no-go",
  "kind": "structure",
  "name": "InflatonNoGo",
  "module_name": "TauLib.BookV.Cosmology.InflationRegime",
  "module_url": "/verify/taulib/docs/book-v-cosmology-inflation-regime/",
  "source_line_start": 109,
  "source_line_end": 118,
  "registry_ids": [
    "V.C17"
  ],
  "related_registry_items": [
    {
      "id": "V.C17",
      "title": "Inflaton No-Go Corollary",
      "url": "/registry/object/V.C17/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/InflationRegime.lean#L109-L118",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.InflationRegime",
        "url": "/verify/taulib/docs/book-v-cosmology-inflation-regime/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/InflationRegime.lean#L109-L118",
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

- Module: [TauLib.BookV.Cosmology.InflationRegime](/verify/taulib/docs/book-v-cosmology-inflation-regime/)
- Source path: [`TauLib/BookV/Cosmology/InflationRegime.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/InflationRegime.lean#L109-L118)
- Source range: L109-L118
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.C17` — Inflaton No-Go Corollary

## Immediate Comment / Docstring

```lean
/-- [V.C17] Inflaton no-go corollary: no inflaton field exists in
    Category τ.

    Proof: the five sectors {D,A,B,C,ω} exhaust all generator
    combinations. No sixth scalar sector can be added beyond the
    locked sector table. The inflationary behaviour is a regime
    property of the existing sectors, not a new field. -/
```

## Source Excerpt

```lean
structure InflatonNoGo where
  /-- Number of sectors (always 5). -/
  num_sectors : Nat
  /-- Exactly 5 sectors. -/
  five_sectors : num_sectors = 5
  /-- Number of exhausted generator combinations (5 = all). -/
  n_exhausted : Nat := 5
  /-- Exhaustion matches sector count. -/
  exhaustion_eq : n_exhausted = num_sectors
  deriving Repr
```
