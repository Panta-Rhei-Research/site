---
{
  "projection_kind": "taulib_declaration",
  "title": "crt_goldbach_duality_check",
  "permalink": "/verify/taulib/docs/book-iii-spectral-goldbach-deep/crt-goldbach-duality-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Spectral.GoldbachDeep`.",
  "declaration_id": "TauLib.BookIII.Spectral.GoldbachDeep::crt_goldbach_duality_check",
  "declaration_slug": "crt-goldbach-duality-check",
  "kind": "def",
  "name": "crt_goldbach_duality_check",
  "module_name": "TauLib.BookIII.Spectral.GoldbachDeep",
  "module_url": "/verify/taulib/docs/book-iii-spectral-goldbach-deep/",
  "source_line_start": 158,
  "source_line_end": 167,
  "registry_ids": [
    "III.P43"
  ],
  "related_registry_items": [
    {
      "id": "III.P43",
      "title": "CRT-Goldbach Duality",
      "url": "/registry/object/III.P43/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/GoldbachDeep.lean#L158-L167",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Spectral.GoldbachDeep",
        "url": "/verify/taulib/docs/book-iii-spectral-goldbach-deep/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/GoldbachDeep.lean#L158-L167",
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

- Module: [TauLib.BookIII.Spectral.GoldbachDeep](/verify/taulib/docs/book-iii-spectral-goldbach-deep/)
- Source path: [`TauLib/BookIII/Spectral/GoldbachDeep.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/GoldbachDeep.lean#L158-L167)
- Source range: L158-L167
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.P43` — CRT-Goldbach Duality

## Immediate Comment / Docstring

```lean
/-- [III.P43] CRT-Goldbach duality: at each depth k, every even n
    in [4..bound] has a local solution at prime p_k. -/
```

## Source Excerpt

```lean
def crt_goldbach_duality_check (bound db : Nat) : Bool :=
  go 4 1 ((bound + 1) * (db + 1))
where
  go (n k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if n > bound then true
    else if k > db then go (n + 2) 1 (fuel - 1)
    else
      crt_goldbach_local_solvable n k && go n (k + 1) (fuel - 1)
  termination_by fuel
```
