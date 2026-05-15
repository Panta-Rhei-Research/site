---
{
  "projection_kind": "taulib_declaration",
  "title": "Clause",
  "permalink": "/corpus/taulib/docs/book-iii-spectrum-three-sat/clause/",
  "summary_short": "`structure` declaration in `TauLib.BookIII.Spectrum.ThreeSAT`.",
  "declaration_id": "TauLib.BookIII.Spectrum.ThreeSAT::Clause",
  "declaration_slug": "clause",
  "kind": "structure",
  "name": "Clause",
  "module_name": "TauLib.BookIII.Spectrum.ThreeSAT",
  "module_url": "/corpus/taulib/docs/book-iii-spectrum-three-sat/",
  "source_line_start": 46,
  "source_line_end": 53,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectrum/ThreeSAT.lean#L46-L53",
  "formal_status": "defined",
  "declaration_role": "type/data schema",
  "formal_status_label": "type/data schema",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Spectrum.ThreeSAT",
        "url": "/corpus/taulib/docs/book-iii-spectrum-three-sat/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectrum/ThreeSAT.lean#L46-L53",
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

- Module: [TauLib.BookIII.Spectrum.ThreeSAT](/corpus/taulib/docs/book-iii-spectrum-three-sat/)
- Source path: [`TauLib/BookIII/Spectrum/ThreeSAT.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectrum/ThreeSAT.lean#L46-L53)
- Source range: L46-L53
- Kind: `structure`
- Public role: `type/data schema`
- Formal status hint: `type/data schema`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- A clause: exactly 3 literals (3-CNF). -/
```

## Source Excerpt

```lean
structure Clause where
  /-- First literal. -/
  l1 : Literal
  /-- Second literal. -/
  l2 : Literal
  /-- Third literal. -/
  l3 : Literal
  deriving DecidableEq, Repr
```
