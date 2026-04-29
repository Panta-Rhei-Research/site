---
{
  "projection_kind": "taulib_declaration",
  "title": "tau_unit_char",
  "permalink": "/verify/taulib/docs/book-i-sets-membership/tau-unit-char/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Sets.Membership`.",
  "declaration_id": "TauLib.BookI.Sets.Membership::tau_unit_char",
  "declaration_slug": "tau-unit-char",
  "kind": "theorem",
  "name": "tau_unit_char",
  "module_name": "TauLib.BookI.Sets.Membership",
  "module_url": "/verify/taulib/docs/book-i-sets-membership/",
  "source_line_start": 93,
  "source_line_end": 97,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/Membership.lean#L93-L97",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/Membership.lean#L93-L97",
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
- Source path: [`TauLib/BookI/Sets/Membership.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/Membership.lean#L93-L97)
- Source range: L93-L97
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The unit has no members other than itself: if a ∈_τ 1, then a = 1. -/
```

## Source Excerpt

```lean
theorem tau_unit_char (a : TauIdx) (h : tau_mem a tau_unit) : a = 1 := by
  unfold tau_unit at h
  unfold tau_mem at h
  rw [idx_divides_iff_nat_dvd] at h
  exact Nat.eq_one_of_dvd_one h
```
