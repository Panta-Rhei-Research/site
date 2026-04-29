---
{
  "projection_kind": "taulib_declaration",
  "title": "boundary_to_interior_check",
  "permalink": "/verify/taulib/docs/book-iii-doors-mutual-determination/boundary-to-interior-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Doors.MutualDetermination`.",
  "declaration_id": "TauLib.BookIII.Doors.MutualDetermination::boundary_to_interior_check",
  "declaration_slug": "boundary-to-interior-check",
  "kind": "def",
  "name": "boundary_to_interior_check",
  "module_name": "TauLib.BookIII.Doors.MutualDetermination",
  "module_url": "/verify/taulib/docs/book-iii-doors-mutual-determination/",
  "source_line_start": 42,
  "source_line_end": 56,
  "registry_ids": [
    "III.D25"
  ],
  "related_registry_items": [
    {
      "id": "III.D25",
      "title": "Mutual Determination Schema",
      "url": "/registry/object/III.D25/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/MutualDetermination.lean#L42-L56",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Doors.MutualDetermination",
        "url": "/verify/taulib/docs/book-iii-doors-mutual-determination/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/MutualDetermination.lean#L42-L56",
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

- Module: [TauLib.BookIII.Doors.MutualDetermination](/verify/taulib/docs/book-iii-doors-mutual-determination/)
- Source path: [`TauLib/BookIII/Doors/MutualDetermination.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/MutualDetermination.lean#L42-L56)
- Source range: L42-L56
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D25` — Mutual Determination Schema

## Immediate Comment / Docstring

```lean
/-- [III.D25] Boundary → Interior: reconstruction from CRT residues
    agrees with direct computation. -/
```

## Source Excerpt

```lean
def boundary_to_interior_check (bound db : TauIdx) : Bool :=
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
        let residues := crt_decompose x k
        let reconstructed := crt_reconstruct residues k
        reconstructed == x % pk && go x (k + 1) (fuel - 1)
  termination_by fuel
```
