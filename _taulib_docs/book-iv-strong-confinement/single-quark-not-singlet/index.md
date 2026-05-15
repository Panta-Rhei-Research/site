---
{
  "projection_kind": "taulib_declaration",
  "title": "single_quark_not_singlet",
  "permalink": "/corpus/taulib/docs/book-iv-strong-confinement/single-quark-not-singlet/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Strong.Confinement`.",
  "declaration_id": "TauLib.BookIV.Strong.Confinement::single_quark_not_singlet",
  "declaration_slug": "single-quark-not-singlet",
  "kind": "theorem",
  "name": "single_quark_not_singlet",
  "module_name": "TauLib.BookIV.Strong.Confinement",
  "module_url": "/corpus/taulib/docs/book-iv-strong-confinement/",
  "source_line_start": 182,
  "source_line_end": 182,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/Confinement.lean#L182-L182",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Strong.Confinement",
        "url": "/corpus/taulib/docs/book-iv-strong-confinement/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/Confinement.lean#L182-L182",
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

- Module: [TauLib.BookIV.Strong.Confinement](/corpus/taulib/docs/book-iv-strong-confinement/)
- Source path: [`TauLib/BookIV/Strong/Confinement.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/Confinement.lean#L182-L182)
- Source range: L182-L182
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- A single quark {1} is NOT a singlet. -/
```

## Source Excerpt

```lean
theorem single_quark_not_singlet : is_color_singlet [1] = false := by rfl
```
