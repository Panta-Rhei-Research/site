---
{
  "projection_kind": "taulib_declaration",
  "title": "operator_realism",
  "permalink": "/verify/taulib/docs/book-vii-meta-registers/operator-realism/",
  "summary_short": "`theorem` declaration in `TauLib.BookVII.Meta.Registers`.",
  "declaration_id": "TauLib.BookVII.Meta.Registers::operator_realism",
  "declaration_slug": "operator-realism",
  "kind": "theorem",
  "name": "operator_realism",
  "module_name": "TauLib.BookVII.Meta.Registers",
  "module_url": "/verify/taulib/docs/book-vii-meta-registers/",
  "source_line_start": 759,
  "source_line_end": 762,
  "registry_ids": [
    "VII.T12"
  ],
  "related_registry_items": [
    {
      "id": "VII.T12",
      "title": "Operator Realism",
      "url": "/registry/object/VII.T12/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L759-L762",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVII.Meta.Registers",
        "url": "/verify/taulib/docs/book-vii-meta-registers/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L759-L762",
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

- Module: [TauLib.BookVII.Meta.Registers](/verify/taulib/docs/book-vii-meta-registers/)
- Source path: [`TauLib/BookVII/Meta/Registers.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L759-L762)
- Source range: L759-L762
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `VII.T12` — Operator Realism

## Immediate Comment / Docstring

```lean
/-- [VII.T12] Operator Realism (ch23). Classification of operators
    is a structural invariant: the operator algebra is determined by
    the kernel axioms, not by convention. Laws are discovered, not
    invented — because continuation operators are structurally forced. -/
```

## Source Excerpt

```lean
theorem operator_realism :
    law_continuation.laws_as_continuation = true ∧
    law_continuation.structure_preserving = true :=
  ⟨rfl, rfl⟩
```
