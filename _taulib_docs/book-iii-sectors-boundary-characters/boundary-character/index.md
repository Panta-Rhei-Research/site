---
{
  "projection_kind": "taulib_declaration",
  "title": "BoundaryCharacter",
  "permalink": "/corpus/taulib/docs/book-iii-sectors-boundary-characters/boundary-character/",
  "summary_short": "`structure` declaration in `TauLib.BookIII.Sectors.BoundaryCharacters`.",
  "declaration_id": "TauLib.BookIII.Sectors.BoundaryCharacters::BoundaryCharacter",
  "declaration_slug": "boundary-character",
  "kind": "structure",
  "name": "BoundaryCharacter",
  "module_name": "TauLib.BookIII.Sectors.BoundaryCharacters",
  "module_url": "/corpus/taulib/docs/book-iii-sectors-boundary-characters/",
  "source_line_start": 41,
  "source_line_end": 44,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Sectors/BoundaryCharacters.lean#L41-L44",
  "formal_status": "defined",
  "declaration_role": "type/data schema",
  "formal_status_label": "type/data schema",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Sectors/BoundaryCharacters.lean#L41-L44",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
      "role": "type/data schema",
      "status": "type/data schema"
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
- Source path: [`TauLib/BookIII/Sectors/BoundaryCharacters.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Sectors/BoundaryCharacters.lean#L41-L44)
- Source range: L41-L44
- Kind: `structure`
- Public role: `type/data schema`
- Formal status hint: `type/data schema`

## Registry Links

- `III.D11` — Boundary Character Space

## Immediate Comment / Docstring

```lean
/-- [III.D11] A boundary character on L = S¹ ∨ S¹.
    Indexed by (m, n) ∈ ℤ² where:
    - m = multiplicative/Galois axis (B-lobe winding number)
    - n = additive/automorphic axis (C-lobe winding number)
    The character lattice is ℤ² from H₁(L; ℤ) ≅ ℤ ⊕ ℤ. -/
```

## Source Excerpt

```lean
structure BoundaryCharacter where
  m_index : Int  -- multiplicative/Galois axis
  n_index : Int  -- additive/automorphic axis
  deriving Repr, DecidableEq, BEq, Inhabited
```
