---
{
  "projection_kind": "taulib_declaration",
  "title": "precision_sprint6d_status",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/precision-sprint6d-status/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::precision_sprint6d_status",
  "declaration_slug": "precision-sprint6d-status",
  "kind": "def",
  "name": "precision_sprint6d_status",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 1590,
  "source_line_end": 1593,
  "registry_ids": [
    "IV.R410"
  ],
  "related_registry_items": [
    {
      "id": "IV.R410",
      "title": "m_μ NNLO + p-n NLO Precision Status after Sprint 6D",
      "url": "/registry/object/IV.R410/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1590-L1593",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Particles.ThreeGenerations",
        "url": "/verify/taulib/docs/book-iv-particles-three-generations/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1590-L1593",
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

- Module: [TauLib.BookIV.Particles.ThreeGenerations](/verify/taulib/docs/book-iv-particles-three-generations/)
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1590-L1593)
- Source range: L1590-L1593
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `IV.R410` — m_μ NNLO + p-n NLO Precision Status after Sprint 6D

## Immediate Comment / Docstring

```lean
-- [IV.R410] Precision status after Sprint 6D
```

## Source Excerpt

```lean
def precision_sprint6d_status : String :=
  "Sprint 6D: m_μ/m_e at +43 ppm (k=23/3, τ-eff); best k=7.5 at -8.2 ppm. " ++
  "p-n: C.3 NLO at +5 ppm (τ-eff best); C.5 at +28 ppm (τ-eff). " ++
  "23=W₃(4)+W₃(3)+1 Window-algebra; 3/20=N_c/(4·W₃(4)) Window-nucleon."
```
