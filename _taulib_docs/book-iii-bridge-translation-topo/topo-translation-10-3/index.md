---
{
  "projection_kind": "taulib_declaration",
  "title": "topo_translation_10_3",
  "permalink": "/corpus/taulib/docs/book-iii-bridge-translation-topo/topo-translation-10-3/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Bridge.TranslationTopo`.",
  "declaration_id": "TauLib.BookIII.Bridge.TranslationTopo::topo_translation_10_3",
  "declaration_slug": "topo-translation-10-3",
  "kind": "theorem",
  "name": "topo_translation_10_3",
  "module_name": "TauLib.BookIII.Bridge.TranslationTopo",
  "module_url": "/corpus/taulib/docs/book-iii-bridge-translation-topo/",
  "source_line_start": 195,
  "source_line_end": 196,
  "registry_ids": [
    "III.D89"
  ],
  "related_registry_items": [
    {
      "id": "III.D89",
      "title": "Topological Translation Functor",
      "url": "/registry/object/III.D89/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/TranslationTopo.lean#L195-L196",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Bridge.TranslationTopo",
        "url": "/corpus/taulib/docs/book-iii-bridge-translation-topo/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/TranslationTopo.lean#L195-L196",
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

- Module: [TauLib.BookIII.Bridge.TranslationTopo](/corpus/taulib/docs/book-iii-bridge-translation-topo/)
- Source path: [`TauLib/BookIII/Bridge/TranslationTopo.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/TranslationTopo.lean#L195-L196)
- Source range: L195-L196
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- `III.D89` — Topological Translation Functor

## Immediate Comment / Docstring

```lean
/-- [III.D89] Tower coherence at bound 10, depth 3. -/
```

## Source Excerpt

```lean
theorem topo_translation_10_3 :
    topo_translation_check 10 3 = true := by native_decide
```
