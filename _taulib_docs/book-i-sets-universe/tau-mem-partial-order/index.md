---
{
  "projection_kind": "taulib_declaration",
  "title": "tau_mem_partial_order",
  "permalink": "/verify/taulib/docs/book-i-sets-universe/tau-mem-partial-order/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Sets.Universe`.",
  "declaration_id": "TauLib.BookI.Sets.Universe::tau_mem_partial_order",
  "declaration_slug": "tau-mem-partial-order",
  "kind": "theorem",
  "name": "tau_mem_partial_order",
  "module_name": "TauLib.BookI.Sets.Universe",
  "module_url": "/verify/taulib/docs/book-i-sets-universe/",
  "source_line_start": 141,
  "source_line_end": 145,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/Universe.lean#L141-L145",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/Universe.lean#L141-L145",
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
- Source path: [`TauLib/BookI/Sets/Universe.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/Universe.lean#L141-L145)
- Source range: L141-L145
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The τ-universe is a partial order (preorder + antisymmetry). -/
```

## Source Excerpt

```lean
theorem tau_mem_partial_order :
    (∀ a : TauIdx, tau_mem a a) ∧
    (∀ a b : TauIdx, tau_mem a b → tau_mem b a → a = b) ∧
    (∀ a b c : TauIdx, tau_mem a b → tau_mem b c → tau_mem a c) :=
  ⟨tau_mem_refl, fun _ _ => tau_mem_antisymm, fun _ _ _ => tau_mem_trans⟩
```
