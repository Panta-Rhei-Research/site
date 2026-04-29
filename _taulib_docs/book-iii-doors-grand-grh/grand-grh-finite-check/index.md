---
{
  "projection_kind": "taulib_declaration",
  "title": "grand_grh_finite_check",
  "permalink": "/verify/taulib/docs/book-iii-doors-grand-grh/grand-grh-finite-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Doors.GrandGRH`.",
  "declaration_id": "TauLib.BookIII.Doors.GrandGRH::grand_grh_finite_check",
  "declaration_slug": "grand-grh-finite-check",
  "kind": "def",
  "name": "grand_grh_finite_check",
  "module_name": "TauLib.BookIII.Doors.GrandGRH",
  "module_url": "/verify/taulib/docs/book-iii-doors-grand-grh/",
  "source_line_start": 43,
  "source_line_end": 62,
  "registry_ids": [
    "III.D31"
  ],
  "related_registry_items": [
    {
      "id": "III.D31",
      "title": "Grand GRH (τ-effective)",
      "url": "/registry/object/III.D31/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/GrandGRH.lean#L43-L62",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Doors.GrandGRH",
        "url": "/verify/taulib/docs/book-iii-doors-grand-grh/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/GrandGRH.lean#L43-L62",
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

- Module: [TauLib.BookIII.Doors.GrandGRH](/verify/taulib/docs/book-iii-doors-grand-grh/)
- Source path: [`TauLib/BookIII/Doors/GrandGRH.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/GrandGRH.lean#L43-L62)
- Source range: L43-L62
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D31` — Grand GRH (τ-effective)

## Immediate Comment / Docstring

```lean
/-- [III.D31] Grand GRH at finite primorial level k: the finite Euler
    product decomposes correctly via B/C/X labels, and each sector
    has the correct zero structure at this level. -/
```

## Source Excerpt

```lean
def grand_grh_finite_check (db : TauIdx) : Bool :=
  go 1 (db + 1)
where
  go (k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k > db then true
    else
      -- Sector purity: B-type and C-type primes are disjoint
      let b_prod := split_zeta_b k
      let c_prod := split_zeta_c k
      let coprime := Nat.gcd b_prod c_prod == 1
      -- Completeness: B * C * X = Prim(k)
      let x_prod := split_zeta_x k
      let pk := primorial k
      let complete := if pk > 0 then b_prod * c_prod * x_prod == pk else true
      -- Each sector has correct eigenvalue structure
      let (b_ct, c_ct, _x_ct) := label_counts k
      let balance := if k >= 3 then b_ct > 0 && c_ct > 0 else true
      coprime && complete && balance && go (k + 1) (fuel - 1)
  termination_by fuel
```
