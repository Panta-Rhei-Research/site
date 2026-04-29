---
{
  "projection_kind": "taulib_declaration",
  "title": "diverge_go_self",
  "permalink": "/verify/taulib/docs/book-i-denotation-structural/diverge-go-self/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Denotation.Structural`.",
  "declaration_id": "TauLib.BookI.Denotation.Structural::diverge_go_self",
  "declaration_slug": "diverge-go-self",
  "kind": "theorem",
  "name": "diverge_go_self",
  "module_name": "TauLib.BookI.Denotation.Structural",
  "module_url": "/verify/taulib/docs/book-i-denotation-structural/",
  "source_line_start": 282,
  "source_line_end": 291,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/Structural.lean#L282-L291",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Denotation.Structural",
        "url": "/verify/taulib/docs/book-i-denotation-structural/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/Structural.lean#L282-L291",
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

- Module: [TauLib.BookI.Denotation.Structural](/verify/taulib/docs/book-i-denotation-structural/)
- Source path: [`TauLib/BookI/Denotation/Structural.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/Structural.lean#L282-L291)
- Source range: L282-L291
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Helper: diverge_go on identical lists always returns 0. -/
```

## Source Excerpt

```lean
private theorem diverge_go_self (c : List TauIdx) (d i fuel : Nat) :
    diverge_go c c d i fuel = 0 := by
  induction fuel generalizing i with
  | zero => unfold diverge_go; rfl
  | succ n ih =>
    unfold diverge_go
    simp only [Nat.succ_ne_zero, ↓reduceIte]
    split
    · rfl
    · simp [ih]
```
