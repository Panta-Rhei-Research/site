---
{
  "projection_kind": "taulib_declaration",
  "title": "no_russell_set",
  "permalink": "/verify/taulib/docs/book-i-sets-universe/no-russell-set/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Sets.Universe`.",
  "declaration_id": "TauLib.BookI.Sets.Universe::no_russell_set",
  "declaration_slug": "no-russell-set",
  "kind": "theorem",
  "name": "no_russell_set",
  "module_name": "TauLib.BookI.Sets.Universe",
  "module_url": "/verify/taulib/docs/book-i-sets-universe/",
  "source_line_start": 71,
  "source_line_end": 76,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/Universe.lean#L71-L76",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Sets.Universe",
        "url": "/verify/taulib/docs/book-i-sets-universe/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/Universe.lean#L71-L76",
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

- Module: [TauLib.BookI.Sets.Universe](/verify/taulib/docs/book-i-sets-universe/)
- Source path: [`TauLib/BookI/Sets/Universe.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/Universe.lean#L71-L76)
- Source range: L71-L76
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [I.P13b] No Russell Set: there is no τ-set R such that
    for all a, a ∈_τ R iff ¬(a ∈_τ R).

    Proof by contradiction: if such R existed, then applying
    the biconditional to a = R gives R ∈_τ R ↔ ¬(R ∈_τ R).
    But R ∈_τ R always holds (since R | R), so we get
    True ↔ False, a contradiction. -/
```

## Source Excerpt

```lean
theorem no_russell_set :
    ¬ ∃ R : TauIdx, ∀ a : TauIdx, tau_mem a R ↔ ¬ tau_mem a R := by
  intro ⟨R, hR⟩
  have h := hR R
  have hRR : tau_mem R R := tau_mem_refl R
  exact (h.mp hRR) hRR
```
