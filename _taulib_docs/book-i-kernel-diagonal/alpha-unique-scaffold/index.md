---
{
  "projection_kind": "taulib_declaration",
  "title": "alpha_unique_scaffold",
  "permalink": "/verify/taulib/docs/book-i-kernel-diagonal/alpha-unique-scaffold/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Kernel.Diagonal`.",
  "declaration_id": "TauLib.BookI.Kernel.Diagonal::alpha_unique_scaffold",
  "declaration_slug": "alpha-unique-scaffold",
  "kind": "theorem",
  "name": "alpha_unique_scaffold",
  "module_name": "TauLib.BookI.Kernel.Diagonal",
  "module_url": "/verify/taulib/docs/book-i-kernel-diagonal/",
  "source_line_start": 83,
  "source_line_end": 87,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Kernel/Diagonal.lean#L83-L87",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Kernel.Diagonal",
        "url": "/verify/taulib/docs/book-i-kernel-diagonal/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Kernel/Diagonal.lean#L83-L87",
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

- Module: [TauLib.BookI.Kernel.Diagonal](/verify/taulib/docs/book-i-kernel-diagonal/)
- Source path: [`TauLib/BookI/Kernel/Diagonal.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Kernel/Diagonal.lean#L83-L87)
- Source range: L83-L87
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Alpha is the unique non-omega, non-solenoidal generator:
    the counting scaffold. -/
```

## Source Excerpt

```lean
theorem alpha_unique_scaffold :
    alpha ∉ solenoidalGenerators ∧ alpha ≠ omega := by
  exact ⟨by decide, by decide⟩

end Tau.Kernel
```
