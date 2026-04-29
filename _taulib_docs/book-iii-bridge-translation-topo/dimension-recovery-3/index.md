---
{
  "projection_kind": "taulib_declaration",
  "title": "dimension_recovery_3",
  "permalink": "/verify/taulib/docs/book-iii-bridge-translation-topo/dimension-recovery-3/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Bridge.TranslationTopo`.",
  "declaration_id": "TauLib.BookIII.Bridge.TranslationTopo::dimension_recovery_3",
  "declaration_slug": "dimension-recovery-3",
  "kind": "theorem",
  "name": "dimension_recovery_3",
  "module_name": "TauLib.BookIII.Bridge.TranslationTopo",
  "module_url": "/verify/taulib/docs/book-iii-bridge-translation-topo/",
  "source_line_start": 199,
  "source_line_end": 200,
  "registry_ids": [
    "III.D90"
  ],
  "related_registry_items": [
    {
      "id": "III.D90",
      "title": "Dimension Recovery",
      "url": "/registry/object/III.D90/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/TranslationTopo.lean#L199-L200",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Bridge.TranslationTopo",
        "url": "/verify/taulib/docs/book-iii-bridge-translation-topo/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/TranslationTopo.lean#L199-L200",
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

- Module: [TauLib.BookIII.Bridge.TranslationTopo](/verify/taulib/docs/book-iii-bridge-translation-topo/)
- Source path: [`TauLib/BookIII/Bridge/TranslationTopo.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/TranslationTopo.lean#L199-L200)
- Source range: L199-L200
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.D90` — Dimension Recovery

## Immediate Comment / Docstring

```lean
/-- [III.D90] Dimension recovery at depth 3. -/
```

## Source Excerpt

```lean
theorem dimension_recovery_3 :
    dimension_recovery_check 3 = true := by native_decide
```
