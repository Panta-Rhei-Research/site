---
{
  "projection_kind": "taulib_declaration",
  "title": "cc_axioms_concrete_witness",
  "permalink": "/verify/taulib/docs/book-i-holomorphy-h6-earned-codomain-wave-cr/cc-axioms-concrete-witness/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Holomorphy.H6EarnedCodomainWaveCR`.",
  "declaration_id": "TauLib.BookI.Holomorphy.H6EarnedCodomainWaveCR::cc_axioms_concrete_witness",
  "declaration_slug": "cc-axioms-concrete-witness",
  "kind": "theorem",
  "name": "cc_axioms_concrete_witness",
  "module_name": "TauLib.BookI.Holomorphy.H6EarnedCodomainWaveCR",
  "module_url": "/verify/taulib/docs/book-i-holomorphy-h6-earned-codomain-wave-cr/",
  "source_line_start": 135,
  "source_line_end": 150,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/H6EarnedCodomainWaveCR.lean#L135-L150",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/H6EarnedCodomainWaveCR.lean#L135-L150",
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
- Source path: [`TauLib/BookI/Holomorphy/H6EarnedCodomainWaveCR.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/H6EarnedCodomainWaveCR.lean#L135-L150)
- Source range: L135-L150
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Paper §4 axioms (CC1)–(CC4) — concrete witness in
    SplitComplex**: the boundary algebra `D = R'[j]/(j²-1)` with
    its canonical involution `σ_D : ⟨a, b⟩ ↦ ⟨a, -b⟩` satisfies
    all four compatibility axioms.

    Concretely we verify the structural-content clauses:

    - (CC2) `σ_D ∘ σ_D = id` on the j-element
    - (CC4) idempotent pair `(e_+, e_-)` with
      `e_+ + e_- = 1` and `e_+ · e_- = 0` and `σ(e_+) = e_-`.

    (CC1) base ring + (CC3) stable tail are encoded by the
    `SplitComplex` structure type itself + the existing
    `diagonal_free_protection` framework, so they're
    structurally implicit. -/
```

## Source Excerpt

```lean
theorem cc_axioms_concrete_witness :
    -- (CC2.a) involution squares to identity on j
    boundarySigma (boundarySigma SplitComplex.j_canonical)
      = SplitComplex.j_canonical ∧
    -- (CC4.a) idempotent sum: e_+ + e_- = 1
    SectorPair.add e_plus_sector e_minus_sector = ⟨1, 1⟩ ∧
    -- (CC4.b) orthogonality: e_+ · e_- = 0
    SectorPair.mul e_plus_sector e_minus_sector = ⟨0, 0⟩ ∧
    -- (CC4.c) involution swap: σ(e_+) = e_-
    sectorSigma e_plus_sector = e_minus_sector := by
  refine ⟨?_, ?_, ?_, ?_⟩
  · show ((⟨0, -(-1)⟩ : SplitComplex)) = ⟨0, 1⟩
    simp
  · rfl
  · rfl
  · rfl
```
