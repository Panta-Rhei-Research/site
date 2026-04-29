---
{
  "projection_kind": "taulib_declaration",
  "title": "chi_plus_bisquare",
  "permalink": "/verify/taulib/docs/book-i-holomorphy-presheaf-essence/chi-plus-bisquare/",
  "summary_short": "`def` declaration in `TauLib.BookI.Holomorphy.PresheafEssence`.",
  "declaration_id": "TauLib.BookI.Holomorphy.PresheafEssence::chi_plus_bisquare",
  "declaration_slug": "chi-plus-bisquare",
  "kind": "def",
  "name": "chi_plus_bisquare",
  "module_name": "TauLib.BookI.Holomorphy.PresheafEssence",
  "module_url": "/verify/taulib/docs/book-i-holomorphy-presheaf-essence/",
  "source_line_start": 209,
  "source_line_end": 210,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/PresheafEssence.lean#L209-L210",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Holomorphy.PresheafEssence",
        "url": "/verify/taulib/docs/book-i-holomorphy-presheaf-essence/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/PresheafEssence.lean#L209-L210",
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

- Module: [TauLib.BookI.Holomorphy.PresheafEssence](/verify/taulib/docs/book-i-holomorphy-presheaf-essence/)
- Source path: [`TauLib/BookI/Holomorphy/PresheafEssence.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/PresheafEssence.lean#L209-L210)
- Source range: L209-L210
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- χ₊ as a bi-square. -/
```

## Source Excerpt

```lean
def chi_plus_bisquare : BiSquare :=
  BiSquare.of_coherent chi_plus_stage chi_plus_coherent
```
