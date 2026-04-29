---
{
  "projection_kind": "taulib_declaration",
  "title": "tau_mem_iff_dvd",
  "permalink": "/verify/taulib/docs/book-i-sets-membership/tau-mem-iff-dvd/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Sets.Membership`.",
  "declaration_id": "TauLib.BookI.Sets.Membership::tau_mem_iff_dvd",
  "declaration_slug": "tau-mem-iff-dvd",
  "kind": "theorem",
  "name": "tau_mem_iff_dvd",
  "module_name": "TauLib.BookI.Sets.Membership",
  "module_url": "/verify/taulib/docs/book-i-sets-membership/",
  "source_line_start": 52,
  "source_line_end": 57,
  "registry_ids": [
    "I.P10"
  ],
  "related_registry_items": [
    {
      "id": "I.P10",
      "title": "Membership Decidability",
      "url": "/registry/object/I.P10/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/Membership.lean#L52-L57",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/Membership.lean#L52-L57",
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
- Source path: [`TauLib/BookI/Sets/Membership.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/Membership.lean#L52-L57)
- Source range: L52-L57
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `I.P10` — Membership Decidability

## Immediate Comment / Docstring

```lean
/-- Bridge: τ-membership is Nat divisibility. -/
```

## Source Excerpt

```lean
theorem tau_mem_iff_dvd (a b : TauIdx) : tau_mem a b ↔ a ∣ b :=
  idx_divides_iff_nat_dvd a b

/-- [I.P10] τ-membership is decidable. -/
instance instDecidableTauMem (a b : TauIdx) : Decidable (tau_mem a b) :=
  instDecidableIdxDivides a b
```
