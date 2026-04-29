---
{
  "projection_kind": "taulib_declaration",
  "title": "tau_inter_union_absorb",
  "permalink": "/verify/taulib/docs/book-i-sets-operations/tau-inter-union-absorb/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Sets.Operations`.",
  "declaration_id": "TauLib.BookI.Sets.Operations::tau_inter_union_absorb",
  "declaration_slug": "tau-inter-union-absorb",
  "kind": "theorem",
  "name": "tau_inter_union_absorb",
  "module_name": "TauLib.BookI.Sets.Operations",
  "module_url": "/verify/taulib/docs/book-i-sets-operations/",
  "source_line_start": 136,
  "source_line_end": 139,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/Operations.lean#L136-L139",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/Operations.lean#L136-L139",
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
- Source path: [`TauLib/BookI/Sets/Operations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/Operations.lean#L136-L139)
- Source range: L136-L139
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
No immediate Lean doc/comment block was detected for this declaration.
```

## Source Excerpt

```lean
theorem tau_inter_union_absorb (a b : TauIdx) :
    tau_inter a (tau_union a b) = a :=
  Nat.dvd_antisymm (Nat.gcd_dvd_left a _)
    (Nat.dvd_gcd (Nat.dvd_refl a) (Nat.dvd_lcm_left a b))
```
