---
{
  "projection_kind": "taulib_declaration",
  "title": "nth_prime_go",
  "permalink": "/verify/taulib/docs/book-i-polarity-mod-arith/nth-prime-go/",
  "summary_short": "`def` declaration in `TauLib.BookI.Polarity.ModArith`.",
  "declaration_id": "TauLib.BookI.Polarity.ModArith::nth_prime_go",
  "declaration_slug": "nth-prime-go",
  "kind": "def",
  "name": "nth_prime_go",
  "module_name": "TauLib.BookI.Polarity.ModArith",
  "module_url": "/verify/taulib/docs/book-i-polarity-mod-arith/",
  "source_line_start": 30,
  "source_line_end": 39,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/ModArith.lean#L30-L39",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Polarity.ModArith",
        "url": "/verify/taulib/docs/book-i-polarity-mod-arith/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/ModArith.lean#L30-L39",
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

- Module: [TauLib.BookI.Polarity.ModArith](/verify/taulib/docs/book-i-polarity-mod-arith/)
- Source path: [`TauLib/BookI/Polarity/ModArith.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/ModArith.lean#L30-L39)
- Source range: L30-L39
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Find the k-th prime by trial (1-indexed: nth_prime 1 = 2). -/
```

## Source Excerpt

```lean
def nth_prime_go (target count cur : Nat) (fuel : Nat) : Nat :=
  if fuel = 0 then cur
  else if count == target then cur
  else
    let next := cur + 1
    if is_prime_bool next then
      nth_prime_go target (count + 1) next (fuel - 1)
    else
      nth_prime_go target count next (fuel - 1)
termination_by fuel
```
