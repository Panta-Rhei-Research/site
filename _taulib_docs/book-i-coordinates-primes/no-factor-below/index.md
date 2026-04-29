---
{
  "projection_kind": "taulib_declaration",
  "title": "no_factor_below",
  "permalink": "/verify/taulib/docs/book-i-coordinates-primes/no-factor-below/",
  "summary_short": "`def` declaration in `TauLib.BookI.Coordinates.Primes`.",
  "declaration_id": "TauLib.BookI.Coordinates.Primes::no_factor_below",
  "declaration_slug": "no-factor-below",
  "kind": "def",
  "name": "no_factor_below",
  "module_name": "TauLib.BookI.Coordinates.Primes",
  "module_url": "/verify/taulib/docs/book-i-coordinates-primes/",
  "source_line_start": 90,
  "source_line_end": 96,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/Primes.lean#L90-L96",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/Primes.lean#L90-L96",
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
- Source path: [`TauLib/BookI/Coordinates/Primes.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/Primes.lean#L90-L96)
- Source range: L90-L96
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Boolean primality check via trial division. -/
```

## Source Excerpt

```lean
def no_factor_below (n d : TauIdx) : Bool :=
  if d ≥ n then true
  else if d * d > n then true
  else if n % d = 0 then false
  else no_factor_below n (d + 1)
termination_by n - d
decreasing_by simp_wf; simp only [TauIdx] at *; omega
```
