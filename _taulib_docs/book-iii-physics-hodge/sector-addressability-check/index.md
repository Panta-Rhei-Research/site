---
{
  "projection_kind": "taulib_declaration",
  "title": "sector_addressability_check",
  "permalink": "/verify/taulib/docs/book-iii-physics-hodge/sector-addressability-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Physics.Hodge`.",
  "declaration_id": "TauLib.BookIII.Physics.Hodge::sector_addressability_check",
  "declaration_slug": "sector-addressability-check",
  "kind": "def",
  "name": "sector_addressability_check",
  "module_name": "TauLib.BookIII.Physics.Hodge",
  "module_url": "/verify/taulib/docs/book-iii-physics-hodge/",
  "source_line_start": 115,
  "source_line_end": 130,
  "registry_ids": [
    "III.D48"
  ],
  "related_registry_items": [
    {
      "id": "III.D48",
      "title": "Sector Addressability",
      "url": "/registry/object/III.D48/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/Hodge.lean#L115-L130",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Physics.Hodge",
        "url": "/verify/taulib/docs/book-iii-physics-hodge/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/Hodge.lean#L115-L130",
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

- Module: [TauLib.BookIII.Physics.Hodge](/verify/taulib/docs/book-iii-physics-hodge/)
- Source path: [`TauLib/BookIII/Physics/Hodge.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/Hodge.lean#L115-L130)
- Source range: L115-L130
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D48` — Sector Addressability

## Immediate Comment / Docstring

```lean
/-- [III.D48] Sector addressability: every cylinder has a unique triple
    (b, c, x) address via its BNF. -/
```

## Source Excerpt

```lean
def sector_addressability_check (bound db : TauIdx) : Bool :=
  go 0 1 ((bound + 1) * (db + 1))
where
  go (x k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if k > db then go (x + 1) 1 (fuel - 1)
    else
      let pk := primorial k
      if pk == 0 then go x (k + 1) (fuel - 1)
      else
        let nf := boundary_normal_form (x % pk) k
        -- Address is well-defined: components sum to original
        let sum := (nf.b_part + nf.c_part + nf.x_part) % pk
        sum == x % pk && go x (k + 1) (fuel - 1)
  termination_by fuel
```
