---
{
  "projection_kind": "taulib_declaration",
  "title": "split_zeta_check",
  "permalink": "/verify/taulib/docs/book-iii-doors-split-complex-zeta/split-zeta-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Doors.SplitComplexZeta`.",
  "declaration_id": "TauLib.BookIII.Doors.SplitComplexZeta::split_zeta_check",
  "declaration_slug": "split-zeta-check",
  "kind": "def",
  "name": "split_zeta_check",
  "module_name": "TauLib.BookIII.Doors.SplitComplexZeta",
  "module_url": "/verify/taulib/docs/book-iii-doors-split-complex-zeta/",
  "source_line_start": 50,
  "source_line_end": 63,
  "registry_ids": [
    "III.D26"
  ],
  "related_registry_items": [
    {
      "id": "III.D26",
      "title": "Split-Complex Zeta ζ_τ",
      "url": "/registry/object/III.D26/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/SplitComplexZeta.lean#L50-L63",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Doors.SplitComplexZeta",
        "url": "/verify/taulib/docs/book-iii-doors-split-complex-zeta/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/SplitComplexZeta.lean#L50-L63",
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

- Module: [TauLib.BookIII.Doors.SplitComplexZeta](/verify/taulib/docs/book-iii-doors-split-complex-zeta/)
- Source path: [`TauLib/BookIII/Doors/SplitComplexZeta.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/SplitComplexZeta.lean#L50-L63)
- Source range: L50-L63
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D26` — Split-Complex Zeta ζ_τ

## Immediate Comment / Docstring

```lean
/-- [III.D26] Split-complex zeta check: B · C · X = Prim(k).
    The three label products account for all primes in the primorial. -/
```

## Source Excerpt

```lean
def split_zeta_check (db : TauIdx) : Bool :=
  go 1 (db + 1)
where
  go (k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k > db then true
    else
      let b_prod := split_zeta_b k
      let c_prod := split_zeta_c k
      let x_prod := split_zeta_x k
      let pk := primorial k
      let product_ok := if pk > 0 then b_prod * c_prod * x_prod == pk else true
      product_ok && go (k + 1) (fuel - 1)
  termination_by fuel
```
