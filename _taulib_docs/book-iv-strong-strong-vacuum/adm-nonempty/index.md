---
{
  "projection_kind": "taulib_declaration",
  "title": "AdmNonempty",
  "permalink": "/verify/taulib/docs/book-iv-strong-strong-vacuum/adm-nonempty/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Strong.StrongVacuum`.",
  "declaration_id": "TauLib.BookIV.Strong.StrongVacuum::AdmNonempty",
  "declaration_slug": "adm-nonempty",
  "kind": "structure",
  "name": "AdmNonempty",
  "module_name": "TauLib.BookIV.Strong.StrongVacuum",
  "module_url": "/verify/taulib/docs/book-iv-strong-strong-vacuum/",
  "source_line_start": 219,
  "source_line_end": 224,
  "registry_ids": [
    "IV.P84"
  ],
  "related_registry_items": [
    {
      "id": "IV.P84",
      "title": "Non-emptiness of $\\mathrm{Adm_s{[n",
      "url": "/registry/object/IV.P84/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/StrongVacuum.lean#L219-L224",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Strong.StrongVacuum",
        "url": "/verify/taulib/docs/book-iv-strong-strong-vacuum/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/StrongVacuum.lean#L219-L224",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
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

- Module: [TauLib.BookIV.Strong.StrongVacuum](/verify/taulib/docs/book-iv-strong-strong-vacuum/)
- Source path: [`TauLib/BookIV/Strong/StrongVacuum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/StrongVacuum.lean#L219-L224)
- Source range: L219-L224
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P84` — Non-emptiness of $\mathrm{Adm_s{[n

## Immediate Comment / Docstring

```lean
/-- [IV.P84] Adm_s[n] is nonempty for every n >= 3:
    the identity endomorphism trivially satisfies all conditions. -/
```

## Source Excerpt

```lean
structure AdmNonempty where
  /-- Witness: identity endomorphism. -/
  witness : String := "identity endomorphism"
  /-- All stages >= 3 have nonempty admissible set. -/
  all_stages : Bool := true
  deriving Repr
```
