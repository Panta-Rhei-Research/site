---
{
  "projection_kind": "taulib_declaration",
  "title": "seven_bundle_closure_synthesis",
  "permalink": "/verify/taulib/docs/book-i-topos-h7-classical-closure/seven-bundle-closure-synthesis/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Topos.H7ClassicalClosure`.",
  "declaration_id": "TauLib.BookI.Topos.H7ClassicalClosure::seven_bundle_closure_synthesis",
  "declaration_slug": "seven-bundle-closure-synthesis",
  "kind": "theorem",
  "name": "seven_bundle_closure_synthesis",
  "module_name": "TauLib.BookI.Topos.H7ClassicalClosure",
  "module_url": "/verify/taulib/docs/book-i-topos-h7-classical-closure/",
  "source_line_start": 268,
  "source_line_end": 295,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/H7ClassicalClosure.lean#L268-L295",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Topos.H7ClassicalClosure",
        "url": "/verify/taulib/docs/book-i-topos-h7-classical-closure/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/H7ClassicalClosure.lean#L268-L295",
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

- Module: [TauLib.BookI.Topos.H7ClassicalClosure](/verify/taulib/docs/book-i-topos-h7-classical-closure/)
- Source path: [`TauLib/BookI/Topos/H7ClassicalClosure.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/H7ClassicalClosure.lean#L268-L295)
- Source range: L268-L295
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **SEVEN-BUNDLE CLOSURE SYNTHESIS — THE KEYSTONE OF KEYSTONES**.

    Wave 33 is the FINAL wave of the H6+H7 closure programme.
    This theorem witnesses the closure of all seven hinge-paper
    bundles in the Panta Rhei foundational arc:

    1. **H1 hyperfactorization** (Wave 21): ABCD chart unique
    2. **H2 prime-polarity** (Wave 18+19a+20): Pol ≡ chi(legendre)
    3. **H3 iota-tau** (Waves 4-17): ι_τ = 2/(π+e) ≈ 0.341304
    4. **H4 boundary-algebra** (Wave 24+25): split-complex j² = +1 unique
    5. **H5 address-resolution / Hinge 7** (Wave 5+26): canonical NF
    6. **H6 holomorphy-first / Hinge 5** (Wave 27-30): earned cat machine
    7. **H7 tau-topos / Hinge 6** (Wave 31-33, THIS WAVE): Truth4 classifier

    All seven bundles structurally formalised end-to-end in TauLib
    at the paper-section level, derived from the same τ-kernel
    (7 axioms, 5 generators, 1 operator).

    Seven structural-content clauses (one per bundle):

    1. **H4 split-complex** (j² = +1)
    2. **H4 elliptic exclusion** ((1+j)(1-j) = 0 vs (1+i)(1-i) ≠ 0)
    3. **H6 earned associativity** (∀ f₁ f₂ f₃, (f₁∘f₂)∘f₃ = f₁∘(f₂∘f₃))
    4. **H5/H6 canonical NF** (Wave 26 + Wave 30 pre-Yoneda)
    5. **H7 subobject classifier** (Truth4 = {T, F, B, N})
    6. **H7 four-sector classification** (Liar B + KR N witnesses)
    7. **H7 classical embedding** (T ≠ F + non-classical extras)

    This theorem is the most outreach-impactful in TauLib: a
    SINGLE Lean proof witnessing that the entire τ-framework's
    seven foundational papers are structurally formalised at the
    paper-section level. -/
```

## Source Excerpt

```lean
theorem seven_bundle_closure_synthesis (p : Program) :
    -- Bundle H4 clause 1: split-complex j² = +1
    SplitComplex.mul SplitComplex.j_canonical SplitComplex.j_canonical
      = SplitComplex.one ∧
    -- Bundle H4 clause 2: elliptic exclusion (split-complex orthogonality)
    SplitComplex.mul ⟨1, 1⟩ ⟨1, -1⟩ = SplitComplex.zero ∧
    -- Bundle H6 clause: earned associativity (StageFun level)
    (∀ f₁ f₂ f₃ : StageFun,
      StageFun.comp (StageFun.comp f₁ f₂) f₃ =
      StageFun.comp f₁ (StageFun.comp f₂ f₃)) ∧
    -- Bundle H5/H6 clause: canonical NF address (Wave 26)
    (∃ nf : NormalForm, normalize p = nf) ∧
    -- Bundle H7 clause 1: subobject classifier four-valued
    (∀ v : Omega_tau, v = T ∨ v = F ∨ v = B ∨ v = N) ∧
    -- Bundle H7 clause 2: four-sector classification (Liar B + KR N)
    (StabilisedValue liarTemplate F B ∧
     StabilisedValue kleeneRosserTemplate F N) ∧
    -- Bundle H7 clause 3: classical embedding
    ((T : Truth4) ≠ F) :=
  ⟨j_squared_eq_one,
   split_complex_admits_orthogonal_pair,
   stagefun_comp_assoc,
   ⟨normalize p, rfl⟩,
   subobject_classifier_witness,
   ⟨liar_stabilises_at_Both, kleene_rosser_stabilises_at_N F⟩,
   classical_topos_subquotient_witness⟩

end Tau.Topos
```
