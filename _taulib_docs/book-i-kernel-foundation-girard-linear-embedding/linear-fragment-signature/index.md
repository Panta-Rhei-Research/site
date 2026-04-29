---
{
  "projection_kind": "taulib_declaration",
  "title": "linear_fragment_signature",
  "permalink": "/verify/taulib/docs/book-i-kernel-foundation-girard-linear-embedding/linear-fragment-signature/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.KernelFoundation.GirardLinearEmbedding`.",
  "declaration_id": "TauLib.BookI.KernelFoundation.GirardLinearEmbedding::linear_fragment_signature",
  "declaration_slug": "linear-fragment-signature",
  "kind": "theorem",
  "name": "linear_fragment_signature",
  "module_name": "TauLib.BookI.KernelFoundation.GirardLinearEmbedding",
  "module_url": "/verify/taulib/docs/book-i-kernel-foundation-girard-linear-embedding/",
  "source_line_start": 164,
  "source_line_end": 166,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/KernelFoundation/GirardLinearEmbedding.lean#L164-L166",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.KernelFoundation.GirardLinearEmbedding",
        "url": "/verify/taulib/docs/book-i-kernel-foundation-girard-linear-embedding/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/KernelFoundation/GirardLinearEmbedding.lean#L164-L166",
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

- Module: [TauLib.BookI.KernelFoundation.GirardLinearEmbedding](/verify/taulib/docs/book-i-kernel-foundation-girard-linear-embedding/)
- Source path: [`TauLib/BookI/KernelFoundation/GirardLinearEmbedding.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/KernelFoundation/GirardLinearEmbedding.lean#L164-L166)
- Source range: L164-L166
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Paper §3 linear-fragment signature**: exactly one of the three
    structural rules is admitted (exchange); the other two refused. -/
```

## Source Excerpt

```lean
theorem linear_fragment_signature :
    (allStructuralRules.filter (·.admittedInLinear)).length = 1 := by
  decide
```
