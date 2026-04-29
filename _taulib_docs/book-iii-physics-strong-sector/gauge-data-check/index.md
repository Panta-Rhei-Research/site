---
{
  "projection_kind": "taulib_declaration",
  "title": "gauge_data_check",
  "permalink": "/verify/taulib/docs/book-iii-physics-strong-sector/gauge-data-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Physics.StrongSector`.",
  "declaration_id": "TauLib.BookIII.Physics.StrongSector::gauge_data_check",
  "declaration_slug": "gauge-data-check",
  "kind": "def",
  "name": "gauge_data_check",
  "module_name": "TauLib.BookIII.Physics.StrongSector",
  "module_url": "/verify/taulib/docs/book-iii-physics-strong-sector/",
  "source_line_start": 111,
  "source_line_end": 127,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/StrongSector.lean#L111-L127",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/StrongSector.lean#L111-L127",
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
- Source path: [`TauLib/BookIII/Physics/StrongSector.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/StrongSector.lean#L111-L127)
- Source range: L111-L127
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D44` — τ-Admissible Gauge Data

## Immediate Comment / Docstring

```lean
/-- [III.D44] Gauge data check: products are consistent, counts match
    the number of primes, and gauge data at k is compatible with k+1. -/
```

## Source Excerpt

```lean
def gauge_data_check (db : TauIdx) : Bool :=
  go 1 (db + 1)
where
  go (k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k > db then true
    else
      let gd := gauge_data_at k
      let pk := primorial k
      -- Product completeness: B * C * X = Prim(k)
      let complete := if pk > 0 then
        gd.b_product * gd.c_product * gd.x_product == pk
      else true
      -- Count completeness: b_ct + c_ct + x_ct = k (number of primes)
      let count_ok := gd.b_count + gd.c_count + gd.x_count == k
      complete && count_ok && go (k + 1) (fuel - 1)
  termination_by fuel
```
