---
{
  "projection_kind": "taulib_declaration",
  "title": "earned_admissibility_check",
  "permalink": "/verify/taulib/docs/book-iii-computation-admissibility/earned-admissibility-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Computation.Admissibility`.",
  "declaration_id": "TauLib.BookIII.Computation.Admissibility::earned_admissibility_check",
  "declaration_slug": "earned-admissibility-check",
  "kind": "def",
  "name": "earned_admissibility_check",
  "module_name": "TauLib.BookIII.Computation.Admissibility",
  "module_url": "/verify/taulib/docs/book-iii-computation-admissibility/",
  "source_line_start": 140,
  "source_line_end": 164,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/Admissibility.lean#L140-L164",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/Admissibility.lean#L140-L164",
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
- Source path: [`TauLib/BookIII/Computation/Admissibility.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/Admissibility.lean#L140-L164)
- Source range: L140-L164
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.P21` — Earned Admissibility

## Immediate Comment / Docstring

```lean
/-- [III.P21] Earned admissibility: canonical operations are τ-admissible.
    Identity, χ₊ (B-projection), χ₋ (C-projection) all have width ≤ 1. -/
```

## Source Excerpt

```lean
def earned_admissibility_check (bound db : TauIdx) : Bool :=
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
        -- Identity: reduce(x, k) == x % pk (exercises reduce)
        let id_ok := reduce x k == xr
        -- B-projection: take BNF, keep only b_part
        let nf := boundary_normal_form xr k
        let b_proj := nf.b_part
        let b_ok := b_proj < pk
        -- C-projection: keep only c_part
        let c_proj := nf.c_part
        let c_ok := c_proj < pk
        -- BNF surjectivity: components sum to original
        let sum_ok := (b_proj + c_proj + nf.x_part) % pk == xr
        id_ok && b_ok && c_ok && sum_ok && go x (k + 1) (fuel - 1)
  termination_by fuel
```
