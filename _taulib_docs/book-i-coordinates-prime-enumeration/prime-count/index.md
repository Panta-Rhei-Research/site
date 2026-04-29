---
{
  "projection_kind": "taulib_declaration",
  "title": "prime_count",
  "permalink": "/verify/taulib/docs/book-i-coordinates-prime-enumeration/prime-count/",
  "summary_short": "`def` declaration in `TauLib.BookI.Coordinates.PrimeEnumeration`.",
  "declaration_id": "TauLib.BookI.Coordinates.PrimeEnumeration::prime_count",
  "declaration_slug": "prime-count",
  "kind": "def",
  "name": "prime_count",
  "module_name": "TauLib.BookI.Coordinates.PrimeEnumeration",
  "module_url": "/verify/taulib/docs/book-i-coordinates-prime-enumeration/",
  "source_line_start": 53,
  "source_line_end": 54,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/PrimeEnumeration.lean#L53-L54",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Coordinates.PrimeEnumeration",
        "url": "/verify/taulib/docs/book-i-coordinates-prime-enumeration/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/PrimeEnumeration.lean#L53-L54",
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

- Module: [TauLib.BookI.Coordinates.PrimeEnumeration](/verify/taulib/docs/book-i-coordinates-prime-enumeration/)
- Source path: [`TauLib/BookI/Coordinates/PrimeEnumeration.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/PrimeEnumeration.lean#L53-L54)
- Source range: L53-L54
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [I.D19f] Prime counting function π(n): number of primes ≤ n.
    Returns 0 for n < 2. -/
```

## Source Excerpt

```lean
def prime_count (n : TauIdx) : TauIdx :=
  if n < 2 then 0 else prime_count_go n 2 0 n
```
