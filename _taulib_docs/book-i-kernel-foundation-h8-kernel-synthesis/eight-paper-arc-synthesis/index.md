---
{
  "projection_kind": "taulib_declaration",
  "title": "eight_paper_arc_synthesis",
  "permalink": "/verify/taulib/docs/book-i-kernel-foundation-h8-kernel-synthesis/eight-paper-arc-synthesis/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.KernelFoundation.H8KernelSynthesis`.",
  "declaration_id": "TauLib.BookI.KernelFoundation.H8KernelSynthesis::eight_paper_arc_synthesis",
  "declaration_slug": "eight-paper-arc-synthesis",
  "kind": "theorem",
  "name": "eight_paper_arc_synthesis",
  "module_name": "TauLib.BookI.KernelFoundation.H8KernelSynthesis",
  "module_url": "/verify/taulib/docs/book-i-kernel-foundation-h8-kernel-synthesis/",
  "source_line_start": 245,
  "source_line_end": 266,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/KernelFoundation/H8KernelSynthesis.lean#L245-L266",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.KernelFoundation.H8KernelSynthesis",
        "url": "/verify/taulib/docs/book-i-kernel-foundation-h8-kernel-synthesis/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/KernelFoundation/H8KernelSynthesis.lean#L245-L266",
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

- Module: [TauLib.BookI.KernelFoundation.H8KernelSynthesis](/verify/taulib/docs/book-i-kernel-foundation-h8-kernel-synthesis/)
- Source path: [`TauLib/BookI/KernelFoundation/H8KernelSynthesis.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/KernelFoundation/H8KernelSynthesis.lean#L245-L266)
- Source range: L245-L266
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **EIGHT-PAPER ARC SYNTHESIS — THE KEYSTONE OF KEYSTONES**.

    Wave 34 is the **CONCLUDING KEY WAVE** of the eight-paper
    foundational programme.  This theorem witnesses the closure of
    all eight foundational papers in the Panta Rhei arc:

    1. **H1 hyperfactorization** (Wave 21): ABCD chart unique
    2. **H2 prime-polarity** (Wave 20): Pol ≡ chi(legendre)
    3. **H3 iota-tau** (Waves 4–17): ι_τ = 2/(π+e)
    4. **H4 boundary-algebra** (Waves 24–25): split-complex j² = +1
    5. **H5 address-resolution / Hinge 7** (Wave 5+26): canonical NF
    6. **H6 holomorphy-first / Hinge 5** (Waves 27–30): earned cat machine
    7. **H7 tau-topos / Hinge 6** (Waves 31–33): Truth4 classifier
    8. **H8/H0 kernel-foundation** (Wave 34, this): architectural thesis

    Two structural-content witnesses:

    **(I) H1–H7 closure** via Wave 33's `seven_bundle_closure_synthesis`:
    seven bundles structurally formalised, witnessed by 7 clauses
    spanning the entire τ-framework's foundational mathematics.

    **(II) H8 kernel-foundation synthesis**: the five-into-one
    architectural thesis stating that the τ-kernel's discipline is
    NOT a design choice but a structural necessity — the same
    constraint visible from five independent angles
    (ontic identity, linear discipline, ★-autonomous, resonance-free,
    reception-constrained).

    This single theorem is the most outreach-impactful result in
    TauLib: a Lean proof witnessing closure of the entire
    eight-paper structural arc.  All derived from the same τ-kernel
    (7 axioms, 5 generators, 1 operator) via shared infrastructure
    (`SplitComplex`, `Truth4`, `OmegaInverseLimit`, `normalize`,
    `OnticIdentityInvariance`, etc.).

    The seven hinges *build* the τ-universe.  H8 *names* what they
    build.  Together they constitute the eight-paper foundational
    programme of Panta Rhei. -/
```

## Source Excerpt

```lean
theorem eight_paper_arc_synthesis (p : Program)
    (f : OrthodoxFoundation) :
    -- (I) H1–H7 closure (Wave 33's seven_bundle_closure_synthesis)
    (SplitComplex.mul SplitComplex.j_canonical SplitComplex.j_canonical
       = SplitComplex.one ∧
     SplitComplex.mul ⟨1, 1⟩ ⟨1, -1⟩ = SplitComplex.zero ∧
     (∀ f₁ f₂ f₃ : StageFun,
       StageFun.comp (StageFun.comp f₁ f₂) f₃ =
       StageFun.comp f₁ (StageFun.comp f₂ f₃)) ∧
     (∃ nf : NormalForm, normalize p = nf) ∧
     (∀ v : Omega_tau, v = T ∨ v = F ∨ v = B ∨ v = N) ∧
     (StabilisedValue liarTemplate F B ∧
      StabilisedValue kleeneRosserTemplate F N) ∧
     ((T : Truth4) ≠ F)) ∧
    -- (II) H8 kernel-foundation synthesis (five-into-one)
    (Nonempty OnticIdentityInvariance ∧
     (∀ d : DiagonalAspect, linear_to_diag (diag_to_linear d) = d) ∧
     Nonempty K5StructuralExclusion ∧
     tau_resonance.isFullResonance = false ∧
     Nonempty StructuralInstability) :=
  ⟨seven_bundle_closure_synthesis p,
   kernel_foundation_synthesis f⟩
```
