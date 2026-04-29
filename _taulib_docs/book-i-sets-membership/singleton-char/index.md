---
{
  "projection_kind": "taulib_declaration",
  "title": "singleton_char",
  "permalink": "/verify/taulib/docs/book-i-sets-membership/singleton-char/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Sets.Membership`.",
  "declaration_id": "TauLib.BookI.Sets.Membership::singleton_char",
  "declaration_slug": "singleton-char",
  "kind": "theorem",
  "name": "singleton_char",
  "module_name": "TauLib.BookI.Sets.Membership",
  "module_url": "/verify/taulib/docs/book-i-sets-membership/",
  "source_line_start": 100,
  "source_line_end": 119,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/Membership.lean#L100-L119",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Sets.Membership",
        "url": "/verify/taulib/docs/book-i-sets-membership/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/Membership.lean#L100-L119",
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

- Module: [TauLib.BookI.Sets.Membership](/verify/taulib/docs/book-i-sets-membership/)
- Source path: [`TauLib/BookI/Sets/Membership.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/Membership.lean#L100-L119)
- Source range: L100-L119
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- A nonzero τ-set p is a singleton (only 1 and p are τ-members) iff p = 1 or p is prime. -/
```

## Source Excerpt

```lean
theorem singleton_char (p : TauIdx) (hp0 : p ≠ 0) :
    (∀ d : TauIdx, tau_mem d p → d = 1 ∨ d = p) ↔ (p = 1 ∨ idx_prime p) := by
  constructor
  · intro h
    by_cases hp1 : p = 1
    · exact Or.inl hp1
    · right
      constructor
      · rcases p with _ | _ | n
        · exact absurd rfl hp0
        · exact absurd rfl hp1
        · exact Nat.le_add_left 2 n
      · intro d hd
        exact h d ((idx_divides_iff_nat_dvd d p).mpr hd)
  · intro h d hd
    rcases h with rfl | hp
    · -- p = 1
      exact Or.inl (Nat.eq_one_of_dvd_one ((idx_divides_iff_nat_dvd d 1).mp hd))
    · -- p is prime
      exact hp.2 d ((idx_divides_iff_nat_dvd d p).mp hd)
```
