---
{
  "projection_kind": "taulib_declaration",
  "title": "functoriality_check",
  "permalink": "/verify/taulib/docs/book-iii-arithmetic-langlands/functoriality-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Arithmetic.Langlands`.",
  "declaration_id": "TauLib.BookIII.Arithmetic.Langlands::functoriality_check",
  "declaration_slug": "functoriality-check",
  "kind": "def",
  "name": "functoriality_check",
  "module_name": "TauLib.BookIII.Arithmetic.Langlands",
  "module_url": "/verify/taulib/docs/book-iii-arithmetic-langlands/",
  "source_line_start": 138,
  "source_line_end": 157,
  "registry_ids": [
    "III.T36"
  ],
  "related_registry_items": [
    {
      "id": "III.T36",
      "title": "Functoriality Theorem",
      "url": "/registry/object/III.T36/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/Langlands.lean#L138-L157",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/Langlands.lean#L138-L157",
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
- Source path: [`TauLib/BookIII/Arithmetic/Langlands.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/Langlands.lean#L138-L157)
- Source range: L138-L157
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.T36` — Functoriality Theorem

## Immediate Comment / Docstring

```lean
/-- [III.T36] Functoriality: sector morphisms (BNF-preserving maps) commute
    with spectral decomposition. At finite level: the polarity swap commutes
    with the B/C/X decomposition. -/
```

## Source Excerpt

```lean
def functoriality_check (bound db : TauIdx) : Bool :=
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
        -- Apply polarity swap (a sector morphism)
        let swapped := polarity_swap nf
        -- Check that swap preserves the total
        let total_orig := (nf.b_part + nf.c_part + nf.x_part) % pk
        let total_swap := (swapped.b_part + swapped.c_part + swapped.x_part) % pk
        total_orig == total_swap && go x (k + 1) (fuel - 1)
  termination_by fuel
```
