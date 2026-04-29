---
{
  "projection_kind": "taulib_declaration",
  "title": "h6_section6_synthesis",
  "permalink": "/verify/taulib/docs/book-i-holomorphy-h6-diagonal-discipline/h6-section6-synthesis/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Holomorphy.H6DiagonalDiscipline`.",
  "declaration_id": "TauLib.BookI.Holomorphy.H6DiagonalDiscipline::h6_section6_synthesis",
  "declaration_slug": "h6-section6-synthesis",
  "kind": "theorem",
  "name": "h6_section6_synthesis",
  "module_name": "TauLib.BookI.Holomorphy.H6DiagonalDiscipline",
  "module_url": "/verify/taulib/docs/book-i-holomorphy-h6-diagonal-discipline/",
  "source_line_start": 220,
  "source_line_end": 233,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/H6DiagonalDiscipline.lean#L220-L233",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Holomorphy.H6DiagonalDiscipline",
        "url": "/verify/taulib/docs/book-i-holomorphy-h6-diagonal-discipline/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/H6DiagonalDiscipline.lean#L220-L233",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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

- Module: [TauLib.BookI.Holomorphy.H6DiagonalDiscipline](/verify/taulib/docs/book-i-holomorphy-h6-diagonal-discipline/)
- Source path: [`TauLib/BookI/Holomorphy/H6DiagonalDiscipline.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/H6DiagonalDiscipline.lean#L220-L233)
- Source range: L220-L233
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Paper §6 synthesis theorem — H6 Diagonal Discipline closure
    (the Wave-27 keystone)**.

    Packages the four-clause structural significance of paper
    §6's diagonal discipline:

    1. **Sector-orthogonality witness**: `e_+ · e_- = 0` in the
       boundary algebra `D` (concrete witness from
       `dd_orthogonal_idempotent_pair_witness`).

    2. **Split-complex signature**: `j² = +1` holds (Wave 25's
       `j_squared_eq_one`), which is what (I2) of the paper's
       three-inversions theorem asserts.

    3. **Elliptic exclusion**: `(1+i)(1-i) = ⟨2, 0⟩ ≠ 0` in
       `GaussianElliptic` (Wave 25), so the elliptic alternative
       `i² = -1` is excluded by exactly the sector-orthogonality
       requirement that the diagonal discipline protects.

    4. **Split-complex contrast**: `(1+j)(1-j) = ⟨0, 0⟩` in
       SplitComplex (Wave 25), so the split-complex signature
       `j² = +1` IS exactly compatible with the σ-equivariant
       idempotent pair that DD1–DD4 demand.

    Together these four facts witness the paper's
    `thm:diagonal-discipline` + `thm:three-inversions`
    equivalence at the structural-content level — the role of
    Wave 27 in the H6 closure programme. -/
```

## Source Excerpt

```lean
theorem h6_section6_synthesis :
    -- Clause 1: Sector orthogonality (the protected structure)
    SectorPair.mul e_plus_sector e_minus_sector = ⟨0, 0⟩ ∧
    -- Clause 2: Split-complex signature j² = +1 (the I2 inversion)
    (SplitComplex.mul SplitComplex.j_canonical SplitComplex.j_canonical
       = SplitComplex.one) ∧
    -- Clause 3: Elliptic exclusion (i² = -1 is structurally precluded)
    (GaussianElliptic.mul ⟨1, 1⟩ ⟨1, -1⟩ ≠ GaussianElliptic.zero) ∧
    -- Clause 4: Split-complex contrast (j² = +1 admits orthogonality)
    (SplitComplex.mul ⟨1, 1⟩ ⟨1, -1⟩ = SplitComplex.zero) :=
  ⟨dd_orthogonal_idempotent_pair_witness,
   j_squared_eq_one,
   elliptic_no_sigma_equivariant_idempotent_pair,
   split_complex_admits_orthogonal_pair⟩
```
