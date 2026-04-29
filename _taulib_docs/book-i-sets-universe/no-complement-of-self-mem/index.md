---
{
  "projection_kind": "taulib_declaration",
  "title": "no_complement_of_self_mem",
  "permalink": "/verify/taulib/docs/book-i-sets-universe/no-complement-of-self-mem/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Sets.Universe`.",
  "declaration_id": "TauLib.BookI.Sets.Universe::no_complement_of_self_mem",
  "declaration_slug": "no-complement-of-self-mem",
  "kind": "theorem",
  "name": "no_complement_of_self_mem",
  "module_name": "TauLib.BookI.Sets.Universe",
  "module_url": "/verify/taulib/docs/book-i-sets-universe/",
  "source_line_start": 80,
  "source_line_end": 84,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/Universe.lean#L80-L84",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/Universe.lean#L80-L84",
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
- Source path: [`TauLib/BookI/Sets/Universe.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/Universe.lean#L80-L84)
- Source range: L80-L84
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Variant: no τ-set separates members from non-members via complement.
    There is no τ-set C that contains exactly the non-self-members. -/
```

## Source Excerpt

```lean
theorem no_complement_of_self_mem :
    ¬ ∃ C : TauIdx, ∀ a : TauIdx, tau_mem a C ↔ ¬ tau_mem a a := by
  intro ⟨C, hC⟩
  have hCC : tau_mem C C := tau_mem_refl C
  exact (hC C).mp hCC hCC
```
