---
{
  "projection_kind": "taulib_declaration",
  "title": "TruthBearerAsSection",
  "permalink": "/verify/taulib/docs/book-vii-ethics-ciproof/truth-bearer-as-section/",
  "summary_short": "`structure` declaration in `TauLib.BookVII.Ethics.CIProof`.",
  "declaration_id": "TauLib.BookVII.Ethics.CIProof::TruthBearerAsSection",
  "declaration_slug": "truth-bearer-as-section",
  "kind": "structure",
  "name": "TruthBearerAsSection",
  "module_name": "TauLib.BookVII.Ethics.CIProof",
  "module_url": "/verify/taulib/docs/book-vii-ethics-ciproof/",
  "source_line_start": 750,
  "source_line_end": 755,
  "registry_ids": [
    "VII.D61"
  ],
  "related_registry_items": [
    {
      "id": "VII.D61",
      "title": "Truth-Bearer as Section",
      "url": "/registry/object/VII.D61/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L750-L755",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVII.Ethics.CIProof",
        "url": "/verify/taulib/docs/book-vii-ethics-ciproof/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L750-L755",
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

- Module: [TauLib.BookVII.Ethics.CIProof](/verify/taulib/docs/book-vii-ethics-ciproof/)
- Source path: [`TauLib/BookVII/Ethics/CIProof.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L750-L755)
- Source range: L750-L755
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VII.D61` — Truth-Bearer as Section

## Immediate Comment / Docstring

```lean
/-- [VII.D61] Truth-Bearer as Section (ch42). The truth-bearer is
    a section of a presheaf: a global assignment of truth values
    compatible with restriction maps. Propositions are sections,
    truth is a global section property. -/
```

## Source Excerpt

```lean
structure TruthBearerAsSection where
  /-- Truth-bearer = section. -/
  bearer_as_section : Bool := true
  /-- Compatible with restrictions. -/
  restriction_compatible : Bool := true
  deriving Repr
```
