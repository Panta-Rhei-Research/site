---
{
  "projection_kind": "taulib_declaration",
  "title": "p_adic_val",
  "permalink": "/verify/taulib/docs/book-i-coordinates-primes/p-adic-val/",
  "summary_short": "`def` declaration in `TauLib.BookI.Coordinates.Primes`.",
  "declaration_id": "TauLib.BookI.Coordinates.Primes::p_adic_val",
  "declaration_slug": "p-adic-val",
  "kind": "def",
  "name": "p_adic_val",
  "module_name": "TauLib.BookI.Coordinates.Primes",
  "module_url": "/verify/taulib/docs/book-i-coordinates-primes/",
  "source_line_start": 414,
  "source_line_end": 424,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/Primes.lean#L414-L424",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Coordinates.Primes",
        "url": "/verify/taulib/docs/book-i-coordinates-primes/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/Primes.lean#L414-L424",
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

- Module: [TauLib.BookI.Coordinates.Primes](/verify/taulib/docs/book-i-coordinates-primes/)
- Source path: [`TauLib/BookI/Coordinates/Primes.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/Primes.lean#L414-L424)
- Source range: L414-L424
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- p-adic valuation: how many times p divides n. -/
```

## Source Excerpt

```lean
def p_adic_val (p n : TauIdx) : TauIdx :=
  if p ≤ 1 then 0
  else if n = 0 then 0
  else go p n n
where
  go (p n fuel : TauIdx) : TauIdx :=
    if fuel = 0 then 0
    else if n % p = 0 then 1 + go p (n / p) (fuel - 1)
    else 0
  termination_by fuel
  decreasing_by simp_wf; simp only [TauIdx] at *; omega
```
