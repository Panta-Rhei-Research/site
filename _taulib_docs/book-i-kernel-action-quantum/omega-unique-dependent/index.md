---
{
  "projection_kind": "taulib_declaration",
  "title": "omega_unique_dependent",
  "permalink": "/verify/taulib/docs/book-i-kernel-action-quantum/omega-unique-dependent/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Kernel.ActionQuantum`.",
  "declaration_id": "TauLib.BookI.Kernel.ActionQuantum::omega_unique_dependent",
  "declaration_slug": "omega-unique-dependent",
  "kind": "theorem",
  "name": "omega_unique_dependent",
  "module_name": "TauLib.BookI.Kernel.ActionQuantum",
  "module_url": "/verify/taulib/docs/book-i-kernel-action-quantum/",
  "source_line_start": 85,
  "source_line_end": 91,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Kernel/ActionQuantum.lean#L85-L91",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Kernel/ActionQuantum.lean#L85-L91",
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
- Source path: [`TauLib/BookI/Kernel/ActionQuantum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Kernel/ActionQuantum.lean#L85-L91)
- Source range: L85-L91
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- ω is the unique dependent generator: it is the ONLY generator
    not in the independent set.
    ω = γ ∩ η (crossing = intersection of B and C sectors). -/
```

## Source Excerpt

```lean
theorem omega_unique_dependent :
    Generator.omega ∉ Generator.independent ∧
    Generator.alpha ∈ Generator.independent ∧
    Generator.pi ∈ Generator.independent ∧
    Generator.gamma ∈ Generator.independent ∧
    Generator.eta ∈ Generator.independent := by
  refine ⟨?_, ?_, ?_, ?_, ?_⟩ <;> native_decide
```
