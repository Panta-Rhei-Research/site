---
{
  "projection_kind": "taulib_declaration",
  "title": "full_bndlift",
  "permalink": "/corpus/taulib/docs/book-ii-hartogs-bnd-lift/full-bndlift/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Hartogs.BndLift`.",
  "declaration_id": "TauLib.BookII.Hartogs.BndLift::full_bndlift",
  "declaration_slug": "full-bndlift",
  "kind": "theorem",
  "name": "full_bndlift",
  "module_name": "TauLib.BookII.Hartogs.BndLift",
  "module_url": "/corpus/taulib/docs/book-ii-hartogs-bnd-lift/",
  "source_line_start": 473,
  "source_line_end": 475,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/BndLift.lean#L473-L475",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Hartogs.BndLift",
        "url": "/corpus/taulib/docs/book-ii-hartogs-bnd-lift/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/BndLift.lean#L473-L475",
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

- Module: [TauLib.BookII.Hartogs.BndLift](/corpus/taulib/docs/book-ii-hartogs-bnd-lift/)
- Source path: [`TauLib/BookII/Hartogs/BndLift.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/BndLift.lean#L473-L475)
- Source range: L473-L475
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
-- Full verification
```

## Source Excerpt

```lean
theorem full_bndlift : full_bndlift_check = true := by native_decide

end Tau.BookII.Hartogs
```
