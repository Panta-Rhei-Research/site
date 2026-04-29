---
{
  "projection_kind": "taulib_declaration",
  "title": "character_mul_check",
  "permalink": "/verify/taulib/docs/book-ii-central-theorem-boundary-characters/character-mul-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.CentralTheorem.BoundaryCharacters`.",
  "declaration_id": "TauLib.BookII.CentralTheorem.BoundaryCharacters::character_mul_check",
  "declaration_slug": "character-mul-check",
  "kind": "def",
  "name": "character_mul_check",
  "module_name": "TauLib.BookII.CentralTheorem.BoundaryCharacters",
  "module_url": "/verify/taulib/docs/book-ii-central-theorem-boundary-characters/",
  "source_line_start": 201,
  "source_line_end": 219,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/BoundaryCharacters.lean#L201-L219",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/BoundaryCharacters.lean#L201-L219",
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
- Source path: [`TauLib/BookII/CentralTheorem/BoundaryCharacters.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/BoundaryCharacters.lean#L201-L219)
- Source range: L201-L219
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.P14` — Character Algebra Ring Structure

## Immediate Comment / Docstring

```lean
/-- [II.P14] Character multiplication preserves idempotent support:
    if chi1 and chi2 are idempotent-supported, then chi1 * chi2 is also
    idempotent-supported.

    Proof: multiplication in sector coordinates is componentwise:
    (B1, C1) * (B2, C2) = (B1*B2, C1*C2).
    e_plus * (B1*B2, C1*C2) = (B1*B2, 0) and
    e_minus * (B1*B2, C1*C2) = (0, C1*C2). -/
```

## Source Excerpt

```lean
def character_mul_check (bound db : TauIdx) : Bool :=
  go 2 1 ((bound + 1) * (db + 1))
where
  go (x k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if k > db then go (x + 1) 1 (fuel - 1)
    else
      -- Product of canonical and chi_plus characters
      let prod_char := IdempotentCharacter.mul canonical_character chi_plus_character
      let prod_val := prod_char.eval x k
      -- Check idempotent support of the product
      let proj_plus := SectorPair.mul e_plus_sector prod_val
      let proj_minus := SectorPair.mul e_minus_sector prod_val
      let recovery := SectorPair.add proj_plus proj_minus == prod_val
      let b_ok := proj_plus.c_sector == 0
      let c_ok := proj_minus.b_sector == 0
      recovery && b_ok && c_ok && go x (k + 1) (fuel - 1)
  termination_by fuel
```
