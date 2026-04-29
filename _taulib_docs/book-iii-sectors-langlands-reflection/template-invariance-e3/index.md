---
{
  "projection_kind": "taulib_declaration",
  "title": "template_invariance_e3",
  "permalink": "/verify/taulib/docs/book-iii-sectors-langlands-reflection/template-invariance-e3/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Sectors.LanglandsReflection`.",
  "declaration_id": "TauLib.BookIII.Sectors.LanglandsReflection::template_invariance_e3",
  "declaration_slug": "template-invariance-e3",
  "kind": "theorem",
  "name": "template_invariance_e3",
  "module_name": "TauLib.BookIII.Sectors.LanglandsReflection",
  "module_url": "/verify/taulib/docs/book-iii-sectors-langlands-reflection/",
  "source_line_start": 264,
  "source_line_end": 265,
  "registry_ids": [
    "III.T06"
  ],
  "related_registry_items": [
    {
      "id": "III.T06",
      "title": "Template Invariance Under Reflection",
      "url": "/registry/object/III.T06/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Sectors/LanglandsReflection.lean#L264-L265",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Sectors.LanglandsReflection",
        "url": "/verify/taulib/docs/book-iii-sectors-langlands-reflection/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Sectors/LanglandsReflection.lean#L264-L265",
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

- Module: [TauLib.BookIII.Sectors.LanglandsReflection](/verify/taulib/docs/book-iii-sectors-langlands-reflection/)
- Source path: [`TauLib/BookIII/Sectors/LanglandsReflection.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Sectors/LanglandsReflection.lean#L264-L265)
- Source range: L264-L265
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.T06` — Template Invariance Under Reflection

## Immediate Comment / Docstring

```lean
/-- [III.T06] Structural: template invariance at E₃ is trivial
    since E₃.succ = E₃ (saturation). -/
```

## Source Excerpt

```lean
theorem template_invariance_e3 :
    layer_of EnrLevel.E3 8 3 = layer_of EnrLevel.E3.succ 8 3 := rfl
```
