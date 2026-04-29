---
{
  "projection_kind": "taulib_declaration",
  "title": "bti_additive_check",
  "permalink": "/verify/taulib/docs/book-iii-sectors-boundary-characters/bti-additive-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Sectors.BoundaryCharacters`.",
  "declaration_id": "TauLib.BookIII.Sectors.BoundaryCharacters::bti_additive_check",
  "declaration_slug": "bti-additive-check",
  "kind": "def",
  "name": "bti_additive_check",
  "module_name": "TauLib.BookIII.Sectors.BoundaryCharacters",
  "module_url": "/verify/taulib/docs/book-iii-sectors-boundary-characters/",
  "source_line_start": 137,
  "source_line_end": 154,
  "registry_ids": [
    "III.D12"
  ],
  "related_registry_items": [
    {
      "id": "III.D12",
      "title": "Boundary-to-Interior Functor",
      "url": "/registry/object/III.D12/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Sectors/BoundaryCharacters.lean#L137-L154",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Sectors/BoundaryCharacters.lean#L137-L154",
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
- Source path: [`TauLib/BookIII/Sectors/BoundaryCharacters.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Sectors/BoundaryCharacters.lean#L137-L154)
- Source range: L137-L154
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D12` — Boundary-to-Interior Functor

## Immediate Comment / Docstring

```lean
/-- [III.D12] BTI functor preserves character addition:
    Φ(χ₁ + χ₂) tower-agrees with Φ(χ₁) + Φ(χ₂) at finite cutoff. -/
```

## Source Excerpt

```lean
def bti_additive_check (bound db : TauIdx) : Bool :=
  go 0 0 0 1 ((bound + 1)^3 * (db + 1))
where
  go (m1 m2 x k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if m1 > bound then true
    else if m2 > bound then go (m1 + 1) 0 0 1 (fuel - 1)
    else if x > bound then go m1 (m2 + 1) 0 1 (fuel - 1)
    else if k > db then go m1 m2 (x + 1) 1 (fuel - 1)
    else
      let χ₁ : BoundaryCharacter := ⟨Int.ofNat m1, 0⟩
      let χ₂ : BoundaryCharacter := ⟨Int.ofNat m2, 0⟩
      let sum_val := boundary_to_interior (χ₁.add χ₂) x k
      let val1 := boundary_to_interior χ₁ x k
      let val2 := boundary_to_interior χ₂ x k
      let add_val := reduce (val1 + val2) k
      sum_val == add_val && go m1 m2 x (k + 1) (fuel - 1)
  termination_by fuel
```
