---
{
  "projection_kind": "taulib_declaration",
  "title": "topo_faithful_6_2",
  "permalink": "/corpus/taulib/docs/book-iii-bridge-translation-topo/topo-faithful-6-2/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Bridge.TranslationTopo`.",
  "declaration_id": "TauLib.BookIII.Bridge.TranslationTopo::topo_faithful_6_2",
  "declaration_slug": "topo-faithful-6-2",
  "kind": "theorem",
  "name": "topo_faithful_6_2",
  "module_name": "TauLib.BookIII.Bridge.TranslationTopo",
  "module_url": "/corpus/taulib/docs/book-iii-bridge-translation-topo/",
  "source_line_start": 203,
  "source_line_end": 204,
  "registry_ids": [
    "III.T60"
  ],
  "related_registry_items": [
    {
      "id": "III.T60",
      "title": "Topological Faithfulness",
      "url": "/registry/object/III.T60/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/TranslationTopo.lean#L203-L204",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/TranslationTopo.lean#L203-L204",
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
- Source path: [`TauLib/BookIII/Bridge/TranslationTopo.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/TranslationTopo.lean#L203-L204)
- Source range: L203-L204
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- `III.T60` — Topological Faithfulness

## Immediate Comment / Docstring

```lean
/-- [III.T60] Topological faithfulness at bound 6, depth 2. -/
```

## Source Excerpt

```lean
theorem topo_faithful_6_2 :
    topo_faithful_check 6 2 = true := by native_decide
```
