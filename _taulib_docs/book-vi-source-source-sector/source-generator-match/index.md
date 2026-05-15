---
{
  "projection_kind": "taulib_declaration",
  "title": "source_generator_match",
  "permalink": "/corpus/taulib/docs/book-vi-source-source-sector/source-generator-match/",
  "summary_short": "`theorem` declaration in `TauLib.BookVI.Source.SourceSector`.",
  "declaration_id": "TauLib.BookVI.Source.SourceSector::source_generator_match",
  "declaration_slug": "source-generator-match",
  "kind": "theorem",
  "name": "source_generator_match",
  "module_name": "TauLib.BookVI.Source.SourceSector",
  "module_url": "/corpus/taulib/docs/book-vi-source-source-sector/",
  "source_line_start": 58,
  "source_line_end": 60,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Source/SourceSector.lean#L58-L60",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.Source.SourceSector",
        "url": "/corpus/taulib/docs/book-vi-source-source-sector/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Source/SourceSector.lean#L58-L60",
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

- Module: [TauLib.BookVI.Source.SourceSector](/corpus/taulib/docs/book-vi-source-source-sector/)
- Source path: [`TauLib/BookVI/Source/SourceSector.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Source/SourceSector.lean#L58-L60)
- Source range: L58-L60
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Source sector matches the FourPlusOne source_sector definition. -/
```

## Source Excerpt

```lean
theorem source_generator_match :
    source_def.generator = source_sector.generator :=
  rfl
```
