---
{
  "projection_kind": "taulib_declaration",
  "title": "FalsificationLevels",
  "permalink": "/verify/taulib/docs/book-v-cosmology-falsification-pack/falsification-levels/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.FalsificationPack`.",
  "declaration_id": "TauLib.BookV.Cosmology.FalsificationPack::FalsificationLevels",
  "declaration_slug": "falsification-levels",
  "kind": "structure",
  "name": "FalsificationLevels",
  "module_name": "TauLib.BookV.Cosmology.FalsificationPack",
  "module_url": "/verify/taulib/docs/book-v-cosmology-falsification-pack/",
  "source_line_start": 86,
  "source_line_end": 99,
  "registry_ids": [
    "V.D184"
  ],
  "related_registry_items": [
    {
      "id": "V.D184",
      "title": "Falsification levels",
      "url": "/registry/object/V.D184/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/FalsificationPack.lean#L86-L99",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.FalsificationPack",
        "url": "/verify/taulib/docs/book-v-cosmology-falsification-pack/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/FalsificationPack.lean#L86-L99",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
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

- Module: [TauLib.BookV.Cosmology.FalsificationPack](/verify/taulib/docs/book-v-cosmology-falsification-pack/)
- Source path: [`TauLib/BookV/Cosmology/FalsificationPack.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/FalsificationPack.lean#L86-L99)
- Source range: L86-L99
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D184` — Falsification levels

## Immediate Comment / Docstring

```lean
/-- [V.D184] Falsification levels: three-tier classification of
    τ-framework predictions by falsifiability strength and
    experimental accessibility.

    Level 1: structural — would refute entire framework
    Level 2: quantitative — tests specific numerical values
    Level 3: frontier — requires future technology -/
```

## Source Excerpt

```lean
structure FalsificationLevels where
  /-- Level 1 predictions. -/
  structural : List TestablePrediction
  /-- Level 2 predictions. -/
  quantitative : List TestablePrediction
  /-- Level 3 predictions. -/
  frontier : List TestablePrediction
  /-- At least one structural prediction. -/
  has_structural : structural.length > 0
  /-- At least one quantitative prediction. -/
  has_quantitative : quantitative.length > 0
  /-- At least one frontier prediction. -/
  has_frontier : frontier.length > 0
  deriving Repr
```
