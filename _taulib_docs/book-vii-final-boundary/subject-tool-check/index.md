---
{
  "projection_kind": "taulib_declaration",
  "title": "subject_tool_check",
  "permalink": "/corpus/taulib/docs/book-vii-final-boundary/subject-tool-check/",
  "summary_short": "`theorem` declaration in `TauLib.BookVII.Final.Boundary`.",
  "declaration_id": "TauLib.BookVII.Final.Boundary::subject_tool_check",
  "declaration_slug": "subject-tool-check",
  "kind": "theorem",
  "name": "subject_tool_check",
  "module_name": "TauLib.BookVII.Final.Boundary",
  "module_url": "/corpus/taulib/docs/book-vii-final-boundary/",
  "source_line_start": 158,
  "source_line_end": 162,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Final/Boundary.lean#L158-L162",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVII.Final.Boundary",
        "url": "/corpus/taulib/docs/book-vii-final-boundary/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Final/Boundary.lean#L158-L162",
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

- Module: [TauLib.BookVII.Final.Boundary](/corpus/taulib/docs/book-vii-final-boundary/)
- Source path: [`TauLib/BookVII/Final/Boundary.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Final/Boundary.lean#L158-L162)
- Source range: L158-L162
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
theorem subject_tool_check :
    subject_tool.boundary_condition = true ∧
    subject_tool.collapse = true ∧
    subject_tool.no_external_standpoint = true :=
  ⟨rfl, rfl, rfl⟩
```
