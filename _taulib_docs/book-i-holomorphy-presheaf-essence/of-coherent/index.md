---
{
  "projection_kind": "taulib_declaration",
  "title": "BiSquare.of_coherent",
  "permalink": "/verify/taulib/docs/book-i-holomorphy-presheaf-essence/of-coherent/",
  "summary_short": "`def` declaration in `TauLib.BookI.Holomorphy.PresheafEssence`.",
  "declaration_id": "TauLib.BookI.Holomorphy.PresheafEssence::BiSquare.of_coherent",
  "declaration_slug": "of-coherent",
  "kind": "def",
  "name": "BiSquare.of_coherent",
  "module_name": "TauLib.BookI.Holomorphy.PresheafEssence",
  "module_url": "/verify/taulib/docs/book-i-holomorphy-presheaf-essence/",
  "source_line_start": 120,
  "source_line_end": 121,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/PresheafEssence.lean#L120-L121",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/PresheafEssence.lean#L120-L121",
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
- Source path: [`TauLib/BookI/Holomorphy/PresheafEssence.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/PresheafEssence.lean#L120-L121)
- Source range: L120-L121
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Construct a BiSquare from a tower-coherent StageFun. -/
```

## Source Excerpt

```lean
def BiSquare.of_coherent (f : StageFun) (htc : TowerCoherent f) : BiSquare :=
  ⟨f, htc.1, htc.2⟩
```
