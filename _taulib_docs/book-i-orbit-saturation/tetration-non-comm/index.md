---
{
  "projection_kind": "taulib_declaration",
  "title": "tetration_non_comm",
  "permalink": "/corpus/taulib/docs/book-i-orbit-saturation/tetration-non-comm/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Orbit.Saturation`.",
  "declaration_id": "TauLib.BookI.Orbit.Saturation::tetration_non_comm",
  "declaration_slug": "tetration-non-comm",
  "kind": "theorem",
  "name": "tetration_non_comm",
  "module_name": "TauLib.BookI.Orbit.Saturation",
  "module_url": "/corpus/taulib/docs/book-i-orbit-saturation/",
  "source_line_start": 38,
  "source_line_end": 39,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/Saturation.lean#L38-L39",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Orbit.Saturation",
        "url": "/corpus/taulib/docs/book-i-orbit-saturation/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/Saturation.lean#L38-L39",
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

- Module: [TauLib.BookI.Orbit.Saturation](/corpus/taulib/docs/book-i-orbit-saturation/)
- Source path: [`TauLib/BookI/Orbit/Saturation.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/Saturation.lean#L38-L39)
- Source range: L38-L39
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Tetration is not commutative: 2↑↑3 = 16 ≠ 9 = 3↑↑2. -/
```

## Source Excerpt

```lean
theorem tetration_non_comm : tetration 2 3 ≠ tetration 3 2 := by
  native_decide
```
