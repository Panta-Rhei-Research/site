---
{
  "projection_kind": "taulib_declaration",
  "title": "earned_codomain_structural_witness",
  "permalink": "/verify/taulib/docs/book-i-holomorphy-h6-earned-codomain-wave-cr/earned-codomain-structural-witness/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Holomorphy.H6EarnedCodomainWaveCR`.",
  "declaration_id": "TauLib.BookI.Holomorphy.H6EarnedCodomainWaveCR::earned_codomain_structural_witness",
  "declaration_slug": "earned-codomain-structural-witness",
  "kind": "theorem",
  "name": "earned_codomain_structural_witness",
  "module_name": "TauLib.BookI.Holomorphy.H6EarnedCodomainWaveCR",
  "module_url": "/verify/taulib/docs/book-i-holomorphy-h6-earned-codomain-wave-cr/",
  "source_line_start": 166,
  "source_line_end": 172,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/H6EarnedCodomainWaveCR.lean#L166-L172",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/H6EarnedCodomainWaveCR.lean#L166-L172",
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
- Source path: [`TauLib/BookI/Holomorphy/H6EarnedCodomainWaveCR.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/H6EarnedCodomainWaveCR.lean#L166-L172)
- Source range: L166-L172
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Paper §4 Theorem `earned-codomain` — structural-witness form**.

    Among all pairs `(S, σ_S)` satisfying (CC1)–(CC4), the unique
    solution (up to canonical isomorphism) is the split-complex
    boundary algebra `D = R'[j]/(j²-1)`.

    The uniqueness theorem reduces to Wave 25's structural witness:
    any boundary-algebra datum satisfying C1-C4 (which is exactly
    what (CC1)+(CC2)+(CC4) of §4 demand at the algebraic level)
    is canonically isomorphic to `D` via `j := e_+ - e_-`,
    satisfying `j² = +1` and `σ(j) = -j`.

    Companion `cc_axioms_concrete_witness` verifies (CC2.a),
    (CC4.a)–(CC4.c) on the canonical `SplitComplex` model. -/
```

## Source Excerpt

```lean
theorem earned_codomain_structural_witness :
    -- Wave 25 uniqueness witness: j² = 1 ∧ σ(j) = -j
    SplitComplex.mul SplitComplex.j_canonical SplitComplex.j_canonical
      = SplitComplex.one ∧
    boundarySigma SplitComplex.j_canonical
      = SplitComplex.neg SplitComplex.j_canonical :=
  uniqueness_canonical_isomorphism_witness
```
