---
{
  "projection_kind": "taulib_declaration",
  "title": "readout_functor_faithfulness",
  "permalink": "/verify/taulib/docs/book-vii-meta-registers/readout-functor-faithfulness/",
  "summary_short": "`theorem` declaration in `TauLib.BookVII.Meta.Registers`.",
  "declaration_id": "TauLib.BookVII.Meta.Registers::readout_functor_faithfulness",
  "declaration_slug": "readout-functor-faithfulness",
  "kind": "theorem",
  "name": "readout_functor_faithfulness",
  "module_name": "TauLib.BookVII.Meta.Registers",
  "module_url": "/verify/taulib/docs/book-vii-meta-registers/",
  "source_line_start": 532,
  "source_line_end": 537,
  "registry_ids": [
    "VII.T10"
  ],
  "related_registry_items": [
    {
      "id": "VII.T10",
      "title": "Readout Functor Faithfulness",
      "url": "/registry/object/VII.T10/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L532-L537",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L532-L537",
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
- Source path: [`TauLib/BookVII/Meta/Registers.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L532-L537)
- Source range: L532-L537
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `VII.T10` — Readout Functor Faithfulness

## Immediate Comment / Docstring

```lean
/-- [VII.T10] Readout Functor Faithfulness (ch15). Each readout functor
    is faithful within its register: distinct kernel morphisms map to
    distinct observations/norms/proofs/stances. Faithfulness ensures
    no structural information is lost within a single register. -/
```

## Source Excerpt

```lean
theorem readout_functor_faithfulness :
    readout_functor.well_defined = true ∧
    readout_functor.functorial = true ∧
    readout_functor.typed_codomain = true ∧
    readout_functor.readout_count = 4 :=
  ⟨rfl, rfl, rfl, rfl⟩
```
