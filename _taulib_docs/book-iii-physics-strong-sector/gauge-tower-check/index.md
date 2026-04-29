---
{
  "projection_kind": "taulib_declaration",
  "title": "gauge_tower_check",
  "permalink": "/verify/taulib/docs/book-iii-physics-strong-sector/gauge-tower-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Physics.StrongSector`.",
  "declaration_id": "TauLib.BookIII.Physics.StrongSector::gauge_tower_check",
  "declaration_slug": "gauge-tower-check",
  "kind": "def",
  "name": "gauge_tower_check",
  "module_name": "TauLib.BookIII.Physics.StrongSector",
  "module_url": "/verify/taulib/docs/book-iii-physics-strong-sector/",
  "source_line_start": 131,
  "source_line_end": 149,
  "registry_ids": [
    "III.D44"
  ],
  "related_registry_items": [
    {
      "id": "III.D44",
      "title": "τ-Admissible Gauge Data",
      "url": "/registry/object/III.D44/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/StrongSector.lean#L131-L149",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Physics.StrongSector",
        "url": "/verify/taulib/docs/book-iii-physics-strong-sector/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/StrongSector.lean#L131-L149",
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

- Module: [TauLib.BookIII.Physics.StrongSector](/verify/taulib/docs/book-iii-physics-strong-sector/)
- Source path: [`TauLib/BookIII/Physics/StrongSector.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/StrongSector.lean#L131-L149)
- Source range: L131-L149
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D44` — τ-Admissible Gauge Data

## Immediate Comment / Docstring

```lean
/-- [III.D44] Gauge tower compatibility: gauge data at k extends to k+1
    (products divide). -/
```

## Source Excerpt

```lean
def gauge_tower_check (db : TauIdx) : Bool :=
  go 1 (db + 1)
where
  go (k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k >= db then true
    else
      let gd_k := gauge_data_at k
      let gd_k1 := gauge_data_at (k + 1)
      -- B-product at k divides B-product at k+1
      let b_div := if gd_k.b_product > 0 then
        gd_k1.b_product % gd_k.b_product == 0
      else true
      -- C-product at k divides C-product at k+1
      let c_div := if gd_k.c_product > 0 then
        gd_k1.c_product % gd_k.c_product == 0
      else true
      b_div && c_div && go (k + 1) (fuel - 1)
  termination_by fuel
```
