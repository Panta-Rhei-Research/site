---
{
  "projection_kind": "taulib_declaration",
  "title": "example_coherence_horizon",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-tovphase-boundary/example-coherence-horizon/",
  "summary_short": "`def` declaration in `TauLib.BookV.GravityField.TOVPhaseBoundary`.",
  "declaration_id": "TauLib.BookV.GravityField.TOVPhaseBoundary::example_coherence_horizon",
  "declaration_slug": "example-coherence-horizon",
  "kind": "def",
  "name": "example_coherence_horizon",
  "module_name": "TauLib.BookV.GravityField.TOVPhaseBoundary",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-tovphase-boundary/",
  "source_line_start": 245,
  "source_line_end": 249,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TOVPhaseBoundary.lean#L245-L249",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.GravityField.TOVPhaseBoundary",
        "url": "/verify/taulib/docs/book-v-gravity-field-tovphase-boundary/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TOVPhaseBoundary.lean#L245-L249",
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

- Module: [TauLib.BookV.GravityField.TOVPhaseBoundary](/verify/taulib/docs/book-v-gravity-field-tovphase-boundary/)
- Source path: [`TauLib/BookV/GravityField/TOVPhaseBoundary.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TOVPhaseBoundary.lean#L245-L249)
- Source range: L245-L249
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Example coherence horizon at ~3 solar masses. -/
```

## Source Excerpt

```lean
def example_coherence_horizon : CoherenceHorizon where
  mass_numer := 30
  mass_denom := 10
  denom_pos := by omega
  mass_positive := by omega
```
