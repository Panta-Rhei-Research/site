---
{
  "projection_kind": "taulib_declaration",
  "title": "boundary_restriction_3",
  "permalink": "/verify/taulib/docs/book-iii-bridge-translation-topo/boundary-restriction-3/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Bridge.TranslationTopo`.",
  "declaration_id": "TauLib.BookIII.Bridge.TranslationTopo::boundary_restriction_3",
  "declaration_slug": "boundary-restriction-3",
  "kind": "theorem",
  "name": "boundary_restriction_3",
  "module_name": "TauLib.BookIII.Bridge.TranslationTopo",
  "module_url": "/verify/taulib/docs/book-iii-bridge-translation-topo/",
  "source_line_start": 207,
  "source_line_end": 208,
  "registry_ids": [
    "III.P37"
  ],
  "related_registry_items": [
    {
      "id": "III.P37",
      "title": "Boundary Restriction",
      "url": "/registry/object/III.P37/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/TranslationTopo.lean#L207-L208",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/TranslationTopo.lean#L207-L208",
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
- Source path: [`TauLib/BookIII/Bridge/TranslationTopo.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/TranslationTopo.lean#L207-L208)
- Source range: L207-L208
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.P37` — Boundary Restriction

## Immediate Comment / Docstring

```lean
/-- [III.P37] Boundary restriction at depth 3. -/
```

## Source Excerpt

```lean
theorem boundary_restriction_3 :
    boundary_restriction_check 3 = true := by native_decide
```
