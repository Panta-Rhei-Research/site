---
{
  "projection_kind": "taulib_declaration",
  "title": "BoundaryCharacter.add",
  "permalink": "/verify/taulib/docs/book-iii-sectors-boundary-characters/add/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Sectors.BoundaryCharacters`.",
  "declaration_id": "TauLib.BookIII.Sectors.BoundaryCharacters::BoundaryCharacter.add",
  "declaration_slug": "add",
  "kind": "def",
  "name": "BoundaryCharacter.add",
  "module_name": "TauLib.BookIII.Sectors.BoundaryCharacters",
  "module_url": "/verify/taulib/docs/book-iii-sectors-boundary-characters/",
  "source_line_start": 50,
  "source_line_end": 51,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Sectors/BoundaryCharacters.lean#L50-L51",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Sectors.BoundaryCharacters",
        "url": "/verify/taulib/docs/book-iii-sectors-boundary-characters/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Sectors/BoundaryCharacters.lean#L50-L51",
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

- Module: [TauLib.BookIII.Sectors.BoundaryCharacters](/verify/taulib/docs/book-iii-sectors-boundary-characters/)
- Source path: [`TauLib/BookIII/Sectors/BoundaryCharacters.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Sectors/BoundaryCharacters.lean#L50-L51)
- Source range: L50-L51
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Character addition on ℤ². -/
```

## Source Excerpt

```lean
def BoundaryCharacter.add (χ₁ χ₂ : BoundaryCharacter) : BoundaryCharacter :=
  ⟨χ₁.m_index + χ₂.m_index, χ₁.n_index + χ₂.n_index⟩
```
