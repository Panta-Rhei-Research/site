---
{
  "projection_kind": "taulib_declaration",
  "title": "addr_equiv_compose_left",
  "permalink": "/verify/taulib/docs/book-i-denotation-equality/addr-equiv-compose-left/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Denotation.Equality`.",
  "declaration_id": "TauLib.BookI.Denotation.Equality::addr_equiv_compose_left",
  "declaration_slug": "addr-equiv-compose-left",
  "kind": "theorem",
  "name": "addr_equiv_compose_left",
  "module_name": "TauLib.BookI.Denotation.Equality",
  "module_url": "/verify/taulib/docs/book-i-denotation-equality/",
  "source_line_start": 74,
  "source_line_end": 77,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/Equality.lean#L74-L77",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Denotation.Equality",
        "url": "/verify/taulib/docs/book-i-denotation-equality/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/Equality.lean#L74-L77",
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

- Module: [TauLib.BookI.Denotation.Equality](/verify/taulib/docs/book-i-denotation-equality/)
- Source path: [`TauLib/BookI/Denotation/Equality.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/Equality.lean#L74-L77)
- Source range: L74-L77
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Composition preserves address equivalence (left). -/
```

## Source Excerpt

```lean
theorem addr_equiv_compose_left {p₁ p₂ : Program} (h : addr_equiv p₁ p₂) (q : Program) :
    addr_equiv (Program.compose p₁ q) (Program.compose p₂ q) := by
  intro x
  rw [exec_compose, exec_compose, h x]
```
