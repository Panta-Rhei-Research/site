---
{
  "projection_kind": "taulib_declaration",
  "title": "sector_growth_check",
  "permalink": "/verify/taulib/docs/book-iii-doors-grand-grh/sector-growth-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Doors.GrandGRH`.",
  "declaration_id": "TauLib.BookIII.Doors.GrandGRH::sector_growth_check",
  "declaration_slug": "sector-growth-check",
  "kind": "def",
  "name": "sector_growth_check",
  "module_name": "TauLib.BookIII.Doors.GrandGRH",
  "module_url": "/verify/taulib/docs/book-iii-doors-grand-grh/",
  "source_line_start": 162,
  "source_line_end": 175,
  "registry_ids": [
    "III.T20"
  ],
  "related_registry_items": [
    {
      "id": "III.T20",
      "title": "Prime Polarity Scaling Theorem",
      "url": "/registry/object/III.T20/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/GrandGRH.lean#L162-L175",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/GrandGRH.lean#L162-L175",
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
- Source path: [`TauLib/BookIII/Doors/GrandGRH.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/GrandGRH.lean#L162-L175)
- Source range: L162-L175
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.T20` — Prime Polarity Scaling Theorem

## Immediate Comment / Docstring

```lean
/-- [III.T20] Sector growth rates: B-product and C-product grow at
    different rates (B = multiplicative/exponent, C = additive/tetration). -/
```

## Source Excerpt

```lean
def sector_growth_check (db : TauIdx) : Bool :=
  go 2 (db + 1)
where
  go (k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k > db then true
    else
      let b_k := split_zeta_b k
      let c_k := split_zeta_c k
      -- B and C products are distinct when both nonempty
      let (b_ct, c_ct, _) := label_counts k
      let distinct := if b_ct > 0 && c_ct > 0 then b_k != c_k else true
      distinct && go (k + 1) (fuel - 1)
  termination_by fuel
```
