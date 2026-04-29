---
{
  "projection_kind": "taulib_declaration",
  "title": "base_change_check",
  "permalink": "/verify/taulib/docs/book-iii-arithmetic-langlands/base-change-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Arithmetic.Langlands`.",
  "declaration_id": "TauLib.BookIII.Arithmetic.Langlands::base_change_check",
  "declaration_slug": "base-change-check",
  "kind": "def",
  "name": "base_change_check",
  "module_name": "TauLib.BookIII.Arithmetic.Langlands",
  "module_url": "/verify/taulib/docs/book-iii-arithmetic-langlands/",
  "source_line_start": 167,
  "source_line_end": 187,
  "registry_ids": [
    "III.T37"
  ],
  "related_registry_items": [
    {
      "id": "III.T37",
      "title": "Base Change-Transfer Naturality",
      "url": "/registry/object/III.T37/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/Langlands.lean#L167-L187",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Arithmetic.Langlands",
        "url": "/verify/taulib/docs/book-iii-arithmetic-langlands/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/Langlands.lean#L167-L187",
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

- Module: [TauLib.BookIII.Arithmetic.Langlands](/verify/taulib/docs/book-iii-arithmetic-langlands/)
- Source path: [`TauLib/BookIII/Arithmetic/Langlands.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/Langlands.lean#L167-L187)
- Source range: L167-L187
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.T37` — Base Change-Transfer Naturality

## Immediate Comment / Docstring

```lean
/-- [III.T37] Base change-transfer naturality: the enrichment functor
    Enr₀₁ on sector morphisms and the defect functional between sectors
    are natural transformations. Checked by: tower projection commutes
    with sector decomposition. -/
```

## Source Excerpt

```lean
def base_change_check (bound db : TauIdx) : Bool :=
  go 0 1 ((bound + 1) * (db + 1))
where
  go (x k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if k >= db then go (x + 1) 1 (fuel - 1)
    else
      let pk := primorial k
      let pk1 := primorial (k + 1)
      if pk == 0 || pk1 == 0 then go x (k + 1) (fuel - 1)
      else
        -- BNF at level k+1 then project to k
        let nf_k1 := boundary_normal_form (x % pk1) (k + 1)
        let sum_k1 := (nf_k1.b_part + nf_k1.c_part + nf_k1.x_part) % pk
        -- BNF at level k directly
        let nf_k := boundary_normal_form (x % pk) k
        let sum_k := (nf_k.b_part + nf_k.c_part + nf_k.x_part) % pk
        -- Naturality: projection commutes with decomposition
        sum_k1 == sum_k && go x (k + 1) (fuel - 1)
  termination_by fuel
```
