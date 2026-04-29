---
{
  "projection_kind": "taulib_declaration",
  "title": "omega_readout",
  "permalink": "/verify/taulib/docs/book-ii-interior-omega-readout/omega-readout/",
  "summary_short": "`def` declaration in `TauLib.BookII.Interior.OmegaReadout`.",
  "declaration_id": "TauLib.BookII.Interior.OmegaReadout::omega_readout",
  "declaration_slug": "omega-readout",
  "kind": "def",
  "name": "omega_readout",
  "module_name": "TauLib.BookII.Interior.OmegaReadout",
  "module_url": "/verify/taulib/docs/book-ii-interior-omega-readout/",
  "source_line_start": 63,
  "source_line_end": 65,
  "registry_ids": [
    "II.D04"
  ],
  "related_registry_items": [
    {
      "id": "II.D04",
      "title": "Omega Readout",
      "url": "/registry/object/II.D04/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Interior/OmegaReadout.lean#L63-L65",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Interior.OmegaReadout",
        "url": "/verify/taulib/docs/book-ii-interior-omega-readout/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Interior/OmegaReadout.lean#L63-L65",
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

- Module: [TauLib.BookII.Interior.OmegaReadout](/verify/taulib/docs/book-ii-interior-omega-readout/)
- Source path: [`TauLib/BookII/Interior/OmegaReadout.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Interior/OmegaReadout.lean#L63-L65)
- Source range: L63-L65
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D04` — Omega Readout

## Immediate Comment / Docstring

```lean
/-- [II.D04] Omega readout of an admissible point.
    Returns (base_A, base_D, fiber_dominance).
    At ω-limit: base → (Ω,Ω), fiber → lobe of ℒ. -/
```

## Source Excerpt

```lean
def omega_readout (p : TauAdmissiblePoint) :
    TauIdx × TauIdx × FiberDominance :=
  (p.a, p.d, p.fiber_dominance)
```
