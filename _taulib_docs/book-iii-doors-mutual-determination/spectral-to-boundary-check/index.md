---
{
  "projection_kind": "taulib_declaration",
  "title": "spectral_to_boundary_check",
  "permalink": "/verify/taulib/docs/book-iii-doors-mutual-determination/spectral-to-boundary-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Doors.MutualDetermination`.",
  "declaration_id": "TauLib.BookIII.Doors.MutualDetermination::spectral_to_boundary_check",
  "declaration_slug": "spectral-to-boundary-check",
  "kind": "def",
  "name": "spectral_to_boundary_check",
  "module_name": "TauLib.BookIII.Doors.MutualDetermination",
  "module_url": "/verify/taulib/docs/book-iii-doors-mutual-determination/",
  "source_line_start": 79,
  "source_line_end": 100,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/MutualDetermination.lean#L79-L100",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/MutualDetermination.lean#L79-L100",
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
- Source path: [`TauLib/BookIII/Doors/MutualDetermination.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/MutualDetermination.lean#L79-L100)
- Source range: L79-L100
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D25` — Mutual Determination Schema

## Immediate Comment / Docstring

```lean
/-- [III.D25] Spectral → Boundary: the spectral decomposition uniquely
    determines the boundary data (injectivity). -/
```

## Source Excerpt

```lean
def spectral_to_boundary_check (bound db : TauIdx) : Bool :=
  go 0 0 1 ((bound + 1) * (bound + 1) * (db + 1))
where
  go (x y k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if y > bound then go (x + 1) 0 1 (fuel - 1)
    else if k > db then go x (y + 1) 1 (fuel - 1)
    else
      let pk := primorial k
      if pk == 0 then go x y (k + 1) (fuel - 1)
      else
        let xr := x % pk
        let yr := y % pk
        let nfx := boundary_normal_form xr k
        let nfy := boundary_normal_form yr k
        let spectral_agree := nfx.b_part == nfy.b_part &&
                              nfx.c_part == nfy.c_part &&
                              nfx.x_part == nfy.x_part
        let ok := if spectral_agree then xr == yr else true
        ok && go x y (k + 1) (fuel - 1)
  termination_by fuel
```
