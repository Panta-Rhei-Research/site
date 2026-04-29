---
{
  "projection_kind": "taulib_declaration",
  "title": "nonOmega_complete",
  "permalink": "/verify/taulib/docs/book-i-kernel-diagonal/non-omega-complete/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Kernel.Diagonal`.",
  "declaration_id": "TauLib.BookI.Kernel.Diagonal::nonOmega_complete",
  "declaration_slug": "non-omega-complete",
  "kind": "theorem",
  "name": "nonOmega_complete",
  "module_name": "TauLib.BookI.Kernel.Diagonal",
  "module_url": "/verify/taulib/docs/book-i-kernel-diagonal/",
  "source_line_start": 42,
  "source_line_end": 44,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Kernel/Diagonal.lean#L42-L44",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Kernel/Diagonal.lean#L42-L44",
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
- Source path: [`TauLib/BookI/Kernel/Diagonal.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Kernel/Diagonal.lean#L42-L44)
- Source range: L42-L44
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The complete list of non-omega generators is [α, π, γ, η]. -/
```

## Source Excerpt

```lean
theorem nonOmega_complete (g : Generator) (hg : g ≠ omega) :
    g ∈ nonOmegaGenerators := by
  cases g <;> simp [nonOmegaGenerators] <;> exact absurd rfl hg
```
