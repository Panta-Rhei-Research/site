---
{
  "projection_kind": "taulib_declaration",
  "title": "sex_is_second_distinction",
  "permalink": "/corpus/taulib/docs/book-vi-consumer-reproduction/sex-is-second-distinction/",
  "summary_short": "`theorem` declaration in `TauLib.BookVI.Consumer.Reproduction`.",
  "declaration_id": "TauLib.BookVI.Consumer.Reproduction::sex_is_second_distinction",
  "declaration_slug": "sex-is-second-distinction",
  "kind": "theorem",
  "name": "sex_is_second_distinction",
  "module_name": "TauLib.BookVI.Consumer.Reproduction",
  "module_url": "/corpus/taulib/docs/book-vi-consumer-reproduction/",
  "source_line_start": 85,
  "source_line_end": 91,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/Reproduction.lean#L85-L91",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.Consumer.Reproduction",
        "url": "/corpus/taulib/docs/book-vi-consumer-reproduction/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/Reproduction.lean#L85-L91",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "role": "proof obligation",
      "status": "formal proof obligation checked"
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

- Module: [TauLib.BookVI.Consumer.Reproduction](/corpus/taulib/docs/book-vi-consumer-reproduction/)
- Source path: [`TauLib/BookVI/Consumer/Reproduction.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/Reproduction.lean#L85-L91)
- Source range: L85-L91
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
No immediate Lean doc/comment block was detected for this declaration.
```

## Source Excerpt

```lean
theorem sex_is_second_distinction :
    second_dist.refinement_level = 1 ∧
    second_dist.first = "self_nonself" ∧
    second_dist.second = "self_otherself" :=
  ⟨rfl, rfl, rfl⟩

end Tau.BookVI.Reproduction
```
