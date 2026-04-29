---
{
  "projection_kind": "taulib_declaration",
  "title": "bc_non_collapse_check",
  "permalink": "/verify/taulib/docs/book-iii-spectral-trichotomy/bc-non-collapse-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Spectral.Trichotomy`.",
  "declaration_id": "TauLib.BookIII.Spectral.Trichotomy::bc_non_collapse_check",
  "declaration_slug": "bc-non-collapse-check",
  "kind": "def",
  "name": "bc_non_collapse_check",
  "module_name": "TauLib.BookIII.Spectral.Trichotomy",
  "module_url": "/verify/taulib/docs/book-iii-spectral-trichotomy/",
  "source_line_start": 208,
  "source_line_end": 223,
  "registry_ids": [
    "III.T15"
  ],
  "related_registry_items": [
    {
      "id": "III.T15",
      "title": "B/C Non-Collapse Theorem",
      "url": "/registry/object/III.T15/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/Trichotomy.lean#L208-L223",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/Trichotomy.lean#L208-L223",
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
- Source path: [`TauLib/BookIII/Spectral/Trichotomy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/Trichotomy.lean#L208-L223)
- Source range: L208-L223
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.T15` — B/C Non-Collapse Theorem

## Immediate Comment / Docstring

```lean
/-- [III.T15] B/C non-collapse: verify that B-supported and C-supported
    subrings are genuinely distinct. No isomorphism preserving
    the tower structure exists between them.
    Criterion: B-type primes and C-type primes have different growth
    behavior (B = exponent-type, C = tetration-type). -/
```

## Source Excerpt

```lean
def bc_non_collapse_check (_bound db : TauIdx) : Bool :=
  go 1 (db + 1)
where
  go (k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k > db then true
    else
      let (b_ct, c_ct, _x_ct) := label_counts k
      -- Both B and C types exist once depth includes p=5 (k ≥ 3)
      let both_exist := if k >= 3 then b_ct > 0 && c_ct > 0 else true
      let b_prod := compute_label_product .B k
      let c_prod := compute_label_product .C k
      -- Non-collapse: products differ when both types present
      let non_iso := if b_ct > 0 && c_ct > 0 then b_prod != c_prod else true
      both_exist && non_iso && go (k + 1) (fuel - 1)
  termination_by fuel
```
