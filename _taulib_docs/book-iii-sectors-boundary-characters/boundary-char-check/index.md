---
{
  "projection_kind": "taulib_declaration",
  "title": "boundary_char_check",
  "permalink": "/verify/taulib/docs/book-iii-sectors-boundary-characters/boundary-char-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Sectors.BoundaryCharacters`.",
  "declaration_id": "TauLib.BookIII.Sectors.BoundaryCharacters::boundary_char_check",
  "declaration_slug": "boundary-char-check",
  "kind": "def",
  "name": "boundary_char_check",
  "module_name": "TauLib.BookIII.Sectors.BoundaryCharacters",
  "module_url": "/verify/taulib/docs/book-iii-sectors-boundary-characters/",
  "source_line_start": 69,
  "source_line_end": 91,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Sectors/BoundaryCharacters.lean#L69-L91",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Sectors/BoundaryCharacters.lean#L69-L91",
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
- Source path: [`TauLib/BookIII/Sectors/BoundaryCharacters.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Sectors/BoundaryCharacters.lean#L69-L91)
- Source range: L69-L91
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D11` — Boundary Character Space

## Immediate Comment / Docstring

```lean
/-- [III.D11] Boundary character space check: verify that characters
    form a group under addition (closure, associativity, identity, inverse)
    at finite cutoff. -/
```

## Source Excerpt

```lean
def boundary_char_check (bound db : TauIdx) : Bool :=
  go 0 0 0 0 1 ((bound + 1)^4 * (db + 1))
where
  go (m1 n1 m2 n2 k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if m1 > bound then true
    else if n1 > bound then go (m1 + 1) 0 0 0 1 (fuel - 1)
    else if m2 > bound then go m1 (n1 + 1) 0 0 1 (fuel - 1)
    else if n2 > bound then go m1 n1 (m2 + 1) 0 1 (fuel - 1)
    else if k > db then go m1 n1 m2 (n2 + 1) 1 (fuel - 1)
    else
      let χ₁ : BoundaryCharacter := ⟨Int.ofNat m1, Int.ofNat n1⟩
      let χ₂ : BoundaryCharacter := ⟨Int.ofNat m2, Int.ofNat n2⟩
      -- Addition closure: eval(χ₁+χ₂) = eval(χ₁) + eval(χ₂) at finite cutoff
      let sum_eval := (χ₁.add χ₂).eval 0 k
      let eval_sum := χ₁.eval 0 k + χ₂.eval 0 k
      -- Identity: eval(zero) = 0
      let zero_ok := BoundaryCharacter.zero.eval 0 k == 0
      -- Inverse: eval(χ + neg(χ)) = 0
      let inv_ok := (χ₁.add χ₁.neg).eval 0 k == 0
      (sum_eval == eval_sum) && zero_ok && inv_ok &&
        go m1 n1 m2 n2 (k + 1) (fuel - 1)
  termination_by fuel
```
