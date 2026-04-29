---
{
  "projection_kind": "taulib_declaration",
  "title": "book_ii_bridge_complete",
  "permalink": "/verify/taulib/docs/book-iii-spectrum-kernel-hinge/book-ii-bridge-complete/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Spectrum.KernelHinge`.",
  "declaration_id": "TauLib.BookIII.Spectrum.KernelHinge::book_ii_bridge_complete",
  "declaration_slug": "book-ii-bridge-complete",
  "kind": "theorem",
  "name": "book_ii_bridge_complete",
  "module_name": "TauLib.BookIII.Spectrum.KernelHinge",
  "module_url": "/verify/taulib/docs/book-iii-spectrum-kernel-hinge/",
  "source_line_start": 131,
  "source_line_end": 134,
  "registry_ids": [
    "I.T34"
  ],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectrum/KernelHinge.lean#L131-L134",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Spectrum.KernelHinge",
        "url": "/verify/taulib/docs/book-iii-spectrum-kernel-hinge/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectrum/KernelHinge.lean#L131-L134",
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

- Module: [TauLib.BookIII.Spectrum.KernelHinge](/verify/taulib/docs/book-iii-spectrum-kernel-hinge/)
- Source path: [`TauLib/BookIII/Spectrum/KernelHinge.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectrum/KernelHinge.lean#L131-L134)
- Source range: L131-L134
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [I.T34] Main theorem: the bridge is complete.
    All fields are instantiated from earned structures;
    no sorry, no axiom, no external import beyond Mathlib tactics. -/
```

## Source Excerpt

```lean
theorem book_ii_bridge_complete :
    book_ii_bridge.hinge.generators_are_five = rfl ∧
    book_ii_bridge.export_data = book_i_export := by
  exact ⟨rfl, rfl⟩
```
