---
{
  "projection_kind": "taulib_declaration",
  "title": "TauAdmissiblePoint.valid",
  "permalink": "/verify/taulib/docs/book-ii-interior-tau-admissible/valid/",
  "summary_short": "`def` declaration in `TauLib.BookII.Interior.TauAdmissible`.",
  "declaration_id": "TauLib.BookII.Interior.TauAdmissible::TauAdmissiblePoint.valid",
  "declaration_slug": "valid",
  "kind": "def",
  "name": "TauAdmissiblePoint.valid",
  "module_name": "TauLib.BookII.Interior.TauAdmissible",
  "module_url": "/verify/taulib/docs/book-ii-interior-tau-admissible/",
  "source_line_start": 103,
  "source_line_end": 104,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Interior/TauAdmissible.lean#L103-L104",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Interior.TauAdmissible",
        "url": "/verify/taulib/docs/book-ii-interior-tau-admissible/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Interior/TauAdmissible.lean#L103-L104",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "status": "defined"
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

- Module: [TauLib.BookII.Interior.TauAdmissible](/verify/taulib/docs/book-ii-interior-tau-admissible/)
- Source path: [`TauLib/BookII/Interior/TauAdmissible.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Interior/TauAdmissible.lean#L103-L104)
- Source range: L103-L104
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Check that a TauAdmissiblePoint satisfies all constraints. -/
```

## Source Excerpt

```lean
def TauAdmissiblePoint.valid (p : TauAdmissiblePoint) : Bool :=
  is_tau_admissible p.a p.b p.c p.d
```
