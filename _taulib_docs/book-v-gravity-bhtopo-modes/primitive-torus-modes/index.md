---
{
  "projection_kind": "taulib_declaration",
  "title": "primitiveTorusModes",
  "permalink": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/primitive-torus-modes/",
  "summary_short": "`def` declaration in `TauLib.BookV.Gravity.BHTopoModes`.",
  "declaration_id": "TauLib.BookV.Gravity.BHTopoModes::primitiveTorusModes",
  "declaration_slug": "primitive-torus-modes",
  "kind": "def",
  "name": "primitiveTorusModes",
  "module_name": "TauLib.BookV.Gravity.BHTopoModes",
  "module_url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/",
  "source_line_start": 65,
  "source_line_end": 68,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/BHTopoModes.lean#L65-L68",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Gravity.BHTopoModes",
        "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/BHTopoModes.lean#L65-L68",
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

- Module: [TauLib.BookV.Gravity.BHTopoModes](/verify/taulib/docs/book-v-gravity-bhtopo-modes/)
- Source path: [`TauLib/BookV/Gravity/BHTopoModes.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/BHTopoModes.lean#L65-L68)
- Source range: L65-L68
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The three primitive torus modes with lowest non-zero QNM frequencies. -/
```

## Source Excerpt

```lean
def primitiveTorusModes : List TorusMode :=
  [{ n := 1, m := 0 },   -- outer cycle: f(1,0) = c/(2πR)
   { n := 0, m := 1 },   -- inner cycle: f(0,1) = c/(2πr) = ι_τ⁻¹·f(1,0)
   { n := 1, m := 1 }]   -- diagonal:   f(1,1) = √(1+ι_τ⁻²)·f(1,0)
```
