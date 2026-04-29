---
{
  "projection_kind": "taulib_declaration",
  "title": "bnf_uniqueness_check",
  "permalink": "/verify/taulib/docs/book-iii-spectral-trichotomy/bnf-uniqueness-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Spectral.Trichotomy`.",
  "declaration_id": "TauLib.BookIII.Spectral.Trichotomy::bnf_uniqueness_check",
  "declaration_slug": "bnf-uniqueness-check",
  "kind": "def",
  "name": "bnf_uniqueness_check",
  "module_name": "TauLib.BookIII.Spectral.Trichotomy",
  "module_url": "/verify/taulib/docs/book-iii-spectral-trichotomy/",
  "source_line_start": 161,
  "source_line_end": 183,
  "registry_ids": [
    "III.D24"
  ],
  "related_registry_items": [
    {
      "id": "III.D24",
      "title": "Boundary Normal Form",
      "url": "/registry/object/III.D24/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/Trichotomy.lean#L161-L183",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Spectral.Trichotomy",
        "url": "/verify/taulib/docs/book-iii-spectral-trichotomy/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/Trichotomy.lean#L161-L183",
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

- Module: [TauLib.BookIII.Spectral.Trichotomy](/verify/taulib/docs/book-iii-spectral-trichotomy/)
- Source path: [`TauLib/BookIII/Spectral/Trichotomy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/Trichotomy.lean#L161-L183)
- Source range: L161-L183
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D24` — Boundary Normal Form

## Immediate Comment / Docstring

```lean
/-- [III.D24] BNF uniqueness: the decomposition is unique. -/
```

## Source Excerpt

```lean
def bnf_uniqueness_check (bound db : TauIdx) : Bool :=
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
        -- If BNFs agree, then x ≡ y mod Prim(k)
        let bnfs_agree := nfx.b_part == nfy.b_part &&
                          nfx.c_part == nfy.c_part &&
                          nfx.x_part == nfy.x_part
        let ok := if bnfs_agree then xr == yr else true
        ok && go x y (k + 1) (fuel - 1)
  termination_by fuel
```
