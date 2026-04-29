---
{
  "projection_kind": "taulib_declaration",
  "title": "nth_prime_go_ge",
  "permalink": "/verify/taulib/docs/book-i-polarity-mod-arith/nth-prime-go-ge/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Polarity.ModArith`.",
  "declaration_id": "TauLib.BookI.Polarity.ModArith::nth_prime_go_ge",
  "declaration_slug": "nth-prime-go-ge",
  "kind": "theorem",
  "name": "nth_prime_go_ge",
  "module_name": "TauLib.BookI.Polarity.ModArith",
  "module_url": "/verify/taulib/docs/book-i-polarity-mod-arith/",
  "source_line_start": 114,
  "source_line_end": 131,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/ModArith.lean#L114-L131",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/ModArith.lean#L114-L131",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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
- Source path: [`TauLib/BookI/Polarity/ModArith.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/ModArith.lean#L114-L131)
- Source range: L114-L131
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- nth_prime_go always returns a value ≥ cur. -/
```

## Source Excerpt

```lean
theorem nth_prime_go_ge (target count cur fuel : Nat) :
    nth_prime_go target count cur fuel ≥ cur := by
  induction fuel generalizing count cur with
  | zero => unfold nth_prime_go; simp
  | succ n ih =>
    unfold nth_prime_go
    simp only [Nat.succ_ne_zero, ↓reduceIte]
    split
    · -- count == target: returns cur
      exact Nat.le_refl cur
    · -- count ≠ target: recurses with next = cur + 1
      split
      · -- is_prime_bool (cur + 1): recurse with (count+1, cur+1)
        show nth_prime_go target (count + 1) (cur + 1) n ≥ cur
        exact Nat.le_trans (Nat.le_succ cur) (ih (count + 1) (cur + 1))
      · -- not prime: recurse with (count, cur+1)
        show nth_prime_go target count (cur + 1) n ≥ cur
        exact Nat.le_trans (Nat.le_succ cur) (ih count (cur + 1))
```
