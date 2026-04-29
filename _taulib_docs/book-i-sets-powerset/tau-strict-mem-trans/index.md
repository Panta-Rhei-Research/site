---
{
  "projection_kind": "taulib_declaration",
  "title": "tau_strict_mem_trans",
  "permalink": "/verify/taulib/docs/book-i-sets-powerset/tau-strict-mem-trans/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Sets.Powerset`.",
  "declaration_id": "TauLib.BookI.Sets.Powerset::tau_strict_mem_trans",
  "declaration_slug": "tau-strict-mem-trans",
  "kind": "theorem",
  "name": "tau_strict_mem_trans",
  "module_name": "TauLib.BookI.Sets.Powerset",
  "module_url": "/verify/taulib/docs/book-i-sets-powerset/",
  "source_line_start": 46,
  "source_line_end": 50,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/Powerset.lean#L46-L50",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/Powerset.lean#L46-L50",
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
- Source path: [`TauLib/BookI/Sets/Powerset.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/Powerset.lean#L46-L50)
- Source range: L46-L50
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Strict membership is transitive. -/
```

## Source Excerpt

```lean
theorem tau_strict_mem_trans {a b c : TauIdx}
    (h1 : tau_strict_mem a b) (h2 : tau_strict_mem b c) :
    tau_strict_mem a c :=
  ⟨tau_mem_trans h1.1 h2.1, fun h => by
    subst h; exact h1.2 (tau_mem_antisymm h1.1 h2.1)⟩
```
