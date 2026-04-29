---
{
  "projection_kind": "taulib_declaration",
  "title": "h8_diagonal_resonance_diagnosis_witness",
  "permalink": "/verify/taulib/docs/book-i-kernel-foundation-h8-kernel-synthesis/h8-diagonal-resonance-diagnosis-witness/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.KernelFoundation.H8KernelSynthesis`.",
  "declaration_id": "TauLib.BookI.KernelFoundation.H8KernelSynthesis::h8_diagonal_resonance_diagnosis_witness",
  "declaration_slug": "h8-diagonal-resonance-diagnosis-witness",
  "kind": "theorem",
  "name": "h8_diagonal_resonance_diagnosis_witness",
  "module_name": "TauLib.BookI.KernelFoundation.H8KernelSynthesis",
  "module_url": "/verify/taulib/docs/book-i-kernel-foundation-h8-kernel-synthesis/",
  "source_line_start": 153,
  "source_line_end": 155,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/KernelFoundation/H8KernelSynthesis.lean#L153-L155",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/KernelFoundation/H8KernelSynthesis.lean#L153-L155",
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
- Source path: [`TauLib/BookI/KernelFoundation/H8KernelSynthesis.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/KernelFoundation/H8KernelSynthesis.lean#L153-L155)
- Source range: L153-L155
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Paper Theorem `main-resonance` (= I.T47)**: LEP splice is the
    universal obstruction; τ-kernel blocks all three components
    (L, E, P) independently.

    Concrete witness: τ-resonance profile is NOT full resonance
    (`tau_no_full_resonance`). -/
```

## Source Excerpt

```lean
theorem h8_diagonal_resonance_diagnosis_witness :
    tau_resonance.isFullResonance = false :=
  tau_no_full_resonance
```
