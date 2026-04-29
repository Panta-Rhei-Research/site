---
{
  "projection_kind": "taulib_declaration",
  "title": "OnticVirtualDistinction",
  "permalink": "/verify/taulib/docs/book-vii-meta-registers/ontic-virtual-distinction/",
  "summary_short": "`structure` declaration in `TauLib.BookVII.Meta.Registers`.",
  "declaration_id": "TauLib.BookVII.Meta.Registers::OnticVirtualDistinction",
  "declaration_slug": "ontic-virtual-distinction",
  "kind": "structure",
  "name": "OnticVirtualDistinction",
  "module_name": "TauLib.BookVII.Meta.Registers",
  "module_url": "/verify/taulib/docs/book-vii-meta-registers/",
  "source_line_start": 617,
  "source_line_end": 624,
  "registry_ids": [
    "VII.D26"
  ],
  "related_registry_items": [
    {
      "id": "VII.D26",
      "title": "Ontic/Virtual Distinction",
      "url": "/registry/object/VII.D26/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L617-L624",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVII.Meta.Registers",
        "url": "/verify/taulib/docs/book-vii-meta-registers/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L617-L624",
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

- Module: [TauLib.BookVII.Meta.Registers](/verify/taulib/docs/book-vii-meta-registers/)
- Source path: [`TauLib/BookVII/Meta/Registers.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L617-L624)
- Source range: L617-L624
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VII.D26` — Ontic/Virtual Distinction

## Immediate Comment / Docstring

```lean
/-- [VII.D26] Ontic/Virtual Distinction (ch18). Two-valued ontological
    classifier: NF-addressed (ontic) vs non-addressed (virtual).
    Virtual objects may appear in intermediate computations but have
    no independent existence. -/
```

## Source Excerpt

```lean
structure OnticVirtualDistinction where
  /-- Ontic: has NF-address. -/
  ontic_addressed : Bool := true
  /-- Virtual: no NF-address. -/
  virtual_unaddressed : Bool := true
  /-- Binary classification exhaustive. -/
  classification_exhaustive : Bool := true
  deriving Repr
```
