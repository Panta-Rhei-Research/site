---
{
  "projection_kind": "taulib_declaration",
  "title": "autoimmunity_five_failures",
  "permalink": "/verify/taulib/docs/book-vi-consumer-immune/autoimmunity-five-failures/",
  "summary_short": "`theorem` declaration in `TauLib.BookVI.Consumer.Immune`.",
  "declaration_id": "TauLib.BookVI.Consumer.Immune::autoimmunity_five_failures",
  "declaration_slug": "autoimmunity-five-failures",
  "kind": "theorem",
  "name": "autoimmunity_five_failures",
  "module_name": "TauLib.BookVI.Consumer.Immune",
  "module_url": "/verify/taulib/docs/book-vi-consumer-immune/",
  "source_line_start": 82,
  "source_line_end": 91,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/Immune.lean#L82-L91",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.Consumer.Immune",
        "url": "/verify/taulib/docs/book-vi-consumer-immune/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/Immune.lean#L82-L91",
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

- Module: [TauLib.BookVI.Consumer.Immune](/verify/taulib/docs/book-vi-consumer-immune/)
- Source path: [`TauLib/BookVI/Consumer/Immune.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/Immune.lean#L82-L91)
- Source range: L82-L91
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
No immediate Lean doc/comment block was detected for this declaration.
```

## Source Excerpt

```lean
theorem autoimmunity_five_failures :
    autoimmune.failure_modes = 5 ∧
    autoimmune.clopen_violation = true ∧
    autoimmune.refinement_violation = true ∧
    autoimmune.stability_violation = true ∧
    autoimmune.law_violation = true ∧
    autoimmune.equivariance_violation = true :=
  ⟨rfl, rfl, rfl, rfl, rfl, rfl⟩

end Tau.BookVI.Immune
```
