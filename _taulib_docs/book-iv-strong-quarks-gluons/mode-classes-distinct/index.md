---
{
  "projection_kind": "taulib_declaration",
  "title": "mode_classes_distinct",
  "permalink": "/verify/taulib/docs/book-iv-strong-quarks-gluons/mode-classes-distinct/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Strong.QuarksGluons`.",
  "declaration_id": "TauLib.BookIV.Strong.QuarksGluons::mode_classes_distinct",
  "declaration_slug": "mode-classes-distinct",
  "kind": "theorem",
  "name": "mode_classes_distinct",
  "module_name": "TauLib.BookIV.Strong.QuarksGluons",
  "module_url": "/verify/taulib/docs/book-iv-strong-quarks-gluons/",
  "source_line_start": 185,
  "source_line_end": 189,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/QuarksGluons.lean#L185-L189",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Strong.QuarksGluons",
        "url": "/verify/taulib/docs/book-iv-strong-quarks-gluons/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/QuarksGluons.lean#L185-L189",
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

- Module: [TauLib.BookIV.Strong.QuarksGluons](/verify/taulib/docs/book-iv-strong-quarks-gluons/)
- Source path: [`TauLib/BookIV/Strong/QuarksGluons.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/QuarksGluons.lean#L185-L189)
- Source range: L185-L189
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- All three mode classes are distinct. -/
```

## Source Excerpt

```lean
theorem mode_classes_distinct :
    quark_generations.gen1_class ≠ quark_generations.gen2_class ∧
    quark_generations.gen2_class ≠ quark_generations.gen3_class ∧
    quark_generations.gen1_class ≠ quark_generations.gen3_class := by
  simp [quark_generations]
```
