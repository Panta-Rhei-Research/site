---
{
  "projection_kind": "taulib_declaration",
  "title": "five_bundle_closure_synthesis",
  "permalink": "/verify/taulib/docs/book-i-addressability-hinge-integration/five-bundle-closure-synthesis/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Addressability.HingeIntegration`.",
  "declaration_id": "TauLib.BookI.Addressability.HingeIntegration::five_bundle_closure_synthesis",
  "declaration_slug": "five-bundle-closure-synthesis",
  "kind": "theorem",
  "name": "five_bundle_closure_synthesis",
  "module_name": "TauLib.BookI.Addressability.HingeIntegration",
  "module_url": "/verify/taulib/docs/book-i-addressability-hinge-integration/",
  "source_line_start": 313,
  "source_line_end": 326,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Addressability/HingeIntegration.lean#L313-L326",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Addressability/HingeIntegration.lean#L313-L326",
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
- Source path: [`TauLib/BookI/Addressability/HingeIntegration.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Addressability/HingeIntegration.lean#L313-L326)
- Source range: L313-L326
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **The five-paper-bundle synthesis** — the structural picture
    after Wave 26 closes H5:

    1. **H1 hyperfactorization**: unique ABCD chart (Wave 21).
    2. **H2 prime-polarity**: Pol ≡ Label_∞ ≡ chi(legendre)
       (Waves 18 + 19a + 20).
    3. **H3 iota-tau**: ι_τ = 2/(π+e) ≈ 0.341304 (Waves 4 + 11 +
       12-17).
    4. **H4 boundary-algebra**: 4-atom dictionary + uniqueness
       + elliptic exclusion (Waves 24 + 25).
    5. **H5 address-resolution / Hinge 7**: canonical NF +
       deterministic normalize + ontic ultrametric (Wave 5 +
       this Wave 26).

    All five bundles structurally formalised in TauLib at the
    paper-section level, all derived from the same τ-kernel,
    with cross-references via shared infrastructure
    (SplitComplex, Truth4, OmegaInverseLimit, normalize, etc.).

    This wave records the synthesis at the registry level. -/
```

## Source Excerpt

```lean
theorem five_bundle_closure_synthesis (p q : Program)
    (nf₁ nf₂ : NormalForm) :
    -- H5 closure: Hinge 7 supplies the canonical-address primitive
    (tauEq p q ↔ OnticDist (normalize p) (normalize q) = 0) ∧
    -- H5 metric structure
    (CayleyDist nf₁ nf₂ = CayleyDist nf₂ nf₁) ∧
    -- H5 ultrametric structure
    (OnticDist nf₁ nf₂ = OnticDist nf₂ nf₁) := by
  refine ⟨?_, ?_, ?_⟩
  · exact address_resolution_theorem p q
  · exact CayleyDist_symm nf₁ nf₂
  · exact OnticDist_symm nf₁ nf₂

end Tau.Addressability
```
