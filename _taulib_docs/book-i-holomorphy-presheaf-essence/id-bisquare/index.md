---
{
  "projection_kind": "taulib_declaration",
  "title": "id_bisquare",
  "permalink": "/verify/taulib/docs/book-i-holomorphy-presheaf-essence/id-bisquare/",
  "summary_short": "`def` declaration in `TauLib.BookI.Holomorphy.PresheafEssence`.",
  "declaration_id": "TauLib.BookI.Holomorphy.PresheafEssence::id_bisquare",
  "declaration_slug": "id-bisquare",
  "kind": "def",
  "name": "id_bisquare",
  "module_name": "TauLib.BookI.Holomorphy.PresheafEssence",
  "module_url": "/verify/taulib/docs/book-i-holomorphy-presheaf-essence/",
  "source_line_start": 217,
  "source_line_end": 218,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/PresheafEssence.lean#L217-L218",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/PresheafEssence.lean#L217-L218",
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
- Source path: [`TauLib/BookI/Holomorphy/PresheafEssence.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/PresheafEssence.lean#L217-L218)
- Source range: L217-L218
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The identity as a bi-square. -/
```

## Source Excerpt

```lean
def id_bisquare : BiSquare :=
  BiSquare.of_coherent id_stage id_coherent
```
