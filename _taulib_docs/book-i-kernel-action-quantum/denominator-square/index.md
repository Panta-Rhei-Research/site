---
{
  "projection_kind": "taulib_declaration",
  "title": "denominator_square",
  "permalink": "/verify/taulib/docs/book-i-kernel-action-quantum/denominator-square/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Kernel.ActionQuantum`.",
  "declaration_id": "TauLib.BookI.Kernel.ActionQuantum::denominator_square",
  "declaration_slug": "denominator-square",
  "kind": "theorem",
  "name": "denominator_square",
  "module_name": "TauLib.BookI.Kernel.ActionQuantum",
  "module_url": "/verify/taulib/docs/book-i-kernel-action-quantum/",
  "source_line_start": 131,
  "source_line_end": 131,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Kernel/ActionQuantum.lean#L131-L131",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Kernel.ActionQuantum",
        "url": "/verify/taulib/docs/book-i-kernel-action-quantum/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Kernel/ActionQuantum.lean#L131-L131",
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

- Module: [TauLib.BookI.Kernel.ActionQuantum](/verify/taulib/docs/book-i-kernel-action-quantum/)
- Source path: [`TauLib/BookI/Kernel/ActionQuantum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Kernel/ActionQuantum.lean#L131-L131)
- Source range: L131-L131
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- 225 = 15² (perfect square). -/
```

## Source Excerpt

```lean
theorem denominator_square : (225 : Nat) = 15 * 15 := by omega
```
