---
{
  "projection_kind": "taulib_declaration",
  "title": "alpha_tower_numer",
  "permalink": "/corpus/taulib/docs/book-iv-sectors-fine-structure/alpha-tower-numer/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Sectors.FineStructure`.",
  "declaration_id": "TauLib.BookIV.Sectors.FineStructure::alpha_tower_numer",
  "declaration_slug": "alpha-tower-numer",
  "kind": "def",
  "name": "alpha_tower_numer",
  "module_name": "TauLib.BookIV.Sectors.FineStructure",
  "module_url": "/corpus/taulib/docs/book-iv-sectors-fine-structure/",
  "source_line_start": 203,
  "source_line_end": 203,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/FineStructure.lean#L203-L203",
  "formal_status": "defined",
  "declaration_role": "data/computed value",
  "formal_status_label": "data/computed value",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Sectors.FineStructure",
        "url": "/corpus/taulib/docs/book-iv-sectors-fine-structure/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/FineStructure.lean#L203-L203",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "role": "data/computed value",
      "status": "data/computed value"
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

- Module: [TauLib.BookIV.Sectors.FineStructure](/corpus/taulib/docs/book-iv-sectors-fine-structure/)
- Source path: [`TauLib/BookIV/Sectors/FineStructure.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/FineStructure.lean#L203-L203)
- Source range: L203-L203
- Kind: `def`
- Public role: `data/computed value`
- Formal status hint: `data/computed value`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The tower fine-structure constant numerator: 121 · ι_τ⁴.
    121 = ω₁² = 11² from the iterated prime tower. -/
```

## Source Excerpt

```lean
def alpha_tower_numer : Nat := 121 * iota_fourth_numer
```
