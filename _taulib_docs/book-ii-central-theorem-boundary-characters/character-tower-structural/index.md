---
{
  "projection_kind": "taulib_declaration",
  "title": "character_tower_structural",
  "permalink": "/corpus/taulib/docs/book-ii-central-theorem-boundary-characters/character-tower-structural/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.CentralTheorem.BoundaryCharacters`.",
  "declaration_id": "TauLib.BookII.CentralTheorem.BoundaryCharacters::character_tower_structural",
  "declaration_slug": "character-tower-structural",
  "kind": "theorem",
  "name": "character_tower_structural",
  "module_name": "TauLib.BookII.CentralTheorem.BoundaryCharacters",
  "module_url": "/corpus/taulib/docs/book-ii-central-theorem-boundary-characters/",
  "source_line_start": 329,
  "source_line_end": 331,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/BoundaryCharacters.lean#L329-L331",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.CentralTheorem.BoundaryCharacters",
        "url": "/corpus/taulib/docs/book-ii-central-theorem-boundary-characters/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/BoundaryCharacters.lean#L329-L331",
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

- Module: [TauLib.BookII.CentralTheorem.BoundaryCharacters](/corpus/taulib/docs/book-ii-central-theorem-boundary-characters/)
- Source path: [`TauLib/BookII/CentralTheorem/BoundaryCharacters.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/BoundaryCharacters.lean#L329-L331)
- Source range: L329-L331
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- `II.D59` — Idempotent-Supported Character

## Immediate Comment / Docstring

```lean
/-- [II.D59] Character tower coherence: the canonical character input
    at stage k equals the stage-(k+1) input reduced.
    reduce(reduce(x, k+1), k) = reduce(x, k). -/
```

## Source Excerpt

```lean
theorem character_tower_structural (x : TauIdx) {k : TauIdx} (_ : k ≤ k + 1) :
    reduce (reduce x (k + 1)) k = reduce x k :=
  reduction_compat x (Nat.le_succ k)
```
