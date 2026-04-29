---
{
  "projection_kind": "taulib_declaration",
  "title": "idemp_character_check",
  "permalink": "/verify/taulib/docs/book-ii-central-theorem-boundary-characters/idemp-character-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.CentralTheorem.BoundaryCharacters`.",
  "declaration_id": "TauLib.BookII.CentralTheorem.BoundaryCharacters::idemp_character_check",
  "declaration_slug": "idemp-character-check",
  "kind": "def",
  "name": "idemp_character_check",
  "module_name": "TauLib.BookII.CentralTheorem.BoundaryCharacters",
  "module_url": "/verify/taulib/docs/book-ii-central-theorem-boundary-characters/",
  "source_line_start": 95,
  "source_line_end": 115,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/BoundaryCharacters.lean#L95-L115",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/BoundaryCharacters.lean#L95-L115",
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

- Module: [TauLib.BookII.CentralTheorem.BoundaryCharacters](/verify/taulib/docs/book-ii-central-theorem-boundary-characters/)
- Source path: [`TauLib/BookII/CentralTheorem/BoundaryCharacters.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/BoundaryCharacters.lean#L95-L115)
- Source range: L95-L115
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D59` — Idempotent-Supported Character

## Immediate Comment / Docstring

```lean
/-- [II.D59] Idempotent decomposition check: for each x at stage k,
    the character value (B, C) satisfies
    e_plus * (B, C) + e_minus * (B, C) = (B, C).

    This verifies that the character IS its own idempotent decomposition:
    the B-channel and C-channel projections sum to the full character. -/
```

## Source Excerpt

```lean
def idemp_character_check (bound db : TauIdx) : Bool :=
  go 2 1 ((bound + 1) * (db + 1))
where
  go (x k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if k > db then go (x + 1) 1 (fuel - 1)
    else
      let chi := canonical_character.eval x k
      -- e_plus * chi = (B, 0)
      let proj_plus := SectorPair.mul e_plus_sector chi
      -- e_minus * chi = (0, C)
      let proj_minus := SectorPair.mul e_minus_sector chi
      -- e_plus * chi + e_minus * chi = chi
      let recovery := SectorPair.add proj_plus proj_minus == chi
      -- B-channel projection has zero C
      let b_ok := proj_plus.c_sector == 0
      -- C-channel projection has zero B
      let c_ok := proj_minus.b_sector == 0
      recovery && b_ok && c_ok && go x (k + 1) (fuel - 1)
  termination_by fuel
```
