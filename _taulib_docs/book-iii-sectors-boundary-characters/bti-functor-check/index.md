---
{
  "projection_kind": "taulib_declaration",
  "title": "bti_functor_check",
  "permalink": "/verify/taulib/docs/book-iii-sectors-boundary-characters/bti-functor-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Sectors.BoundaryCharacters`.",
  "declaration_id": "TauLib.BookIII.Sectors.BoundaryCharacters::bti_functor_check",
  "declaration_slug": "bti-functor-check",
  "kind": "def",
  "name": "bti_functor_check",
  "module_name": "TauLib.BookIII.Sectors.BoundaryCharacters",
  "module_url": "/verify/taulib/docs/book-iii-sectors-boundary-characters/",
  "source_line_start": 111,
  "source_line_end": 133,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Sectors/BoundaryCharacters.lean#L111-L133",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Sectors/BoundaryCharacters.lean#L111-L133",
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
- Source path: [`TauLib/BookIII/Sectors/BoundaryCharacters.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Sectors/BoundaryCharacters.lean#L111-L133)
- Source range: L111-L133
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D12` — Boundary-to-Interior Functor

## Immediate Comment / Docstring

```lean
/-- [III.D12] BTI functor preserves tower coherence:
    reduce(Φ(χ)(x, k+1), k) = Φ(χ)(x, k).
    This is the holomorphic extension property. -/
```

## Source Excerpt

```lean
def bti_functor_check (bound db : TauIdx) : Bool :=
  go 0 0 1 ((bound + 1) * (bound + 1) * (db + 1))
where
  go (m x k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if m > bound then true
    else if x > bound then go (m + 1) 0 1 (fuel - 1)
    else if k >= db then go m (x + 1) 1 (fuel - 1)
    else
      -- Test m-axis character
      let χ_m : BoundaryCharacter := ⟨Int.ofNat m, 0⟩
      let val_high_m := boundary_to_interior χ_m x (k + 1)
      let projected_m := reduce val_high_m k
      let val_low_m := boundary_to_interior χ_m x k
      let m_ok := projected_m == val_low_m
      -- Test n-axis character
      let χ_n : BoundaryCharacter := ⟨0, Int.ofNat m⟩
      let val_high_n := boundary_to_interior χ_n x (k + 1)
      let projected_n := reduce val_high_n k
      let val_low_n := boundary_to_interior χ_n x k
      let n_ok := projected_n == val_low_n
      m_ok && n_ok && go m x (k + 1) (fuel - 1)
  termination_by fuel
```
