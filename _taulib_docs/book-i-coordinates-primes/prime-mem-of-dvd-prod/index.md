---
{
  "projection_kind": "taulib_declaration",
  "title": "prime_mem_of_dvd_prod",
  "permalink": "/verify/taulib/docs/book-i-coordinates-primes/prime-mem-of-dvd-prod/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Coordinates.Primes`.",
  "declaration_id": "TauLib.BookI.Coordinates.Primes::prime_mem_of_dvd_prod",
  "declaration_slug": "prime-mem-of-dvd-prod",
  "kind": "theorem",
  "name": "prime_mem_of_dvd_prod",
  "module_name": "TauLib.BookI.Coordinates.Primes",
  "module_url": "/verify/taulib/docs/book-i-coordinates-primes/",
  "source_line_start": 305,
  "source_line_end": 320,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/Primes.lean#L305-L320",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/Primes.lean#L305-L320",
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
- Source path: [`TauLib/BookI/Coordinates/Primes.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/Primes.lean#L305-L320)
- Source range: L305-L320
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- If p is prime and p divides a product of primes, then p is in the list. -/
```

## Source Excerpt

```lean
theorem prime_mem_of_dvd_prod {p : TauIdx} (hp : idx_prime p)
    {ps : List TauIdx} (hps : ∀ q ∈ ps, idx_prime q) (hdvd : p ∣ list_prod ps) :
    p ∈ ps := by
  induction ps with
  | nil =>
    simp [list_prod] at hdvd
    obtain ⟨k, hk⟩ := hdvd; have := hp.1; simp only [TauIdx] at *; omega
  | cons q rest ih =>
    simp only [list_prod] at hdvd
    rcases euclid_lemma hp hdvd with h | h
    · -- p | q, both prime → p = q
      rcases (hps q (by simp)).2 p h with h' | h'
      · exfalso; have := hp.1; simp only [TauIdx] at *; omega
      · exact List.mem_cons.mpr (Or.inl h')
    · exact List.mem_cons.mpr (Or.inr
        (ih (fun q hq => hps q (List.mem_cons_of_mem _ hq)) h))
```
