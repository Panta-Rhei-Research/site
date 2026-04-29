---
{
  "projection_kind": "taulib_declaration",
  "title": "IdempotentCharacter",
  "permalink": "/verify/taulib/docs/book-ii-central-theorem-boundary-characters/idempotent-character/",
  "summary_short": "`structure` declaration in `TauLib.BookII.CentralTheorem.BoundaryCharacters`.",
  "declaration_id": "TauLib.BookII.CentralTheorem.BoundaryCharacters::IdempotentCharacter",
  "declaration_slug": "idempotent-character",
  "kind": "structure",
  "name": "IdempotentCharacter",
  "module_name": "TauLib.BookII.CentralTheorem.BoundaryCharacters",
  "module_url": "/verify/taulib/docs/book-ii-central-theorem-boundary-characters/",
  "source_line_start": 58,
  "source_line_end": 63,
  "registry_ids": [
    "II.D59"
  ],
  "related_registry_items": [
    {
      "id": "II.D59",
      "title": "Idempotent-Supported Character",
      "url": "/registry/object/II.D59/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/BoundaryCharacters.lean#L58-L63",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.CentralTheorem.BoundaryCharacters",
        "url": "/verify/taulib/docs/book-ii-central-theorem-boundary-characters/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/BoundaryCharacters.lean#L58-L63",
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

- Module: [TauLib.BookII.CentralTheorem.BoundaryCharacters](/verify/taulib/docs/book-ii-central-theorem-boundary-characters/)
- Source path: [`TauLib/BookII/CentralTheorem/BoundaryCharacters.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/BoundaryCharacters.lean#L58-L63)
- Source range: L58-L63
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `II.D59` — Idempotent-Supported Character

## Immediate Comment / Docstring

```lean
/-- [II.D59] An idempotent-supported character is a stagewise map
    from (x, k) to a SectorPair, representing the B-channel and
    C-channel components. The character is determined by its
    idempotent projections: chi = e_plus * chi_plus + e_minus * chi_minus.

    In the primorial model, the character at stage k on input x is:
    - B-component: the B-coordinate of from_tau_idx(reduce(x, k))
    - C-component: the C-coordinate of from_tau_idx(reduce(x, k))

    This is the canonical character associated to x. -/
```

## Source Excerpt

```lean
structure IdempotentCharacter where
  /-- B-channel function: (x, k) -> B-component at stage k. -/
  b_ch : TauIdx -> TauIdx -> Int
  /-- C-channel function: (x, k) -> C-component at stage k. -/
  c_ch : TauIdx -> TauIdx -> Int
  deriving Inhabited
```
