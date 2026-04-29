---
{
  "projection_kind": "taulib_declaration",
  "title": "obstruction_bounded_check",
  "permalink": "/verify/taulib/docs/book-iii-spectral-goldbach-deep/obstruction-bounded-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Spectral.GoldbachDeep`.",
  "declaration_id": "TauLib.BookIII.Spectral.GoldbachDeep::obstruction_bounded_check",
  "declaration_slug": "obstruction-bounded-check",
  "kind": "def",
  "name": "obstruction_bounded_check",
  "module_name": "TauLib.BookIII.Spectral.GoldbachDeep",
  "module_url": "/verify/taulib/docs/book-iii-spectral-goldbach-deep/",
  "source_line_start": 122,
  "source_line_end": 133,
  "registry_ids": [
    "III.T71"
  ],
  "related_registry_items": [
    {
      "id": "III.T71",
      "title": "Obstruction Bounded",
      "url": "/registry/object/III.T71/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/GoldbachDeep.lean#L122-L133",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/GoldbachDeep.lean#L122-L133",
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
- Source path: [`TauLib/BookIII/Spectral/GoldbachDeep.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/GoldbachDeep.lean#L122-L133)
- Source range: L122-L133
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.T71` — Obstruction Bounded

## Immediate Comment / Docstring

```lean
/-- [III.T71] Obstruction at each prime is at most 1. -/
```

## Source Excerpt

```lean
def obstruction_bounded_check (bound db : Nat) : Bool :=
  go 4 1 ((bound + 1) * (db + 1))
where
  go (n k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if n > bound then true
    else if k > db then go (n + 2) 1 (fuel - 1)
    else
      let p := nth_prime k
      let obs := goldbach_obstruction_count n p
      (obs <= 1) && go n (k + 1) (fuel - 1)
  termination_by fuel
```
