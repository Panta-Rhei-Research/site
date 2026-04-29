---
{
  "projection_kind": "taulib_declaration",
  "title": "orbit_set_alpha_eq_tau_mem",
  "permalink": "/verify/taulib/docs/book-i-sets-orbit-sets/orbit-set-alpha-eq-tau-mem/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Sets.OrbitSets`.",
  "declaration_id": "TauLib.BookI.Sets.OrbitSets::orbit_set_alpha_eq_tau_mem",
  "declaration_slug": "orbit-set-alpha-eq-tau-mem",
  "kind": "theorem",
  "name": "orbit_set_alpha_eq_tau_mem",
  "module_name": "TauLib.BookI.Sets.OrbitSets",
  "module_url": "/verify/taulib/docs/book-i-sets-orbit-sets/",
  "source_line_start": 76,
  "source_line_end": 78,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/OrbitSets.lean#L76-L78",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Sets.OrbitSets",
        "url": "/verify/taulib/docs/book-i-sets-orbit-sets/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/OrbitSets.lean#L76-L78",
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

- Module: [TauLib.BookI.Sets.OrbitSets](/verify/taulib/docs/book-i-sets-orbit-sets/)
- Source path: [`TauLib/BookI/Sets/OrbitSets.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/OrbitSets.lean#L76-L78)
- Source range: L76-L78
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The orbit-set for α IS τ-membership — by definition.
    This is a definitional identity, not just a propositional equivalence.
    Part VIII's single-orbit set theory (∈_τ = divisibility) and the
    five-orbit representation theory of Chapter 83 are one theory. -/
```

## Source Excerpt

```lean
theorem orbit_set_alpha_eq_tau_mem (n k : TauIdx) :
    orbit_set_alpha n k ↔ tau_mem k n :=
  Iff.rfl
```
