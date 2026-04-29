---
{
  "projection_kind": "taulib_declaration",
  "title": "baryon_is_singlet",
  "permalink": "/verify/taulib/docs/book-iv-strong-confinement/baryon-is-singlet/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Strong.Confinement`.",
  "declaration_id": "TauLib.BookIV.Strong.Confinement::baryon_is_singlet",
  "declaration_slug": "baryon-is-singlet",
  "kind": "theorem",
  "name": "baryon_is_singlet",
  "module_name": "TauLib.BookIV.Strong.Confinement",
  "module_url": "/verify/taulib/docs/book-iv-strong-confinement/",
  "source_line_start": 176,
  "source_line_end": 176,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/Confinement.lean#L176-L176",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Strong.Confinement",
        "url": "/verify/taulib/docs/book-iv-strong-confinement/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/Confinement.lean#L176-L176",
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

- Module: [TauLib.BookIV.Strong.Confinement](/verify/taulib/docs/book-iv-strong-confinement/)
- Source path: [`TauLib/BookIV/Strong/Confinement.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/Confinement.lean#L176-L176)
- Source range: L176-L176
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Baryon winding pattern {0,1,2} is a singlet. -/
```

## Source Excerpt

```lean
theorem baryon_is_singlet : is_color_singlet [0, 1, 2] = true := by rfl
```
