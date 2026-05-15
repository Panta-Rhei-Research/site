---
{
  "projection_kind": "taulib_declaration",
  "title": "bti_zero",
  "permalink": "/corpus/taulib/docs/book-iii-sectors-boundary-characters/bti-zero/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Sectors.BoundaryCharacters`.",
  "declaration_id": "TauLib.BookIII.Sectors.BoundaryCharacters::bti_zero",
  "declaration_slug": "bti-zero",
  "kind": "theorem",
  "name": "bti_zero",
  "module_name": "TauLib.BookIII.Sectors.BoundaryCharacters",
  "module_url": "/corpus/taulib/docs/book-iii-sectors-boundary-characters/",
  "source_line_start": 207,
  "source_line_end": 212,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Sectors/BoundaryCharacters.lean#L207-L212",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Sectors/BoundaryCharacters.lean#L207-L212",
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

- Module: [TauLib.BookIII.Sectors.BoundaryCharacters](/corpus/taulib/docs/book-iii-sectors-boundary-characters/)
- Source path: [`TauLib/BookIII/Sectors/BoundaryCharacters.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Sectors/BoundaryCharacters.lean#L207-L212)
- Source range: L207-L212
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- `III.D12` — Boundary-to-Interior Functor

## Immediate Comment / Docstring

```lean
/-- [III.D12] Structural: BTI of trivial character is zero.
    Φ(0)(x, k) = reduce(0, k) = 0. -/
```

## Source Excerpt

```lean
theorem bti_zero (x k : TauIdx) :
    boundary_to_interior BoundaryCharacter.zero x k = 0 := by
  simp only [boundary_to_interior, BoundaryCharacter.zero, Int.natAbs_zero,
             Nat.add_zero, Nat.mul_zero, reduce, Nat.zero_mod]

end Tau.BookIII.Sectors
```
