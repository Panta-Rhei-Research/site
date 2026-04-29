---
{
  "projection_kind": "taulib_declaration",
  "title": "prod_one_implies_nil",
  "permalink": "/verify/taulib/docs/book-i-coordinates-primes/prod-one-implies-nil/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Coordinates.Primes`.",
  "declaration_id": "TauLib.BookI.Coordinates.Primes::prod_one_implies_nil",
  "declaration_slug": "prod-one-implies-nil",
  "kind": "theorem",
  "name": "prod_one_implies_nil",
  "module_name": "TauLib.BookI.Coordinates.Primes",
  "module_url": "/verify/taulib/docs/book-i-coordinates-primes/",
  "source_line_start": 292,
  "source_line_end": 302,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/Primes.lean#L292-L302",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/Primes.lean#L292-L302",
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

- Module: [TauLib.BookI.Coordinates.Primes](/verify/taulib/docs/book-i-coordinates-primes/)
- Source path: [`TauLib/BookI/Coordinates/Primes.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/Primes.lean#L292-L302)
- Source range: L292-L302
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Product of primes = 1 implies empty list. -/
```

## Source Excerpt

```lean
private theorem prod_one_implies_nil (ps : List TauIdx)
    (hps : ∀ p ∈ ps, idx_prime p) (h1 : list_prod ps = 1) : ps = [] := by
  rcases ps with _ | ⟨p, rest⟩
  · rfl
  · exfalso
    simp only [list_prod] at h1
    have hp : p ≥ 2 := (hps p (by simp)).1
    have hr : list_prod rest ≥ 1 :=
      list_prod_pos_of_primes rest (fun q hq => hps q (List.mem_cons_of_mem p hq))
    have := Nat.mul_le_mul hp hr
    simp only [TauIdx] at *; omega
```
