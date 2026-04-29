---
{
  "projection_kind": "taulib_declaration",
  "title": "tau_mem_mul_right",
  "permalink": "/verify/taulib/docs/book-i-sets-membership/tau-mem-mul-right/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Sets.Membership`.",
  "declaration_id": "TauLib.BookI.Sets.Membership::tau_mem_mul_right",
  "declaration_slug": "tau-mem-mul-right",
  "kind": "theorem",
  "name": "tau_mem_mul_right",
  "module_name": "TauLib.BookI.Sets.Membership",
  "module_url": "/verify/taulib/docs/book-i-sets-membership/",
  "source_line_start": 126,
  "source_line_end": 130,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/Membership.lean#L126-L130",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/Membership.lean#L126-L130",
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
- Source path: [`TauLib/BookI/Sets/Membership.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/Membership.lean#L126-L130)
- Source range: L126-L130
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Product membership: if a ∈_τ b, then a ∈_τ b*c. -/
```

## Source Excerpt

```lean
theorem tau_mem_mul_right {a b : TauIdx} (h : tau_mem a b) (c : TauIdx) :
    tau_mem a (idx_mul b c) := by
  rw [tau_mem_iff_dvd] at h ⊢
  rw [idx_mul_eq_nat_mul]
  exact Nat.dvd_trans h (Nat.dvd_mul_right b c)
```
