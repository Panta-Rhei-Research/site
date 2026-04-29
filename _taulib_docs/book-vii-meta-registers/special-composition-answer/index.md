---
{
  "projection_kind": "taulib_declaration",
  "title": "special_composition_answer",
  "permalink": "/verify/taulib/docs/book-vii-meta-registers/special-composition-answer/",
  "summary_short": "`theorem` declaration in `TauLib.BookVII.Meta.Registers`.",
  "declaration_id": "TauLib.BookVII.Meta.Registers::special_composition_answer",
  "declaration_slug": "special-composition-answer",
  "kind": "theorem",
  "name": "special_composition_answer",
  "module_name": "TauLib.BookVII.Meta.Registers",
  "module_url": "/verify/taulib/docs/book-vii-meta-registers/",
  "source_line_start": 868,
  "source_line_end": 871,
  "registry_ids": [
    "VII.P07"
  ],
  "related_registry_items": [
    {
      "id": "VII.P07",
      "title": "Special Composition Answer",
      "url": "/registry/object/VII.P07/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L868-L871",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L868-L871",
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
- Source path: [`TauLib/BookVII/Meta/Registers.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L868-L871)
- Source range: L868-L871
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `VII.P07` — Special Composition Answer

## Immediate Comment / Docstring

```lean
/-- [VII.P07] Special Composition Answer (ch27). Composition exists
    when the colimit exists in the ambient category. This gives a
    precise structural answer to van Inwagen's Special Composition
    Question: things compose when their diagram has a colimit. -/
```

## Source Excerpt

```lean
theorem special_composition_answer :
    mereological_colimit.composition_as_colimit = true ∧
    mereological_colimit.universal_property = true :=
  ⟨rfl, rfl⟩
```
