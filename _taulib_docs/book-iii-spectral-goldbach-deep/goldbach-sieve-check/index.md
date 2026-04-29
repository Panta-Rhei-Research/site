---
{
  "projection_kind": "taulib_declaration",
  "title": "goldbach_sieve_check",
  "permalink": "/verify/taulib/docs/book-iii-spectral-goldbach-deep/goldbach-sieve-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Spectral.GoldbachDeep`.",
  "declaration_id": "TauLib.BookIII.Spectral.GoldbachDeep::goldbach_sieve_check",
  "declaration_slug": "goldbach-sieve-check",
  "kind": "def",
  "name": "goldbach_sieve_check",
  "module_name": "TauLib.BookIII.Spectral.GoldbachDeep",
  "module_url": "/verify/taulib/docs/book-iii-spectral-goldbach-deep/",
  "source_line_start": 63,
  "source_line_end": 72,
  "registry_ids": [
    "III.D102"
  ],
  "related_registry_items": [
    {
      "id": "III.D102",
      "title": "Sieve-Accelerated Goldbach",
      "url": "/registry/object/III.D102/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/GoldbachDeep.lean#L63-L72",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/GoldbachDeep.lean#L63-L72",
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
- Source path: [`TauLib/BookIII/Spectral/GoldbachDeep.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/GoldbachDeep.lean#L63-L72)
- Source range: L63-L72
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D102` — Sieve-Accelerated Goldbach

## Immediate Comment / Docstring

```lean
/-- [III.D102] Sieve-accelerated Goldbach check for all even n in [4..bound]. -/
```

## Source Excerpt

```lean
def goldbach_sieve_check (bound : Nat) : Bool :=
  go 4 (bound + 1)
where
  go (n fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if n > bound then true
    else
      let ok := n % 2 != 0 || goldbach_sieve_pair n
      ok && go (n + 1) (fuel - 1)
  termination_by fuel
```
