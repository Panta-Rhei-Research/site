---
{
  "projection_kind": "taulib_declaration",
  "title": "embed_int_mul",
  "permalink": "/corpus/taulib/docs/book-i-kernel-foundation-scalar-bridges/embed-int-mul/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.KernelFoundation.ScalarBridges`.",
  "declaration_id": "TauLib.BookI.KernelFoundation.ScalarBridges::embed_int_mul",
  "declaration_slug": "embed-int-mul",
  "kind": "theorem",
  "name": "embed_int_mul",
  "module_name": "TauLib.BookI.KernelFoundation.ScalarBridges",
  "module_url": "/corpus/taulib/docs/book-i-kernel-foundation-scalar-bridges/",
  "source_line_start": 186,
  "source_line_end": 190,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/KernelFoundation/ScalarBridges.lean#L186-L190",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.KernelFoundation.ScalarBridges",
        "url": "/corpus/taulib/docs/book-i-kernel-foundation-scalar-bridges/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/KernelFoundation/ScalarBridges.lean#L186-L190",
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

- Module: [TauLib.BookI.KernelFoundation.ScalarBridges](/corpus/taulib/docs/book-i-kernel-foundation-scalar-bridges/)
- Source path: [`TauLib/BookI/KernelFoundation/ScalarBridges.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/KernelFoundation/ScalarBridges.lean#L186-L190)
- Source range: L186-L190
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The embedding preserves multiplication.

    `(a · 1 + 0 · j)(b · 1 + 0 · j) = ab · 1 + 0 · j`,
    i.e. `embed (a · b) = embed a · embed b`. -/
```

## Source Excerpt

```lean
theorem embed_int_mul (a b : Int) :
    embed_int_into_d (a * b) =
      SplitComplex.mul (embed_int_into_d a) (embed_int_into_d b) := by
  unfold embed_int_into_d SplitComplex.mul
  simp
```
