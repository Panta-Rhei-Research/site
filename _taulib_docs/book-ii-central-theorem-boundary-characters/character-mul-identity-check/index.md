---
{
  "projection_kind": "taulib_declaration",
  "title": "character_mul_identity_check",
  "permalink": "/verify/taulib/docs/book-ii-central-theorem-boundary-characters/character-mul-identity-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.CentralTheorem.BoundaryCharacters`.",
  "declaration_id": "TauLib.BookII.CentralTheorem.BoundaryCharacters::character_mul_identity_check",
  "declaration_slug": "character-mul-identity-check",
  "kind": "def",
  "name": "character_mul_identity_check",
  "module_name": "TauLib.BookII.CentralTheorem.BoundaryCharacters",
  "module_url": "/verify/taulib/docs/book-ii-central-theorem-boundary-characters/",
  "source_line_start": 250,
  "source_line_end": 261,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/BoundaryCharacters.lean#L250-L261",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/BoundaryCharacters.lean#L250-L261",
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
- Source path: [`TauLib/BookII/CentralTheorem/BoundaryCharacters.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/BoundaryCharacters.lean#L250-L261)
- Source range: L250-L261
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.P14` — Character Algebra Ring Structure

## Immediate Comment / Docstring

```lean
/-- [II.P14] Ring axiom: multiplicative identity check.
    chi * 1 = chi for the canonical character. -/
```

## Source Excerpt

```lean
def character_mul_identity_check (bound db : TauIdx) : Bool :=
  go 2 1 ((bound + 1) * (db + 1))
where
  go (x k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if k > db then go (x + 1) 1 (fuel - 1)
    else
      let orig := canonical_character.eval x k
      let prod := (IdempotentCharacter.mul canonical_character unit_character).eval x k
      (orig == prod) && go x (k + 1) (fuel - 1)
  termination_by fuel
```
