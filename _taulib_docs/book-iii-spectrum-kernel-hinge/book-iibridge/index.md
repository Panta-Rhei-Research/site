---
{
  "projection_kind": "taulib_declaration",
  "title": "BookIIBridge",
  "permalink": "/verify/taulib/docs/book-iii-spectrum-kernel-hinge/book-iibridge/",
  "summary_short": "`structure` declaration in `TauLib.BookIII.Spectrum.KernelHinge`.",
  "declaration_id": "TauLib.BookIII.Spectrum.KernelHinge::BookIIBridge",
  "declaration_slug": "book-iibridge",
  "kind": "structure",
  "name": "BookIIBridge",
  "module_name": "TauLib.BookIII.Spectrum.KernelHinge",
  "module_url": "/verify/taulib/docs/book-iii-spectrum-kernel-hinge/",
  "source_line_start": 111,
  "source_line_end": 119,
  "registry_ids": [
    "I.T34"
  ],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectrum/KernelHinge.lean#L111-L119",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectrum/KernelHinge.lean#L111-L119",
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

- Module: [TauLib.BookIII.Spectrum.KernelHinge](/verify/taulib/docs/book-iii-spectrum-kernel-hinge/)
- Source path: [`TauLib/BookIII/Spectrum/KernelHinge.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectrum/KernelHinge.lean#L111-L119)
- Source range: L111-L119
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [I.T34] The Book II bridge: ALL imports for Book II are earned.

    Book II needs:
    1. The earned category Cat_τ with composition and identity ✓
    2. The earned topos E_τ with Ω_τ classifier ✓
    3. The holomorphic function space Hol(L) ✓
    4. The Identity Theorem for uniqueness ✓
    5. The Global Hartogs Extension Theorem ✓
    6. The τ-Tower machine for computability arguments ✓

    We witness this by constructing the complete export structure. -/
```

## Source Excerpt

```lean
structure BookIIBridge where
  -- The Book I export (from BoundaryInterior)
  export_data : BookIExport
  -- The kernel hinge (witnessing earned status)
  hinge : KernelHinge
  -- The TTM for computability (from Part XVI)
  ttm_exists : TTM
  -- τ-admissibility (from Part XVI)
  admissibility : TauAdmissible chi_plus_stage
```
