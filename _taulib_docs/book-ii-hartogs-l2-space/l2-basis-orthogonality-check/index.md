---
{
  "projection_kind": "taulib_declaration",
  "title": "l2_basis_orthogonality_check",
  "permalink": "/verify/taulib/docs/book-ii-hartogs-l2-space/l2-basis-orthogonality-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Hartogs.L2Space`.",
  "declaration_id": "TauLib.BookII.Hartogs.L2Space::l2_basis_orthogonality_check",
  "declaration_slug": "l2-basis-orthogonality-check",
  "kind": "def",
  "name": "l2_basis_orthogonality_check",
  "module_name": "TauLib.BookII.Hartogs.L2Space",
  "module_url": "/verify/taulib/docs/book-ii-hartogs-l2-space/",
  "source_line_start": 164,
  "source_line_end": 182,
  "registry_ids": [
    "II.D82"
  ],
  "related_registry_items": [
    {
      "id": "II.D82",
      "title": "L² Inner Product",
      "url": "/registry/object/II.D82/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/L2Space.lean#L164-L182",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Hartogs.L2Space",
        "url": "/verify/taulib/docs/book-ii-hartogs-l2-space/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/L2Space.lean#L164-L182",
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

- Module: [TauLib.BookII.Hartogs.L2Space](/verify/taulib/docs/book-ii-hartogs-l2-space/)
- Source path: [`TauLib/BookII/Hartogs/L2Space.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/L2Space.lean#L164-L182)
- Source range: L164-L182
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D82` — L² Inner Product

## Immediate Comment / Docstring

```lean
/-- [II.D82] Check that indicator functions form an orthogonal basis
    for L²(Z/M_k Z). -/
```

## Source Excerpt

```lean
def l2_basis_orthogonality_check (k : Nat) : Bool :=
  let pk := primorial k
  go_a 0 pk pk
where
  go_a (a pk fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if a >= pk then true
    else go_b a 0 pk pk && go_a (a + 1) pk (fuel - 1)
  termination_by fuel
  go_b (a b pk fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if b >= pk then true
    else
      let f : Nat → Int := fun x => if x == a then 1 else 0
      let g : Nat → Int := fun x => if x == b then 1 else 0
      let ip := inner_product_sum f g k
      let expected := if a == b then 1 else 0
      (ip == expected) && go_b a (b + 1) pk (fuel - 1)
  termination_by fuel
```
