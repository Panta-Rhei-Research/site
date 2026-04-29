---
{
  "projection_kind": "taulib_declaration",
  "title": "pvsnp_obstruction_3",
  "permalink": "/verify/taulib/docs/book-iii-bridge-translation-obstruction/pvsnp-obstruction-3/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Bridge.TranslationObstruction`.",
  "declaration_id": "TauLib.BookIII.Bridge.TranslationObstruction::pvsnp_obstruction_3",
  "declaration_slug": "pvsnp-obstruction-3",
  "kind": "theorem",
  "name": "pvsnp_obstruction_3",
  "module_name": "TauLib.BookIII.Bridge.TranslationObstruction",
  "module_url": "/verify/taulib/docs/book-iii-bridge-translation-obstruction/",
  "source_line_start": 258,
  "source_line_end": 259,
  "registry_ids": [
    "III.P38"
  ],
  "related_registry_items": [
    {
      "id": "III.P38",
      "title": "P vs NP as Polynomial Translation Obstruction",
      "url": "/registry/object/III.P38/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/TranslationObstruction.lean#L258-L259",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Bridge.TranslationObstruction",
        "url": "/verify/taulib/docs/book-iii-bridge-translation-obstruction/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/TranslationObstruction.lean#L258-L259",
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

- Module: [TauLib.BookIII.Bridge.TranslationObstruction](/verify/taulib/docs/book-iii-bridge-translation-obstruction/)
- Source path: [`TauLib/BookIII/Bridge/TranslationObstruction.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/TranslationObstruction.lean#L258-L259)
- Source range: L258-L259
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.P38` — P vs NP as Polynomial Translation Obstruction

## Immediate Comment / Docstring

```lean
/-- [III.P38] P vs NP obstruction at depth 3. -/
```

## Source Excerpt

```lean
theorem pvsnp_obstruction_3 :
    pvsnp_obstruction_check 3 = true := by native_decide
```
