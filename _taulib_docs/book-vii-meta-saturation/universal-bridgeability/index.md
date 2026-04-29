---
{
  "projection_kind": "taulib_declaration",
  "title": "universal_bridgeability",
  "permalink": "/verify/taulib/docs/book-vii-meta-saturation/universal-bridgeability/",
  "summary_short": "`theorem` declaration in `TauLib.BookVII.Meta.Saturation`.",
  "declaration_id": "TauLib.BookVII.Meta.Saturation::universal_bridgeability",
  "declaration_slug": "universal-bridgeability",
  "kind": "theorem",
  "name": "universal_bridgeability",
  "module_name": "TauLib.BookVII.Meta.Saturation",
  "module_url": "/verify/taulib/docs/book-vii-meta-saturation/",
  "source_line_start": 703,
  "source_line_end": 706,
  "registry_ids": [
    "VII.P13"
  ],
  "related_registry_items": [
    {
      "id": "VII.P13",
      "title": "Universal Bridgeability",
      "url": "/registry/object/VII.P13/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Saturation.lean#L703-L706",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVII.Meta.Saturation",
        "url": "/verify/taulib/docs/book-vii-meta-saturation/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Saturation.lean#L703-L706",
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

- Module: [TauLib.BookVII.Meta.Saturation](/verify/taulib/docs/book-vii-meta-saturation/)
- Source path: [`TauLib/BookVII/Meta/Saturation.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Saturation.lean#L703-L706)
- Source range: L703-L706
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `VII.P13` — Universal Bridgeability

## Immediate Comment / Docstring

```lean
/-- [VII.P13] Universal Bridgeability (ch63). Any E₂+ system
    (with SelfDesc) can bridge to linguistic representation.
    The bridge functor from subsymbolic to symbolic is available
    at E₂ and higher. -/
```

## Source Excerpt

```lean
theorem universal_bridgeability :
    subsymbolic.pre_symbolic = true ∧
    subsymbolic.pattern_recognition = true :=
  ⟨rfl, rfl⟩
```
