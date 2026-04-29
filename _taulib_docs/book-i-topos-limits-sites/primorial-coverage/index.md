---
{
  "projection_kind": "taulib_declaration",
  "title": "PrimorialCoverage",
  "permalink": "/verify/taulib/docs/book-i-topos-limits-sites/primorial-coverage/",
  "summary_short": "`structure` declaration in `TauLib.BookI.Topos.LimitsSites`.",
  "declaration_id": "TauLib.BookI.Topos.LimitsSites::PrimorialCoverage",
  "declaration_slug": "primorial-coverage",
  "kind": "structure",
  "name": "PrimorialCoverage",
  "module_name": "TauLib.BookI.Topos.LimitsSites",
  "module_url": "/verify/taulib/docs/book-i-topos-limits-sites/",
  "source_line_start": 123,
  "source_line_end": 129,
  "registry_ids": [
    "I.D56"
  ],
  "related_registry_items": [
    {
      "id": "I.D56",
      "title": "Tau-Site",
      "url": "/registry/object/I.D56/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/LimitsSites.lean#L123-L129",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Topos.LimitsSites",
        "url": "/verify/taulib/docs/book-i-topos-limits-sites/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/LimitsSites.lean#L123-L129",
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

- Module: [TauLib.BookI.Topos.LimitsSites](/verify/taulib/docs/book-i-topos-limits-sites/)
- Source path: [`TauLib/BookI/Topos/LimitsSites.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/LimitsSites.lean#L123-L129)
- Source range: L123-L129
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `I.D56` — Tau-Site

## Immediate Comment / Docstring

```lean
/-- [I.D56] The primorial coverage: at each depth k,
    the covering family for object X consists of the
    CRT residues mod each prime p_0, ..., p_{k-1}. -/
```

## Source Excerpt

```lean
structure PrimorialCoverage where
  /-- The primorial depth. -/
  depth : TauIdx
  /-- The object being covered. -/
  obj : TauIdx
  /-- The CRT components form the covering family. -/
  components : TauIdx → TauIdx := fun i => crt_component obj i
```
