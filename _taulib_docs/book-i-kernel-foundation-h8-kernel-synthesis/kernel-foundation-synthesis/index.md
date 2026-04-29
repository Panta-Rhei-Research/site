---
{
  "projection_kind": "taulib_declaration",
  "title": "kernel_foundation_synthesis",
  "permalink": "/verify/taulib/docs/book-i-kernel-foundation-h8-kernel-synthesis/kernel-foundation-synthesis/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.KernelFoundation.H8KernelSynthesis`.",
  "declaration_id": "TauLib.BookI.KernelFoundation.H8KernelSynthesis::kernel_foundation_synthesis",
  "declaration_slug": "kernel-foundation-synthesis",
  "kind": "theorem",
  "name": "kernel_foundation_synthesis",
  "module_name": "TauLib.BookI.KernelFoundation.H8KernelSynthesis",
  "module_url": "/verify/taulib/docs/book-i-kernel-foundation-h8-kernel-synthesis/",
  "source_line_start": 186,
  "source_line_end": 201,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/KernelFoundation/H8KernelSynthesis.lean#L186-L201",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/KernelFoundation/H8KernelSynthesis.lean#L186-L201",
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
- Source path: [`TauLib/BookI/KernelFoundation/H8KernelSynthesis.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/KernelFoundation/H8KernelSynthesis.lean#L186-L201)
- Source range: L186-L201
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Wave 34 H8 Kernel-Foundation Synthesis (KEYSTONE)**.

    Packages the five-into-one thesis of paper §8: τ-kernel is
    simultaneously
    (1) ontically identified,
    (2) linearly disciplined,
    (3) ★-autonomous,
    (4) resonance-free, and
    (5) host-reception constrained
    — five facets of a single design choice.

    Note: `OnticIdentityInvariance`, `K5StructuralExclusion`, and
    `StructuralInstability` are data-structures (Type), so we wrap
    them with `Nonempty` to land in Prop. -/
```

## Source Excerpt

```lean
theorem kernel_foundation_synthesis (f : OrthodoxFoundation) :
    -- Clause 1: Ontic identity invariance (I.T46)
    Nonempty OnticIdentityInvariance ∧
    -- Clause 2: Diagonal-Linear Correspondence round-trip (I.T37)
    (∀ d : DiagonalAspect, linear_to_diag (diag_to_linear d) = d) ∧
    -- Clause 3: K5 structural exclusion (I.T39)
    Nonempty K5StructuralExclusion ∧
    -- Clause 4: Diagonal resonance diagnosis — τ blocks LEP (I.T47)
    tau_resonance.isFullResonance = false ∧
    -- Clause 5: Reception instability for orthodox foundations (I.T48)
    Nonempty StructuralInstability :=
  ⟨⟨h8_ontic_identity_invariance_witness⟩,
   h8_diagonal_linear_correspondence_witness,
   ⟨h8_k5_structural_exclusion_witness⟩,
   h8_diagonal_resonance_diagnosis_witness,
   ⟨h8_reception_instability_witness f⟩⟩
```
