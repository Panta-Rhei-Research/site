---
{
  "projection_kind": "taulib_declaration",
  "title": "e3_succ_saturates",
  "permalink": "/verify/taulib/docs/book-iii-mirror-saturation/e3-succ-saturates/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Mirror.Saturation`.",
  "declaration_id": "TauLib.BookIII.Mirror.Saturation::e3_succ_saturates",
  "declaration_slug": "e3-succ-saturates",
  "kind": "theorem",
  "name": "e3_succ_saturates",
  "module_name": "TauLib.BookIII.Mirror.Saturation",
  "module_url": "/verify/taulib/docs/book-iii-mirror-saturation/",
  "source_line_start": 281,
  "source_line_end": 281,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Mirror/Saturation.lean#L281-L281",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Mirror.Saturation",
        "url": "/verify/taulib/docs/book-iii-mirror-saturation/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Mirror/Saturation.lean#L281-L281",
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

- Module: [TauLib.BookIII.Mirror.Saturation](/verify/taulib/docs/book-iii-mirror-saturation/)
- Source path: [`TauLib/BookIII/Mirror/Saturation.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Mirror/Saturation.lean#L281-L281)
- Source range: L281-L281
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- E3.succ = E3: successor saturates at E3. -/
```

## Source Excerpt

```lean
theorem e3_succ_saturates : EnrLevel.E3.succ = EnrLevel.E3 := rfl
```
