---
{
  "projection_kind": "taulib_declaration",
  "title": "moduli_singleton_check",
  "permalink": "/verify/taulib/docs/book-ii-central-theorem-categoricity/moduli-singleton-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.CentralTheorem.Categoricity`.",
  "declaration_id": "TauLib.BookII.CentralTheorem.Categoricity::moduli_singleton_check",
  "declaration_slug": "moduli-singleton-check",
  "kind": "def",
  "name": "moduli_singleton_check",
  "module_name": "TauLib.BookII.CentralTheorem.Categoricity",
  "module_url": "/verify/taulib/docs/book-ii-central-theorem-categoricity/",
  "source_line_start": 207,
  "source_line_end": 223,
  "registry_ids": [
    "II.D61"
  ],
  "related_registry_items": [
    {
      "id": "II.D61",
      "title": "Moduli Space",
      "url": "/registry/object/II.D61/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/Categoricity.lean#L207-L223",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.CentralTheorem.Categoricity",
        "url": "/verify/taulib/docs/book-ii-central-theorem-categoricity/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/Categoricity.lean#L207-L223",
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

- Module: [TauLib.BookII.CentralTheorem.Categoricity](/verify/taulib/docs/book-ii-central-theorem-categoricity/)
- Source path: [`TauLib/BookII/CentralTheorem/Categoricity.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/Categoricity.lean#L207-L223)
- Source range: L207-L223
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D61` — Moduli Space

## Immediate Comment / Docstring

```lean
/-- [II.D61] Moduli space singleton check: M_{tau^3} = {pt}.

    The ABCD chart has NO free parameters:
    - from_tau_idx is uniquely determined by the primorial factorization
    - to_tau_idx is uniquely determined by the encoding
    - The round-trip to_tau_idx . from_tau_idx = id
    - No continuous deformation can change any ABCD coordinate
      while preserving tau-admissibility

    We verify: for every x in [2, bound], the ABCD chart is rigid
    (round-trips perfectly, and the representation is unique). -/
```

## Source Excerpt

```lean
def moduli_singleton_check (bound : TauIdx) : Bool :=
  go 2 (bound + 1)
where
  go (x fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else
      let p := from_tau_idx x
      -- Round-trip: to_tau_idx(from_tau_idx(x)) = x
      let rt_ok := to_tau_idx p == x
      -- No deformations: perturbing any ABCD coordinate changes the index
      -- (or breaks admissibility). Test: incrementing B changes the index.
      let p_inc_b : TauAdmissiblePoint := { p with b := p.b + 1 }
      let idx_inc := to_tau_idx p_inc_b
      let rigid_ok := idx_inc != x || p.b + 1 == p.b  -- can't happen
      rt_ok && rigid_ok && go (x + 1) (fuel - 1)
  termination_by fuel
```
