---
{
  "projection_kind": "taulib_declaration",
  "title": "MuonNNLOK23",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/muon-nnlok23/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::MuonNNLOK23",
  "declaration_slug": "muon-nnlok23",
  "kind": "structure",
  "name": "MuonNNLOK23",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 1547,
  "source_line_end": 1556,
  "registry_ids": [
    "IV.D360"
  ],
  "related_registry_items": [
    {
      "id": "IV.D360",
      "title": "m_μ/m_e NNLO k=23/3: W₃(4)+W₃(3)+1 Window-Algebra Exponent",
      "url": "/registry/object/IV.D360/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1547-L1556",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1547-L1556",
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

- Module: [TauLib.BookIV.Particles.ThreeGenerations](/verify/taulib/docs/book-iv-particles-three-generations/)
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1547-L1556)
- Source range: L1547-L1556
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D360` — m_μ/m_e NNLO k=23/3: W₃(4)+W₃(3)+1 Window-Algebra Exponent

## Immediate Comment / Docstring

```lean
/-- [IV.D360] NNLO k=23/3 correction structure (formalized). -/
```

## Source Excerpt

```lean
structure MuonNNLOK23 where
  /-- Numerator of k: 23. -/
  k_numer : Nat := 23
  /-- Denominator of k: 3. -/
  k_denom : Nat := 3
  /-- Deviation from PDG in ppm. -/
  deviation_ppm : Nat := 43
  /-- Window algebra terms: W₃(4)+W₃(3)+1 = 5+17+1 = 23. -/
  n_window_terms : Nat := 3
  deriving Repr
```
