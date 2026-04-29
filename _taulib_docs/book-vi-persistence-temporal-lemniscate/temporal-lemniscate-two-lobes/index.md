---
{
  "projection_kind": "taulib_declaration",
  "title": "temporal_lemniscate_two_lobes",
  "permalink": "/verify/taulib/docs/book-vi-persistence-temporal-lemniscate/temporal-lemniscate-two-lobes/",
  "summary_short": "`theorem` declaration in `TauLib.BookVI.Persistence.TemporalLemniscate`.",
  "declaration_id": "TauLib.BookVI.Persistence.TemporalLemniscate::temporal_lemniscate_two_lobes",
  "declaration_slug": "temporal-lemniscate-two-lobes",
  "kind": "theorem",
  "name": "temporal_lemniscate_two_lobes",
  "module_name": "TauLib.BookVI.Persistence.TemporalLemniscate",
  "module_url": "/verify/taulib/docs/book-vi-persistence-temporal-lemniscate/",
  "source_line_start": 55,
  "source_line_end": 56,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Persistence/TemporalLemniscate.lean#L55-L56",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.Persistence.TemporalLemniscate",
        "url": "/verify/taulib/docs/book-vi-persistence-temporal-lemniscate/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Persistence/TemporalLemniscate.lean#L55-L56",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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

- Module: [TauLib.BookVI.Persistence.TemporalLemniscate](/verify/taulib/docs/book-vi-persistence-temporal-lemniscate/)
- Source path: [`TauLib/BookVI/Persistence/TemporalLemniscate.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Persistence/TemporalLemniscate.lean#L55-L56)
- Source range: L55-L56
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
No immediate Lean doc/comment block was detected for this declaration.
```

## Source Excerpt

```lean
theorem temporal_lemniscate_two_lobes :
    temporal_lem.lobe_count = 2 := temporal_lem.lobes_eq
```
