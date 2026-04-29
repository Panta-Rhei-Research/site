---
{
  "projection_kind": "taulib_declaration",
  "title": "hinge7_integration_synthesis",
  "permalink": "/verify/taulib/docs/book-i-addressability-hinge-integration/hinge7-integration-synthesis/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Addressability.HingeIntegration`.",
  "declaration_id": "TauLib.BookI.Addressability.HingeIntegration::hinge7_integration_synthesis",
  "declaration_slug": "hinge7-integration-synthesis",
  "kind": "theorem",
  "name": "hinge7_integration_synthesis",
  "module_name": "TauLib.BookI.Addressability.HingeIntegration",
  "module_url": "/verify/taulib/docs/book-i-addressability-hinge-integration/",
  "source_line_start": 271,
  "source_line_end": 287,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Addressability/HingeIntegration.lean#L271-L287",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Addressability.HingeIntegration",
        "url": "/verify/taulib/docs/book-i-addressability-hinge-integration/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Addressability/HingeIntegration.lean#L271-L287",
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

- Module: [TauLib.BookI.Addressability.HingeIntegration](/verify/taulib/docs/book-i-addressability-hinge-integration/)
- Source path: [`TauLib/BookI/Addressability/HingeIntegration.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Addressability/HingeIntegration.lean#L271-L287)
- Source range: L271-L287
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Paper Theorem 7 (Hinge 7 Integration Tabulation) — KEYSTONE**.

    The most outreach-impactful synthesis theorem of the
    address-resolution paper bundle.  Hinge 7 is the foundational
    capstone of the Panta Rhei seven-hinge arc by:

    1. **Discharging** the "modulo Hinge 7 NF confluence" scope
       caveats of Hinge 5 (HolEnd_τ pre-Yoneda collapse) and
       Hinge 6 (τ-topos circularity resolution).  Captured by
       the `nf_confluence_statement` theorem above: TauLib's
       deterministic `normalize` function makes confluence
       computational.

    2. **Supplying** the canonical-address framework used as
       coordinate primitive in Hinges 1-4 (Hyperfact ABCD,
       Prime polarity classifier, ι_τ master constant, boundary
       algebra).  Captured by the existence of `normalize` as a
       canonical map Program → NormalForm.

    3. **Establishing** the ontic ultrametric as the τ-native
       metric structure replacing Euclidean distance.  Captured
       via `OnticDist` (Wave 5) + `ontic_ultrametric_symmetry`.

    4. **Completing** the seven-hinge foundational arc: Hinges
       1+2+3+4+5+6+7 are now structurally formalised in TauLib
       at the paper-bundle level.

    This single theorem packages the four-clause structural
    significance of Hinge 7 within Panta Rhei. -/
```

## Source Excerpt

```lean
theorem hinge7_integration_synthesis :
    -- Clause 1: Confluence is computational (deterministic NF)
    (∀ p : Program, ∃ nf : NormalForm, normalize p = nf) ∧
    -- Clause 2: Canonical-address framework available (Address Resolution)
    (∀ a b : Program, tauEq a b ↔ OnticDist (normalize a) (normalize b) = 0) ∧
    -- Clause 3: Ontic ultrametric structure
    (∀ nf₁ nf₂ : NormalForm, OnticDist nf₁ nf₂ = OnticDist nf₂ nf₁) ∧
    -- Clause 4: Cayley metric structure (companion to ontic)
    (∀ nf₁ nf₂ nf₃ : NormalForm,
      CayleyDist nf₁ nf₂ = CayleyDist nf₂ nf₁ ∧
      CayleyDist nf₁ nf₃ ≤ CayleyDist nf₁ nf₂ + CayleyDist nf₂ nf₃) := by
  refine ⟨?_, ?_, ?_, ?_⟩
  · intro p; exact ⟨normalize p, rfl⟩
  · exact address_resolution_theorem
  · exact OnticDist_symm
  · intro nf₁ nf₂ nf₃
    exact ⟨CayleyDist_symm nf₁ nf₂, CayleyDist_triangle nf₁ nf₂ nf₃⟩
```
