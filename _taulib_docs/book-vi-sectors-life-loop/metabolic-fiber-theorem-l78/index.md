---
{
  "projection_kind": "taulib_declaration",
  "title": "metabolic_fiber_theorem",
  "permalink": "/corpus/taulib/docs/book-vi-sectors-life-loop/metabolic-fiber-theorem-l78/",
  "summary_short": "`theorem` declaration in `TauLib.BookVI.Sectors.LifeLoop`.",
  "declaration_id": "TauLib.BookVI.Sectors.LifeLoop::metabolic_fiber_theorem",
  "declaration_slug": "metabolic-fiber-theorem-l78",
  "kind": "theorem",
  "name": "metabolic_fiber_theorem",
  "module_name": "TauLib.BookVI.Sectors.LifeLoop",
  "module_url": "/corpus/taulib/docs/book-vi-sectors-life-loop/",
  "source_line_start": 78,
  "source_line_end": 82,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Sectors/LifeLoop.lean#L78-L82",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.Sectors.LifeLoop",
        "url": "/corpus/taulib/docs/book-vi-sectors-life-loop/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Sectors/LifeLoop.lean#L78-L82",
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

- Module: [TauLib.BookVI.Sectors.LifeLoop](/corpus/taulib/docs/book-vi-sectors-life-loop/)
- Source path: [`TauLib/BookVI/Sectors/LifeLoop.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Sectors/LifeLoop.lean#L78-L82)
- Source range: L78-L82
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
theorem metabolic_fiber_theorem :
    metabolic_fiber.factor_count = 3 ∧
    metabolic_fiber.src_nontrivial = true ∧
    metabolic_fiber.rec_nontrivial = true :=
  ⟨rfl, rfl, rfl⟩
```
