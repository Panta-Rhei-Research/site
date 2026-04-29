---
{
  "projection_kind": "taulib_declaration",
  "title": "kernel_hinge",
  "permalink": "/verify/taulib/docs/book-iii-spectrum-kernel-hinge/kernel-hinge-l88/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Spectrum.KernelHinge`.",
  "declaration_id": "TauLib.BookIII.Spectrum.KernelHinge::kernel_hinge",
  "declaration_slug": "kernel-hinge-l88",
  "kind": "def",
  "name": "kernel_hinge",
  "module_name": "TauLib.BookIII.Spectrum.KernelHinge",
  "module_url": "/verify/taulib/docs/book-iii-spectrum-kernel-hinge/",
  "source_line_start": 88,
  "source_line_end": 94,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectrum/KernelHinge.lean#L88-L94",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Spectrum.KernelHinge",
        "url": "/verify/taulib/docs/book-iii-spectrum-kernel-hinge/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectrum/KernelHinge.lean#L88-L94",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
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

- Module: [TauLib.BookIII.Spectrum.KernelHinge](/verify/taulib/docs/book-iii-spectrum-kernel-hinge/)
- Source path: [`TauLib/BookIII/Spectrum/KernelHinge.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectrum/KernelHinge.lean#L88-L94)
- Source range: L88-L94
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The canonical kernel hinge diagram, instantiated from earned structures. -/
```

## Source Excerpt

```lean
def kernel_hinge : KernelHinge where
  generators_count := 5
  generators_are_five := rfl
  earned_category := cat_tau
  earned_topos := earned_topos
  identity_theorem := tau_identity_nat
  four_valued_classifier := omega_tau_classifier
```
