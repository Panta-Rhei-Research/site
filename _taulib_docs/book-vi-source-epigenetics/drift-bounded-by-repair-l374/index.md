---
{
  "projection_kind": "taulib_declaration",
  "title": "drift_bounded_by_repair",
  "permalink": "/corpus/taulib/docs/book-vi-source-epigenetics/drift-bounded-by-repair-l374/",
  "summary_short": "`theorem` declaration in `TauLib.BookVI.Source.Epigenetics`.",
  "declaration_id": "TauLib.BookVI.Source.Epigenetics::drift_bounded_by_repair",
  "declaration_slug": "drift-bounded-by-repair-l374",
  "kind": "theorem",
  "name": "drift_bounded_by_repair",
  "module_name": "TauLib.BookVI.Source.Epigenetics",
  "module_url": "/corpus/taulib/docs/book-vi-source-epigenetics/",
  "source_line_start": 374,
  "source_line_end": 380,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Source/Epigenetics.lean#L374-L380",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.Source.Epigenetics",
        "url": "/corpus/taulib/docs/book-vi-source-epigenetics/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Source/Epigenetics.lean#L374-L380",
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

- Module: [TauLib.BookVI.Source.Epigenetics](/corpus/taulib/docs/book-vi-source-epigenetics/)
- Source path: [`TauLib/BookVI/Source/Epigenetics.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Source/Epigenetics.lean#L374-L380)
- Source range: L374-L380
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
theorem drift_bounded_by_repair :
    drift_repair.consumes_repair_budget = true ∧
    drift_repair.exhaustion_implies_drift = true ∧
    drift_repair.bounded_while_funded = true :=
  ⟨rfl, rfl, rfl⟩

end Tau.BookVI.Epigenetics
```
