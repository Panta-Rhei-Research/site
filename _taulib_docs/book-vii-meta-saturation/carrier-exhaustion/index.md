---
{
  "projection_kind": "taulib_declaration",
  "title": "carrier_exhaustion",
  "permalink": "/verify/taulib/docs/book-vii-meta-saturation/carrier-exhaustion/",
  "summary_short": "`theorem` declaration in `TauLib.BookVII.Meta.Saturation`.",
  "declaration_id": "TauLib.BookVII.Meta.Saturation::carrier_exhaustion",
  "declaration_slug": "carrier-exhaustion",
  "kind": "theorem",
  "name": "carrier_exhaustion",
  "module_name": "TauLib.BookVII.Meta.Saturation",
  "module_url": "/verify/taulib/docs/book-vii-meta-saturation/",
  "source_line_start": 288,
  "source_line_end": 292,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Saturation.lean#L288-L292",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Saturation.lean#L288-L292",
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
- Source path: [`TauLib/BookVII/Meta/Saturation.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Saturation.lean#L288-L292)
- Source range: L288-L292
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [VII.Lxx] Carrier Exhaustion: at E₃, the carrier is exhausted.
    SelfDesc² already captures all self-referential structure.
    Further iteration does not produce new content:
    - MetaDecode(MetaDecode(X)) ⊆ MetaDecode(X)
    - The self-model includes the capacity for self-modelling -/
```

## Source Excerpt

```lean
theorem carrier_exhaustion :
    metadecode.self_referential = true ∧
    metadecode.faithful = true ∧
    metadecode.well_defined = true :=
  ⟨rfl, rfl, rfl⟩
```
