---
{
  "projection_kind": "taulib_declaration",
  "title": "book_i_admissibility",
  "permalink": "/verify/taulib/docs/book-iii-spectrum-kernel-hinge/book-i-admissibility/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Spectrum.KernelHinge`.",
  "declaration_id": "TauLib.BookIII.Spectrum.KernelHinge::book_i_admissibility",
  "declaration_slug": "book-i-admissibility",
  "kind": "theorem",
  "name": "book_i_admissibility",
  "module_name": "TauLib.BookIII.Spectrum.KernelHinge",
  "module_url": "/verify/taulib/docs/book-iii-spectrum-kernel-hinge/",
  "source_line_start": 160,
  "source_line_end": 173,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectrum/KernelHinge.lean#L160-L173",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectrum/KernelHinge.lean#L160-L173",
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

- Module: [TauLib.BookIII.Spectrum.KernelHinge](/verify/taulib/docs/book-iii-spectrum-kernel-hinge/)
- Source path: [`TauLib/BookIII/Spectrum/KernelHinge.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectrum/KernelHinge.lean#L160-L173)
- Source range: L160-L173
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Tower coherence implies admissibility (I.T33 + I.P30). -/
```

## Source Excerpt

```lean
theorem book_i_admissibility :
    TauAdmissible chi_plus_stage ∧
    TauAdmissible chi_minus_stage ∧
    TauAdmissible id_stage :=
  ⟨chi_plus_admissible, chi_minus_admissible, id_admissible⟩

-- ============================================================
-- SMOKE TESTS
-- ============================================================

-- Kernel hinge instantiation
#check kernel_hinge
#check book_ii_bridge
#check book_ii_bridge_complete
```
