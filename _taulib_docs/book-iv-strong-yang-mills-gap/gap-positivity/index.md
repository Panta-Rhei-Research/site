---
{
  "projection_kind": "taulib_declaration",
  "title": "GapPositivity",
  "permalink": "/corpus/taulib/docs/book-iv-strong-yang-mills-gap/gap-positivity/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Strong.YangMillsGap`.",
  "declaration_id": "TauLib.BookIV.Strong.YangMillsGap::GapPositivity",
  "declaration_slug": "gap-positivity",
  "kind": "structure",
  "name": "GapPositivity",
  "module_name": "TauLib.BookIV.Strong.YangMillsGap",
  "module_url": "/corpus/taulib/docs/book-iv-strong-yang-mills-gap/",
  "source_line_start": 252,
  "source_line_end": 257,
  "registry_ids": [
    "IV.P107"
  ],
  "related_registry_items": [
    {
      "id": "IV.P107",
      "title": "Gap positivity at each finite stage",
      "url": "/registry/object/IV.P107/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/YangMillsGap.lean#L252-L257",
  "formal_status": "defined",
  "declaration_role": "type/data schema",
  "formal_status_label": "type/data schema",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Strong.YangMillsGap",
        "url": "/corpus/taulib/docs/book-iv-strong-yang-mills-gap/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/YangMillsGap.lean#L252-L257",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
      "role": "type/data schema",
      "status": "type/data schema"
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

- Module: [TauLib.BookIV.Strong.YangMillsGap](/corpus/taulib/docs/book-iv-strong-yang-mills-gap/)
- Source path: [`TauLib/BookIV/Strong/YangMillsGap.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/YangMillsGap.lean#L252-L257)
- Source range: L252-L257
- Kind: `structure`
- Public role: `type/data schema`
- Formal status hint: `type/data schema`

## Registry Links

- `IV.P107` — Gap positivity at each finite stage

## Immediate Comment / Docstring

```lean
/-- [IV.P107] Gap positivity at each finite stage:
    delta_n^s > 0 for every n >= 3. -/
```

## Source Excerpt

```lean
structure GapPositivity where
  /-- Gap is positive at each stage. -/
  positive_all_stages : Bool := true
  /-- Mechanism: finite config, positive-definite Q on non-vacuum. -/
  mechanism : String := "finite C_s[n], Q_n^s positive on non-vacuum perturbations"
  deriving Repr
```
