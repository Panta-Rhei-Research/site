---
{
  "projection_kind": "taulib_declaration",
  "title": "obstruction_check",
  "permalink": "/verify/taulib/docs/book-iii-doors-poincare/obstruction-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Doors.Poincare`.",
  "declaration_id": "TauLib.BookIII.Doors.Poincare::obstruction_check",
  "declaration_slug": "obstruction-check",
  "kind": "def",
  "name": "obstruction_check",
  "module_name": "TauLib.BookIII.Doors.Poincare",
  "module_url": "/verify/taulib/docs/book-iii-doors-poincare/",
  "source_line_start": 122,
  "source_line_end": 142,
  "registry_ids": [
    "III.P13"
  ],
  "related_registry_items": [
    {
      "id": "III.P13",
      "title": "Poincaré as Gluing Guarantee",
      "url": "/registry/object/III.P13/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/Poincare.lean#L122-L142",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Doors.Poincare",
        "url": "/verify/taulib/docs/book-iii-doors-poincare/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/Poincare.lean#L122-L142",
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

- Module: [TauLib.BookIII.Doors.Poincare](/verify/taulib/docs/book-iii-doors-poincare/)
- Source path: [`TauLib/BookIII/Doors/Poincare.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/Poincare.lean#L122-L142)
- Source range: L122-L142
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.P13` — Poincaré as Gluing Guarantee

## Immediate Comment / Docstring

```lean
/-- [III.P13] Obstruction detection: when the fundamental group is
    non-trivial, the gluing fails. Test: inconsistent residues
    cannot be reconstructed coherently. -/
```

## Source Excerpt

```lean
def obstruction_check (db : TauIdx) : Bool :=
  go 1 (db + 1)
where
  go (k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k > db then true
    else
      let pk := primorial k
      if pk == 0 || pk <= 1 then go (k + 1) (fuel - 1)
      else
        -- Trivial fundamental group ⟹ unique reconstruction
        -- Test: for all x < Prim(k), CRT is bijective
        let bijective := check_bijectivity 0 pk k
        bijective && go (k + 1) (fuel - 1)
  termination_by fuel
  check_bijectivity (x pk k : Nat) : Bool :=
    if x >= pk then true
    else
      let residues := crt_decompose x k
      let reconstructed := crt_reconstruct residues k
      reconstructed == x && check_bijectivity (x + 1) pk k
```
