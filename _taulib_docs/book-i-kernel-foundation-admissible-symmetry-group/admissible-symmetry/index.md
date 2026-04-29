---
{
  "projection_kind": "taulib_declaration",
  "title": "AdmissibleSymmetry",
  "permalink": "/verify/taulib/docs/book-i-kernel-foundation-admissible-symmetry-group/admissible-symmetry/",
  "summary_short": "`structure` declaration in `TauLib.BookI.KernelFoundation.AdmissibleSymmetryGroup`.",
  "declaration_id": "TauLib.BookI.KernelFoundation.AdmissibleSymmetryGroup::AdmissibleSymmetry",
  "declaration_slug": "admissible-symmetry",
  "kind": "structure",
  "name": "AdmissibleSymmetry",
  "module_name": "TauLib.BookI.KernelFoundation.AdmissibleSymmetryGroup",
  "module_url": "/verify/taulib/docs/book-i-kernel-foundation-admissible-symmetry-group/",
  "source_line_start": 105,
  "source_line_end": 110,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/KernelFoundation/AdmissibleSymmetryGroup.lean#L105-L110",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.KernelFoundation.AdmissibleSymmetryGroup",
        "url": "/verify/taulib/docs/book-i-kernel-foundation-admissible-symmetry-group/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/KernelFoundation/AdmissibleSymmetryGroup.lean#L105-L110",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
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

- Module: [TauLib.BookI.KernelFoundation.AdmissibleSymmetryGroup](/verify/taulib/docs/book-i-kernel-foundation-admissible-symmetry-group/)
- Source path: [`TauLib/BookI/KernelFoundation/AdmissibleSymmetryGroup.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/KernelFoundation/AdmissibleSymmetryGroup.lean#L105-L110)
- Source range: L105-L110
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Paper §6 admissible-symmetry definition (structural witness)**.

    An `AdmissibleSymmetry` is a τ-endo-functor on `Program`
    preserving the canonical normal form.  This is the
    NF-coherence projection of the paper's full
    "K0–K6-preserving τ-endo-functor" — the relevant operational
    content for Clause (iii) of the Ontic Identity Invariance
    theorem (I.T46). -/
```

## Source Excerpt

```lean
structure AdmissibleSymmetry where
  /-- The underlying map on Programs. -/
  apply : Program → Program
  /-- NF-preservation: the symmetry acts trivially on the
      canonical NF address (paper §6 NF coherence requirement). -/
  preserves_nf : ∀ p : Program, normalize (apply p) = normalize p
```
