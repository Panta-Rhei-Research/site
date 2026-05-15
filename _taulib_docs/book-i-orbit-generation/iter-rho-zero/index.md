---
{
  "projection_kind": "taulib_declaration",
  "title": "iter_rho_zero",
  "permalink": "/corpus/taulib/docs/book-i-orbit-generation/iter-rho-zero/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Orbit.Generation`.",
  "declaration_id": "TauLib.BookI.Orbit.Generation::iter_rho_zero",
  "declaration_slug": "iter-rho-zero",
  "kind": "theorem",
  "name": "iter_rho_zero",
  "module_name": "TauLib.BookI.Orbit.Generation",
  "module_url": "/corpus/taulib/docs/book-i-orbit-generation/",
  "source_line_start": 39,
  "source_line_end": 41,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/Generation.lean#L39-L41",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Orbit.Generation",
        "url": "/corpus/taulib/docs/book-i-orbit-generation/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/Generation.lean#L39-L41",
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

- Module: [TauLib.BookI.Orbit.Generation](/corpus/taulib/docs/book-i-orbit-generation/)
- Source path: [`TauLib/BookI/Orbit/Generation.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/Generation.lean#L39-L41)
- Source range: L39-L41
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
theorem iter_rho_zero (x : TauObj) : iter_rho 0 x = x := rfl

@[simp]
```
