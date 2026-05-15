---
{
  "projection_kind": "taulib_declaration",
  "title": "pi_plus_singlet",
  "permalink": "/corpus/taulib/docs/book-iv-strong-quarks-gluons/pi-plus-singlet/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Strong.QuarksGluons`.",
  "declaration_id": "TauLib.BookIV.Strong.QuarksGluons::pi_plus_singlet",
  "declaration_slug": "pi-plus-singlet",
  "kind": "theorem",
  "name": "pi_plus_singlet",
  "module_name": "TauLib.BookIV.Strong.QuarksGluons",
  "module_url": "/corpus/taulib/docs/book-iv-strong-quarks-gluons/",
  "source_line_start": 329,
  "source_line_end": 329,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/QuarksGluons.lean#L329-L329",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Strong.QuarksGluons",
        "url": "/corpus/taulib/docs/book-iv-strong-quarks-gluons/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/QuarksGluons.lean#L329-L329",
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

- Module: [TauLib.BookIV.Strong.QuarksGluons](/corpus/taulib/docs/book-iv-strong-quarks-gluons/)
- Source path: [`TauLib/BookIV/Strong/QuarksGluons.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/QuarksGluons.lean#L329-L329)
- Source range: L329-L329
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Pi+ is a color singlet. -/
```

## Source Excerpt

```lean
theorem pi_plus_singlet : pi_plus.is_singlet = true := by rfl
```
