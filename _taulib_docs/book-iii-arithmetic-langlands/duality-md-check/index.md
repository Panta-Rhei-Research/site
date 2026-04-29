---
{
  "projection_kind": "taulib_declaration",
  "title": "duality_md_check",
  "permalink": "/verify/taulib/docs/book-iii-arithmetic-langlands/duality-md-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Arithmetic.Langlands`.",
  "declaration_id": "TauLib.BookIII.Arithmetic.Langlands::duality_md_check",
  "declaration_slug": "duality-md-check",
  "kind": "def",
  "name": "duality_md_check",
  "module_name": "TauLib.BookIII.Arithmetic.Langlands",
  "module_url": "/verify/taulib/docs/book-iii-arithmetic-langlands/",
  "source_line_start": 109,
  "source_line_end": 129,
  "registry_ids": [
    "III.P28"
  ],
  "related_registry_items": [
    {
      "id": "III.P28",
      "title": "Duality as Mutual Determination on ℤ²",
      "url": "/registry/object/III.P28/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/Langlands.lean#L109-L129",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/Langlands.lean#L109-L129",
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
- Source path: [`TauLib/BookIII/Arithmetic/Langlands.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/Langlands.lean#L109-L129)
- Source range: L109-L129
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.P28` — Duality as Mutual Determination on ℤ²

## Immediate Comment / Docstring

```lean
/-- [III.P28] Duality as Mutual Determination: the A-G duality IS MD
    with m-axis = boundary, n-axis = spectral, full = interior. -/
```

## Source Excerpt

```lean
def duality_md_check (bound db : TauIdx) : Bool :=
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
        -- m-axis (boundary) determines n-axis (spectral) via BNF
        let m := nf.b_part
        let n := nf.c_part
        -- Interior = full character = m + n + x_part
        let interior := (m + n + nf.x_part) % pk
        -- MD: interior = original
        interior == xr && go x (k + 1) (fuel - 1)
  termination_by fuel
```
