---
{
  "projection_kind": "taulib_declaration",
  "title": "Pol_trichotomy_at_first_nine_primes",
  "permalink": "/verify/taulib/docs/book-i-polarity-prime-polarity-isomorphism/pol-trichotomy-at-first-nine-primes/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Polarity.PrimePolarityIsomorphism`.",
  "declaration_id": "TauLib.BookI.Polarity.PrimePolarityIsomorphism::Pol_trichotomy_at_first_nine_primes",
  "declaration_slug": "pol-trichotomy-at-first-nine-primes",
  "kind": "theorem",
  "name": "Pol_trichotomy_at_first_nine_primes",
  "module_name": "TauLib.BookI.Polarity.PrimePolarityIsomorphism",
  "module_url": "/verify/taulib/docs/book-i-polarity-prime-polarity-isomorphism/",
  "source_line_start": 194,
  "source_line_end": 226,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/PrimePolarityIsomorphism.lean#L194-L226",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Polarity.PrimePolarityIsomorphism",
        "url": "/verify/taulib/docs/book-i-polarity-prime-polarity-isomorphism/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/PrimePolarityIsomorphism.lean#L194-L226",
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

- Module: [TauLib.BookI.Polarity.PrimePolarityIsomorphism](/verify/taulib/docs/book-i-polarity-prime-polarity-isomorphism/)
- Source path: [`TauLib/BookI/Polarity/PrimePolarityIsomorphism.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/PrimePolarityIsomorphism.lean#L194-L226)
- Source range: L194-L226
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Paper Corollary 7.2(2) — disjoint partition at small primes**:
    `Pol(p)` returns one of `{-1, 0, +1}` at every concrete prime.

    Verified via `native_decide` at the first 9 primes (2, 3, 5, 7,
    11, 13, 17, 19, 23) — the same range used in Wave 18's
    classifier verification.  The general structural claim "for
    every prime p, `Pol(p) ∈ {-1, 0, 1}`" follows from the chi_p
    definition's branch-returning behaviour, but the universal
    proof involves case analysis on `modPow`'s output that requires
    more analytic infrastructure than TauLib's tactics-only budget;
    deferred and recorded as paper-side. -/
```

## Source Excerpt

```lean
theorem Pol_trichotomy_at_first_nine_primes :
    (Pol 2 = -1 ∨ Pol 2 = 0 ∨ Pol 2 = 1) ∧
    (Pol 3 = -1 ∨ Pol 3 = 0 ∨ Pol 3 = 1) ∧
    (Pol 5 = -1 ∨ Pol 5 = 0 ∨ Pol 5 = 1) ∧
    (Pol 7 = -1 ∨ Pol 7 = 0 ∨ Pol 7 = 1) ∧
    (Pol 11 = -1 ∨ Pol 11 = 0 ∨ Pol 11 = 1) ∧
    (Pol 13 = -1 ∨ Pol 13 = 0 ∨ Pol 13 = 1) ∧
    (Pol 17 = -1 ∨ Pol 17 = 0 ∨ Pol 17 = 1) ∧
    (Pol 19 = -1 ∨ Pol 19 = 0 ∨ Pol 19 = 1) ∧
    (Pol 23 = -1 ∨ Pol 23 = 0 ∨ Pol 23 = 1) := by
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_⟩
  · right; left; native_decide   -- Pol 2 = 0
  · left; native_decide            -- Pol 3 = -1
  · left; native_decide            -- Pol 5 = -1
  · right; right; native_decide    -- Pol 7 = +1
  · left; native_decide            -- Pol 11 = -1
  · left; native_decide            -- Pol 13 = -1
  · right; right; native_decide    -- Pol 17 = +1
  · left; native_decide            -- Pol 19 = -1
  · right; right; native_decide    -- Pol 23 = +1

-- ============================================================
-- PART 6: H3 ↔ H2 unified-classifier corollary
-- ============================================================

/-- **The unified classifier** as a single function. By the
    Isomorphism Theorem, we may use either name interchangeably. -/
abbrev unifiedClassifier (i : TauIdx) : Int := labelInfty i

/-- The unified classifier matches Pol at every prime index. -/
@[simp] theorem unifiedClassifier_eq_Pol (i : TauIdx) :
    unifiedClassifier i = Pol (nth_prime (i + 1)) :=
  labelInfty_eq_Pol_at_index i
```
