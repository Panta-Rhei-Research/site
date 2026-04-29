---
{
  "projection_kind": "taulib_declaration",
  "title": "coprime_primorial_of_coprime_primes",
  "permalink": "/verify/taulib/docs/book-i-polarity-crtbasis/coprime-primorial-of-coprime-primes/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Polarity.CRTBasis`.",
  "declaration_id": "TauLib.BookI.Polarity.CRTBasis::coprime_primorial_of_coprime_primes",
  "declaration_slug": "coprime-primorial-of-coprime-primes",
  "kind": "theorem",
  "name": "coprime_primorial_of_coprime_primes",
  "module_name": "TauLib.BookI.Polarity.CRTBasis",
  "module_url": "/verify/taulib/docs/book-i-polarity-crtbasis/",
  "source_line_start": 72,
  "source_line_end": 86,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/CRTBasis.lean#L72-L86",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Polarity.CRTBasis",
        "url": "/verify/taulib/docs/book-i-polarity-crtbasis/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/CRTBasis.lean#L72-L86",
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

- Module: [TauLib.BookI.Polarity.CRTBasis](/verify/taulib/docs/book-i-polarity-crtbasis/)
- Source path: [`TauLib/BookI/Polarity/CRTBasis.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/CRTBasis.lean#L72-L86)
- Source range: L72-L86
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Any prime that is pairwise coprime to all primes in M_k is coprime to M_k. -/
```

## Source Excerpt

```lean
private theorem coprime_primorial_of_coprime_primes {m : TauIdx} :
    ∀ {k : TauIdx}, (∀ j, j < k → Nat.Coprime (nth_prime m) (nth_prime (j + 1))) →
    Nat.Coprime (nth_prime m) (primorial k) := by
  intro k
  induction k with
  | zero =>
    intro _
    show Nat.gcd (nth_prime m) 1 = 1
    exact Nat.gcd_one_right _
  | succ n ih =>
    intro h
    simp only [primorial]
    apply coprime_product_right
    · exact h n (by simp only [TauIdx]; omega)
    · exact ih (fun j hj => h j (by simp only [TauIdx] at *; omega))
```
