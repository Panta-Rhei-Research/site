---
{
  "projection_kind": "taulib_declaration",
  "title": "crt_unique_mod",
  "permalink": "/verify/taulib/docs/book-i-polarity-crtbasis/crt-unique-mod/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Polarity.CRTBasis`.",
  "declaration_id": "TauLib.BookI.Polarity.CRTBasis::crt_unique_mod",
  "declaration_slug": "crt-unique-mod",
  "kind": "theorem",
  "name": "crt_unique_mod",
  "module_name": "TauLib.BookI.Polarity.CRTBasis",
  "module_url": "/verify/taulib/docs/book-i-polarity-crtbasis/",
  "source_line_start": 280,
  "source_line_end": 296,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/CRTBasis.lean#L280-L296",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/CRTBasis.lean#L280-L296",
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
- Source path: [`TauLib/BookI/Polarity/CRTBasis.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/CRTBasis.lean#L280-L296)
- Source range: L280-L296
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- CRT uniqueness: pointwise agreement at each prime implies agreement
    modulo the primorial. -/
```

## Source Excerpt

```lean
theorem crt_unique_mod : ∀ {k : TauIdx}, CRTHyp k →
    ∀ {a b : TauIdx},
    (∀ l, l < k → a % nth_prime (l + 1) = b % nth_prime (l + 1)) →
    a % primorial k = b % primorial k := by
  intro k; induction k with
  | zero => intro _ _ _ _; simp only [primorial, Nat.mod_one]
  | succ n ih =>
    intro hyp a b h
    simp only [primorial]
    apply mod_eq_of_coprime_mod_eq (prime_coprime_primorial hyp)
    · exact h n (by simp only [TauIdx]; omega)
    · exact ih
        ⟨fun j hj => hyp.all_prime j (by simp only [TauIdx] at *; omega),
         fun j l hj hl hjl => hyp.pairwise_coprime j l
           (by simp only [TauIdx] at *; omega)
           (by simp only [TauIdx] at *; omega) hjl⟩
        (fun l hl => h l (by simp only [TauIdx] at *; omega))
```
