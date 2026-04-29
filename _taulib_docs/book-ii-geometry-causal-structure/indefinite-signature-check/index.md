---
{
  "projection_kind": "taulib_declaration",
  "title": "indefinite_signature_check",
  "permalink": "/verify/taulib/docs/book-ii-geometry-causal-structure/indefinite-signature-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Geometry.CausalStructure`.",
  "declaration_id": "TauLib.BookII.Geometry.CausalStructure::indefinite_signature_check",
  "declaration_slug": "indefinite-signature-check",
  "kind": "def",
  "name": "indefinite_signature_check",
  "module_name": "TauLib.BookII.Geometry.CausalStructure",
  "module_url": "/verify/taulib/docs/book-ii-geometry-causal-structure/",
  "source_line_start": 146,
  "source_line_end": 150,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Geometry/CausalStructure.lean#L146-L150",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Geometry.CausalStructure",
        "url": "/verify/taulib/docs/book-ii-geometry-causal-structure/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Geometry/CausalStructure.lean#L146-L150",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "status": "defined"
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

- Module: [TauLib.BookII.Geometry.CausalStructure](/verify/taulib/docs/book-ii-geometry-causal-structure/)
- Source path: [`TauLib/BookII/Geometry/CausalStructure.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Geometry/CausalStructure.lean#L146-L150)
- Source range: L146-L150
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Contrast: split-complex norm has INDEFINITE signature.
    Some nonzero vectors have negative norm squared. -/
```

## Source Excerpt

```lean
def indefinite_signature_check : Bool :=
  -- (0, 1) has split-complex norm 0² - 1² = -1 < 0 (spacelike)
  classify_causal 0 1 == .spacelike &&
  -- (1, 0) has split-complex norm 1² - 0² = +1 > 0 (timelike)
  classify_causal 1 0 == .timelike
```
