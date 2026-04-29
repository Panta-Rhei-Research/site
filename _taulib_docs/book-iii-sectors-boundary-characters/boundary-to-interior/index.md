---
{
  "projection_kind": "taulib_declaration",
  "title": "boundary_to_interior",
  "permalink": "/verify/taulib/docs/book-iii-sectors-boundary-characters/boundary-to-interior/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Sectors.BoundaryCharacters`.",
  "declaration_id": "TauLib.BookIII.Sectors.BoundaryCharacters::boundary_to_interior",
  "declaration_slug": "boundary-to-interior",
  "kind": "def",
  "name": "boundary_to_interior",
  "module_name": "TauLib.BookIII.Sectors.BoundaryCharacters",
  "module_url": "/verify/taulib/docs/book-iii-sectors-boundary-characters/",
  "source_line_start": 104,
  "source_line_end": 106,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Sectors/BoundaryCharacters.lean#L104-L106",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Sectors/BoundaryCharacters.lean#L104-L106",
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
- Source path: [`TauLib/BookIII/Sectors/BoundaryCharacters.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Sectors/BoundaryCharacters.lean#L104-L106)
- Source range: L104-L106
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D12` — Boundary-to-Interior Functor

## Immediate Comment / Docstring

```lean
/-- [III.D12] Boundary-to-interior functor Φ: Char(L) → O(τ³).
    Maps a boundary character (m,n) to its interior holomorphic extension.
    At finite cutoff: Φ(χ)(x, k) = reduce((|m| + |n|) · reduce(x, k), k).

    This definition is manifestly tower-coherent: since reduce(x, k+1) ≡
    reduce(x, k) mod P_k, the character-weighted value also reduces correctly.
    This is Langlands₀: boundary functoriality. -/
```

## Source Excerpt

```lean
def boundary_to_interior (χ : BoundaryCharacter) (x k : TauIdx) : TauIdx :=
  let rx := reduce x k
  reduce (rx * (χ.m_index.natAbs + χ.n_index.natAbs)) k
```
