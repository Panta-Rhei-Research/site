---
{
  "projection_kind": "taulib_declaration",
  "title": "starting_primes_all_prime",
  "permalink": "/verify/taulib/docs/book-ii-interior-abcdrigidity/starting-primes-all-prime/",
  "summary_short": "`def` declaration in `TauLib.BookII.Interior.ABCDRigidity`.",
  "declaration_id": "TauLib.BookII.Interior.ABCDRigidity::starting_primes_all_prime",
  "declaration_slug": "starting-primes-all-prime",
  "kind": "def",
  "name": "starting_primes_all_prime",
  "module_name": "TauLib.BookII.Interior.ABCDRigidity",
  "module_url": "/verify/taulib/docs/book-ii-interior-abcdrigidity/",
  "source_line_start": 101,
  "source_line_end": 102,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Interior/ABCDRigidity.lean#L101-L102",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Interior.ABCDRigidity",
        "url": "/verify/taulib/docs/book-ii-interior-abcdrigidity/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Interior/ABCDRigidity.lean#L101-L102",
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

- Module: [TauLib.BookII.Interior.ABCDRigidity](/verify/taulib/docs/book-ii-interior-abcdrigidity/)
- Source path: [`TauLib/BookII/Interior/ABCDRigidity.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Interior/ABCDRigidity.lean#L101-L102)
- Source range: L101-L102
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The four starting primes are all prime. -/
```

## Source Excerpt

```lean
def starting_primes_all_prime : Bool :=
  four_starting_primes.all is_prime_bool
```
