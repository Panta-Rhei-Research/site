---
{
  "projection_kind": "taulib_declaration",
  "title": "composition_check",
  "permalink": "/verify/taulib/docs/book-iii-computation-admissibility/composition-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Computation.Admissibility`.",
  "declaration_id": "TauLib.BookIII.Computation.Admissibility::composition_check",
  "declaration_slug": "composition-check",
  "kind": "def",
  "name": "composition_check",
  "module_name": "TauLib.BookIII.Computation.Admissibility",
  "module_url": "/verify/taulib/docs/book-iii-computation-admissibility/",
  "source_line_start": 168,
  "source_line_end": 190,
  "registry_ids": [
    "III.P21"
  ],
  "related_registry_items": [
    {
      "id": "III.P21",
      "title": "Earned Admissibility",
      "url": "/registry/object/III.P21/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/Admissibility.lean#L168-L190",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Computation.Admissibility",
        "url": "/verify/taulib/docs/book-iii-computation-admissibility/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/Admissibility.lean#L168-L190",
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

- Module: [TauLib.BookIII.Computation.Admissibility](/verify/taulib/docs/book-iii-computation-admissibility/)
- Source path: [`TauLib/BookIII/Computation/Admissibility.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/Admissibility.lean#L168-L190)
- Source range: L168-L190
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.P21` — Earned Admissibility

## Immediate Comment / Docstring

```lean
/-- [III.P21] Composition sub-additivity: compositions of admissible
    operations stay admissible. -/
```

## Source Excerpt

```lean
def composition_check (bound db : TauIdx) : Bool :=
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
        let xr := x % pk
        let nf := boundary_normal_form xr k
        -- Compose B-proj then C-proj: both outputs stay in range
        let b := nf.b_part
        let nf2 := boundary_normal_form b k
        let c_of_b := nf2.c_part
        let ok := c_of_b < pk
        -- Sub-additivity: composing projections doesn't exceed sum
        let b_of_c := (boundary_normal_form nf.c_part k).b_part
        let sub_ok := b_of_c + c_of_b <= pk
        ok && sub_ok && go x (k + 1) (fuel - 1)
  termination_by fuel
```
