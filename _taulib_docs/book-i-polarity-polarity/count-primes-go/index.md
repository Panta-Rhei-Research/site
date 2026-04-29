---
{
  "projection_kind": "taulib_declaration",
  "title": "count_primes_go",
  "permalink": "/verify/taulib/docs/book-i-polarity-polarity/count-primes-go/",
  "summary_short": "`def` declaration in `TauLib.BookI.Polarity.Polarity`.",
  "declaration_id": "TauLib.BookI.Polarity.Polarity::count_primes_go",
  "declaration_slug": "count-primes-go",
  "kind": "def",
  "name": "count_primes_go",
  "module_name": "TauLib.BookI.Polarity.Polarity",
  "module_url": "/verify/taulib/docs/book-i-polarity-polarity/",
  "source_line_start": 208,
  "source_line_end": 214,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/Polarity.lean#L208-L214",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Polarity.Polarity",
        "url": "/verify/taulib/docs/book-i-polarity-polarity/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/Polarity.lean#L208-L214",
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

- Module: [TauLib.BookI.Polarity.Polarity](/verify/taulib/docs/book-i-polarity-polarity/)
- Source path: [`TauLib/BookI/Polarity/Polarity.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/Polarity.lean#L208-L214)
- Source range: L208-L214
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Count total primes among 2..n. -/
```

## Source Excerpt

```lean
def count_primes_go (i n : Nat) (acc : Nat) (fuel : Nat) : Nat :=
  if fuel = 0 then acc
  else if i > n then acc
  else
    let acc' := if is_prime_bool i then acc + 1 else acc
    count_primes_go (i + 1) n acc' (fuel - 1)
termination_by fuel
```
