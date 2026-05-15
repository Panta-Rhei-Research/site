---
{
  "projection_kind": "taulib_declaration",
  "title": "towerVal",
  "permalink": "/corpus/taulib/docs/book-i-coordinates-iterated-prime/tower-val/",
  "summary_short": "`def` declaration in `TauLib.BookI.Coordinates.IteratedPrime`.",
  "declaration_id": "TauLib.BookI.Coordinates.IteratedPrime::towerVal",
  "declaration_slug": "tower-val",
  "kind": "def",
  "name": "towerVal",
  "module_name": "TauLib.BookI.Coordinates.IteratedPrime",
  "module_url": "/corpus/taulib/docs/book-i-coordinates-iterated-prime/",
  "source_line_start": 120,
  "source_line_end": 122,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/IteratedPrime.lean#L120-L122",
  "formal_status": "defined",
  "declaration_role": "data/computed value",
  "formal_status_label": "data/computed value",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Coordinates.IteratedPrime",
        "url": "/corpus/taulib/docs/book-i-coordinates-iterated-prime/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/IteratedPrime.lean#L120-L122",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "role": "data/computed value",
      "status": "data/computed value"
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

- Module: [TauLib.BookI.Coordinates.IteratedPrime](/corpus/taulib/docs/book-i-coordinates-iterated-prime/)
- Source path: [`TauLib/BookI/Coordinates/IteratedPrime.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/IteratedPrime.lean#L120-L122)
- Source range: L120-L122
- Kind: `def`
- Public role: `data/computed value`
- Formal status hint: `data/computed value`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Tower value with 1-indexed input (physics convention).
    towerVal 0 n = n (identity, α-orbit).
    towerVal 1 n = nthPrime(n-1) (primes, π-orbit, 1-indexed).
    towerVal 2 n = nthPrime(nthPrime(n-1) - 1) (super-primes, γ-orbit).
    The index shift accounts for nthPrime being 0-indexed. -/
```

## Source Excerpt

```lean
def towerVal : Nat → Nat → Nat
  | 0, n => n
  | k + 1, n => nthPrime (towerVal k n - 1)
```
