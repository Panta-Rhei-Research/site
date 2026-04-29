---
{
  "projection_kind": "taulib_declaration",
  "title": "tau_strict_mem_wf",
  "permalink": "/verify/taulib/docs/book-i-sets-powerset/tau-strict-mem-wf/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Sets.Powerset`.",
  "declaration_id": "TauLib.BookI.Sets.Powerset::tau_strict_mem_wf",
  "declaration_slug": "tau-strict-mem-wf",
  "kind": "theorem",
  "name": "tau_strict_mem_wf",
  "module_name": "TauLib.BookI.Sets.Powerset",
  "module_url": "/verify/taulib/docs/book-i-sets-powerset/",
  "source_line_start": 97,
  "source_line_end": 100,
  "registry_ids": [
    "I.P12"
  ],
  "related_registry_items": [
    {
      "id": "I.P12",
      "title": "Countability of Set(tau)",
      "url": "/registry/object/I.P12/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/Powerset.lean#L97-L100",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Sets.Powerset",
        "url": "/verify/taulib/docs/book-i-sets-powerset/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/Powerset.lean#L97-L100",
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

- Module: [TauLib.BookI.Sets.Powerset](/verify/taulib/docs/book-i-sets-powerset/)
- Source path: [`TauLib/BookI/Sets/Powerset.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/Powerset.lean#L97-L100)
- Source range: L97-L100
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `I.P12` — Countability of Set(tau)

## Immediate Comment / Docstring

```lean
/-- [I.P12] Well-foundedness of nonzero strict τ-membership:
    there is no infinite descending chain
    ... ∈^strict_τ x₂ ∈^strict_τ x₁ ∈^strict_τ x₀
    when all elements are nonzero.

    Proof: tau_strict_mem_nz is a subrelation of Nat.lt (via identity),
    and Nat.lt is well-founded. -/
```

## Source Excerpt

```lean
theorem tau_strict_mem_wf : WellFounded tau_strict_mem_nz :=
  Subrelation.wf
    (fun h => strict_mem_nz_sub_lt h)
    (InvImage.wf id Nat.lt_wfRel.wf)
```
