---
{
  "projection_kind": "taulib_declaration",
  "title": "neg_neg_char",
  "permalink": "/corpus/taulib/docs/book-iii-sectors-boundary-characters/neg-neg-char/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Sectors.BoundaryCharacters`.",
  "declaration_id": "TauLib.BookIII.Sectors.BoundaryCharacters::neg_neg_char",
  "declaration_slug": "neg-neg-char",
  "kind": "theorem",
  "name": "neg_neg_char",
  "module_name": "TauLib.BookIII.Sectors.BoundaryCharacters",
  "module_url": "/corpus/taulib/docs/book-iii-sectors-boundary-characters/",
  "source_line_start": 201,
  "source_line_end": 203,
  "registry_ids": [
    "III.D11"
  ],
  "related_registry_items": [
    {
      "id": "III.D11",
      "title": "Boundary Character Space",
      "url": "/registry/object/III.D11/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Sectors/BoundaryCharacters.lean#L201-L203",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Sectors.BoundaryCharacters",
        "url": "/corpus/taulib/docs/book-iii-sectors-boundary-characters/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Sectors/BoundaryCharacters.lean#L201-L203",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "role": "proof obligation",
      "status": "formal proof obligation checked"
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

- Module: [TauLib.BookIII.Sectors.BoundaryCharacters](/corpus/taulib/docs/book-iii-sectors-boundary-characters/)
- Source path: [`TauLib/BookIII/Sectors/BoundaryCharacters.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Sectors/BoundaryCharacters.lean#L201-L203)
- Source range: L201-L203
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- `III.D11` — Boundary Character Space

## Immediate Comment / Docstring

```lean
/-- [III.D11] Structural: character negation is an involution. -/
```

## Source Excerpt

```lean
theorem neg_neg_char (χ : BoundaryCharacter) :
    χ.neg.neg = χ := by
  simp only [BoundaryCharacter.neg, Int.neg_neg]
```
