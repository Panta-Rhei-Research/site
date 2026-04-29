---
{
  "projection_kind": "taulib_declaration",
  "title": "tau_inter_distrib_union",
  "permalink": "/verify/taulib/docs/book-i-sets-operations/tau-inter-distrib-union/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Sets.Operations`.",
  "declaration_id": "TauLib.BookI.Sets.Operations::tau_inter_distrib_union",
  "declaration_slug": "tau-inter-distrib-union",
  "kind": "theorem",
  "name": "tau_inter_distrib_union",
  "module_name": "TauLib.BookI.Sets.Operations",
  "module_url": "/verify/taulib/docs/book-i-sets-operations/",
  "source_line_start": 289,
  "source_line_end": 292,
  "registry_ids": [
    "I.P11"
  ],
  "related_registry_items": [
    {
      "id": "I.P11",
      "title": "Distributive Lattice",
      "url": "/registry/object/I.P11/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/Operations.lean#L289-L292",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Sets.Operations",
        "url": "/verify/taulib/docs/book-i-sets-operations/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/Operations.lean#L289-L292",
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

- Module: [TauLib.BookI.Sets.Operations](/verify/taulib/docs/book-i-sets-operations/)
- Source path: [`TauLib/BookI/Sets/Operations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/Operations.lean#L289-L292)
- Source range: L289-L292
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `I.P11` — Distributive Lattice

## Immediate Comment / Docstring

```lean
/-- [I.P11] Distributive Lattice: gcd distributes over lcm.
    gcd(a, lcm(b,c)) = lcm(gcd(a,b), gcd(a,c)). -/
```

## Source Excerpt

```lean
theorem tau_inter_distrib_union (a b c : TauIdx) :
    tau_inter a (tau_union b c) = tau_union (tau_inter a b) (tau_inter a c) := by
  unfold tau_inter tau_union idx_gcd
  exact nat_gcd_distrib_lcm a b c
```
