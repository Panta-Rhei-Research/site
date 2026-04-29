---
{
  "projection_kind": "taulib_declaration",
  "title": "goldbach_obstruction_count",
  "permalink": "/verify/taulib/docs/book-iii-spectral-goldbach-deep/goldbach-obstruction-count/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Spectral.GoldbachDeep`.",
  "declaration_id": "TauLib.BookIII.Spectral.GoldbachDeep::goldbach_obstruction_count",
  "declaration_slug": "goldbach-obstruction-count",
  "kind": "def",
  "name": "goldbach_obstruction_count",
  "module_name": "TauLib.BookIII.Spectral.GoldbachDeep",
  "module_url": "/verify/taulib/docs/book-iii-spectral-goldbach-deep/",
  "source_line_start": 117,
  "source_line_end": 119,
  "registry_ids": [
    "III.D104"
  ],
  "related_registry_items": [
    {
      "id": "III.D104",
      "title": "Goldbach Obstruction",
      "url": "/registry/object/III.D104/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/GoldbachDeep.lean#L117-L119",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/GoldbachDeep.lean#L117-L119",
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
- Source path: [`TauLib/BookIII/Spectral/GoldbachDeep.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/GoldbachDeep.lean#L117-L119)
- Source range: L117-L119
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D104` — Goldbach Obstruction

## Immediate Comment / Docstring

```lean
/-- [III.D104] Count obstructed residues at prime p for even n:
    r in [0..p-1] such that both r ≡ 0 AND (n-r) ≡ 0 (mod p).
    This equals 1 if p | n, and 0 otherwise. -/
```

## Source Excerpt

```lean
def goldbach_obstruction_count (n p : Nat) : Nat :=
  if p < 2 then 0
  else if n % p == 0 then 1 else 0
```
