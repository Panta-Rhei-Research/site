---
{
  "projection_kind": "taulib_declaration",
  "title": "LanguageSharedCode",
  "permalink": "/verify/taulib/docs/book-vi-mind-bridge/language-shared-code/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Mind.Bridge`.",
  "declaration_id": "TauLib.BookVI.Mind.Bridge::LanguageSharedCode",
  "declaration_slug": "language-shared-code",
  "kind": "structure",
  "name": "LanguageSharedCode",
  "module_name": "TauLib.BookVI.Mind.Bridge",
  "module_url": "/verify/taulib/docs/book-vi-mind-bridge/",
  "source_line_start": 93,
  "source_line_end": 100,
  "registry_ids": [
    "VI.T39"
  ],
  "related_registry_items": [
    {
      "id": "VI.T39",
      "title": "Language as Shared Code",
      "url": "/registry/object/VI.T39/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Mind/Bridge.lean#L93-L100",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.Mind.Bridge",
        "url": "/verify/taulib/docs/book-vi-mind-bridge/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Mind/Bridge.lean#L93-L100",
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

- Module: [TauLib.BookVI.Mind.Bridge](/verify/taulib/docs/book-vi-mind-bridge/)
- Source path: [`TauLib/BookVI/Mind/Bridge.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Mind/Bridge.lean#L93-L100)
- Source range: L93-L100
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.T39` — Language as Shared Code

## Immediate Comment / Docstring

```lean
/-- [VI.T39] Language as Shared Code.
    Language is the externalization of the ω-germ code evaluator:
    finite alphabet → encoding → transmission → decoding.
    This makes the internal evaluator (VI.D09) inter-subjective. -/
```

## Source Excerpt

```lean
structure LanguageSharedCode where
  /-- Alphabet is finite. -/
  alphabet_finite : Bool := true
  /-- Encoding function exists. -/
  encoding : Bool := true
  /-- Decoding function exists. -/
  decoding : Bool := true
  deriving Repr
```
