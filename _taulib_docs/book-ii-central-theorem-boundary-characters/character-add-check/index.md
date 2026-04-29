---
{
  "projection_kind": "taulib_declaration",
  "title": "character_add_check",
  "permalink": "/verify/taulib/docs/book-ii-central-theorem-boundary-characters/character-add-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.CentralTheorem.BoundaryCharacters`.",
  "declaration_id": "TauLib.BookII.CentralTheorem.BoundaryCharacters::character_add_check",
  "declaration_slug": "character-add-check",
  "kind": "def",
  "name": "character_add_check",
  "module_name": "TauLib.BookII.CentralTheorem.BoundaryCharacters",
  "module_url": "/verify/taulib/docs/book-ii-central-theorem-boundary-characters/",
  "source_line_start": 164,
  "source_line_end": 182,
  "registry_ids": [
    "II.P14"
  ],
  "related_registry_items": [
    {
      "id": "II.P14",
      "title": "Character Algebra Ring Structure",
      "url": "/registry/object/II.P14/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/BoundaryCharacters.lean#L164-L182",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/BoundaryCharacters.lean#L164-L182",
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
- Source path: [`TauLib/BookII/CentralTheorem/BoundaryCharacters.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/BoundaryCharacters.lean#L164-L182)
- Source range: L164-L182
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.P14` — Character Algebra Ring Structure

## Immediate Comment / Docstring

```lean
/-- [II.P14] Character addition preserves idempotent support:
    if chi1 and chi2 are idempotent-supported, then chi1 + chi2 is also
    idempotent-supported.

    Proof: e_plus * (B1+B2, C1+C2) = (B1+B2, 0) and
    e_minus * (B1+B2, C1+C2) = (0, C1+C2), and their sum
    = (B1+B2, C1+C2) = (chi1 + chi2). -/
```

## Source Excerpt

```lean
def character_add_check (bound db : TauIdx) : Bool :=
  go 2 1 ((bound + 1) * (db + 1))
where
  go (x k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if k > db then go (x + 1) 1 (fuel - 1)
    else
      -- Sum of canonical and chi_plus characters
      let sum_char := IdempotentCharacter.add canonical_character chi_plus_character
      let sum_val := sum_char.eval x k
      -- Check idempotent support of the sum
      let proj_plus := SectorPair.mul e_plus_sector sum_val
      let proj_minus := SectorPair.mul e_minus_sector sum_val
      let recovery := SectorPair.add proj_plus proj_minus == sum_val
      let b_ok := proj_plus.c_sector == 0
      let c_ok := proj_minus.b_sector == 0
      recovery && b_ok && c_ok && go x (k + 1) (fuel - 1)
  termination_by fuel
```
