---
{
  "projection_kind": "taulib_declaration",
  "title": "SpectrumSummary",
  "permalink": "/verify/taulib/docs/book-iv-particles-spectrum-complete/spectrum-summary/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.SpectrumComplete`.",
  "declaration_id": "TauLib.BookIV.Particles.SpectrumComplete::SpectrumSummary",
  "declaration_slug": "spectrum-summary",
  "kind": "structure",
  "name": "SpectrumSummary",
  "module_name": "TauLib.BookIV.Particles.SpectrumComplete",
  "module_url": "/verify/taulib/docs/book-iv-particles-spectrum-complete/",
  "source_line_start": 235,
  "source_line_end": 246,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/SpectrumComplete.lean#L235-L246",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Particles.SpectrumComplete",
        "url": "/verify/taulib/docs/book-iv-particles-spectrum-complete/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/SpectrumComplete.lean#L235-L246",
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

- Module: [TauLib.BookIV.Particles.SpectrumComplete](/verify/taulib/docs/book-iv-particles-spectrum-complete/)
- Source path: [`TauLib/BookIV/Particles/SpectrumComplete.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/SpectrumComplete.lean#L235-L246)
- Source range: L235-L246
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Summary of the complete particle spectrum:
    - All observed SM particles accounted for
    - No BSM particles predicted
    - Two inputs only (ι_τ, m_n)
    - Ontic/non-ontic line is mathematical -/
```

## Source Excerpt

```lean
structure SpectrumSummary where
  /-- All SM particles accounted for. -/
  sm_complete : Bool := true
  /-- No BSM predicted. -/
  no_bsm : Bool := true
  /-- Number of inputs. -/
  num_inputs : Nat := 2
  /-- Ontic entities in register. -/
  ontic_count : Nat := 15
  /-- Non-ontic entities identified. -/
  non_ontic_count : Nat := 5
  deriving Repr
```
