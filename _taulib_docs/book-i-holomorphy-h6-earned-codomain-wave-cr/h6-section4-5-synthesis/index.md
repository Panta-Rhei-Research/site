---
{
  "projection_kind": "taulib_declaration",
  "title": "h6_section4_5_synthesis",
  "permalink": "/verify/taulib/docs/book-i-holomorphy-h6-earned-codomain-wave-cr/h6-section4-5-synthesis/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Holomorphy.H6EarnedCodomainWaveCR`.",
  "declaration_id": "TauLib.BookI.Holomorphy.H6EarnedCodomainWaveCR::h6_section4_5_synthesis",
  "declaration_slug": "h6-section4-5-synthesis",
  "kind": "theorem",
  "name": "h6_section4_5_synthesis",
  "module_name": "TauLib.BookI.Holomorphy.H6EarnedCodomainWaveCR",
  "module_url": "/verify/taulib/docs/book-i-holomorphy-h6-earned-codomain-wave-cr/",
  "source_line_start": 286,
  "source_line_end": 303,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/H6EarnedCodomainWaveCR.lean#L286-L303",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Holomorphy.H6EarnedCodomainWaveCR",
        "url": "/verify/taulib/docs/book-i-holomorphy-h6-earned-codomain-wave-cr/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/H6EarnedCodomainWaveCR.lean#L286-L303",
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

- Module: [TauLib.BookI.Holomorphy.H6EarnedCodomainWaveCR](/verify/taulib/docs/book-i-holomorphy-h6-earned-codomain-wave-cr/)
- Source path: [`TauLib/BookI/Holomorphy/H6EarnedCodomainWaveCR.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/H6EarnedCodomainWaveCR.lean#L286-L303)
- Source range: L286-L303
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Wave 28 H6 §4+§5 synthesis theorem (the keystone)**.

    Packages the structural punchline of paper §§4+5: the
    earned scalar codomain `D = R'[j]/(j²-1)` is uniquely
    forced by (CC1)–(CC4), and exactly because `j² = +1`,
    τ-holomorphic functions into `D` satisfy the wave equation
    rather than Laplace.

    Four clauses:

    1. **§4 uniqueness**: split-complex `j² = +1` is the unique
       structural choice (Wave 25 uniqueness witness).
    2. **§4 (CC4) concrete**: `(e_+, e_-)` is σ-equivariant
       orthogonal idempotent pair (Wave 27 + Wave 25).
    3. **§5 keystone**: wave equation `∂_t² u = ∂_x² u` follows
       from split-complex CR system + commutativity.
    4. **§5 v-component symmetry**: same wave equation for `v`. -/
```

## Source Excerpt

```lean
theorem h6_section4_5_synthesis {α : Type*}
    (dt dx : (α → Int) → (α → Int))
    (commute : ∀ f, dt (dx f) = dx (dt f))
    (u v : α → Int)
    (cr : split_cr_system dt dx u v) :
    -- Clause 1: j² = +1 (Wave 25 + §4 structural witness)
    SplitComplex.mul SplitComplex.j_canonical SplitComplex.j_canonical
      = SplitComplex.one ∧
    -- Clause 2: (CC4) concrete: orthogonal σ-equivariant idempotents
    SectorPair.mul e_plus_sector e_minus_sector = ⟨0, 0⟩ ∧
    -- Clause 3: wave equation for u
    dt (dt u) = dx (dx u) ∧
    -- Clause 4: wave equation for v
    dt (dt v) = dx (dx v) :=
  ⟨j_squared_eq_one,
   dd_orthogonal_idempotent_pair_witness,
   wave_equation_from_split_cr dt dx commute u v cr,
   wave_equation_from_split_cr_v dt dx commute u v cr⟩
```
