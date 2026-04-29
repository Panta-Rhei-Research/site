---
{
  "projection_kind": "taulib_declaration",
  "title": "bc_coprime_check",
  "permalink": "/verify/taulib/docs/book-iii-spectral-trichotomy/bc-coprime-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Spectral.Trichotomy`.",
  "declaration_id": "TauLib.BookIII.Spectral.Trichotomy::bc_coprime_check",
  "declaration_slug": "bc-coprime-check",
  "kind": "def",
  "name": "bc_coprime_check",
  "module_name": "TauLib.BookIII.Spectral.Trichotomy",
  "module_url": "/verify/taulib/docs/book-iii-spectral-trichotomy/",
  "source_line_start": 227,
  "source_line_end": 240,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/Trichotomy.lean#L227-L240",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/Trichotomy.lean#L227-L240",
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
- Source path: [`TauLib/BookIII/Spectral/Trichotomy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/Trichotomy.lean#L227-L240)
- Source range: L227-L240
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.T15` — B/C Non-Collapse Theorem

## Immediate Comment / Docstring

```lean
/-- [III.T15] B/C asymmetry: the B-product and C-product at depth k
    are coprime (no shared prime factors). -/
```

## Source Excerpt

```lean
def bc_coprime_check (db : TauIdx) : Bool :=
  go 1 (db + 1)
where
  go (k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k > db then true
    else
      let b_prod := compute_label_product .B k
      let c_prod := compute_label_product .C k
      -- B and C products share no common prime factor
      -- (by definition: each prime gets exactly one label)
      let coprime := Nat.gcd b_prod c_prod == 1
      coprime && go (k + 1) (fuel - 1)
  termination_by fuel
```
