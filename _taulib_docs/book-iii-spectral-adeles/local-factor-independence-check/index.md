---
{
  "projection_kind": "taulib_declaration",
  "title": "local_factor_independence_check",
  "permalink": "/verify/taulib/docs/book-iii-spectral-adeles/local-factor-independence-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Spectral.Adeles`.",
  "declaration_id": "TauLib.BookIII.Spectral.Adeles::local_factor_independence_check",
  "declaration_slug": "local-factor-independence-check",
  "kind": "def",
  "name": "local_factor_independence_check",
  "module_name": "TauLib.BookIII.Spectral.Adeles",
  "module_url": "/verify/taulib/docs/book-iii-spectral-adeles/",
  "source_line_start": 177,
  "source_line_end": 199,
  "registry_ids": [
    "III.P07"
  ],
  "related_registry_items": [
    {
      "id": "III.P07",
      "title": "Adelic Euler Product",
      "url": "/registry/object/III.P07/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/Adeles.lean#L177-L199",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Spectral.Adeles",
        "url": "/verify/taulib/docs/book-iii-spectral-adeles/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/Adeles.lean#L177-L199",
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

- Module: [TauLib.BookIII.Spectral.Adeles](/verify/taulib/docs/book-iii-spectral-adeles/)
- Source path: [`TauLib/BookIII/Spectral/Adeles.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/Adeles.lean#L177-L199)
- Source range: L177-L199
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.P07` — Adelic Euler Product

## Immediate Comment / Docstring

```lean
/-- [III.P07] Local factor independence: modifying one local factor
    only changes that component, not others. -/
```

## Source Excerpt

```lean
def local_factor_independence_check (bound db : TauIdx) : Bool :=
  go 0 1 0 ((bound + 1) * (db + 1) * (db + 1))
where
  go (x k i fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if k > db then go (x + 1) 1 0 (fuel - 1)
    else if i >= k then go x (k + 1) 0 (fuel - 1)
    else
      let residues := crt_decompose x k
      -- Modify component i
      let p_i := nth_prime (i + 1)
      let modified := residues.set i (if p_i > 0 then (residues.getD i 0 + 1) % p_i else 0)
      -- Check: other components unchanged
      let others_ok := check_others residues modified i 0 k
      others_ok && go x k (i + 1) (fuel - 1)
  termination_by fuel
  check_others (orig modified : List TauIdx) (skip j k : Nat) : Bool :=
    if j >= k then true
    else if j == skip then check_others orig modified skip (j + 1) k
    else
      orig.getD j 0 == modified.getD j 0 &&
        check_others orig modified skip (j + 1) k
```
