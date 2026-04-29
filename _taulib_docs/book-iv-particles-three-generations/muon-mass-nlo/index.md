---
{
  "projection_kind": "taulib_declaration",
  "title": "MuonMassNLO",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/muon-mass-nlo/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::MuonMassNLO",
  "declaration_slug": "muon-mass-nlo",
  "kind": "structure",
  "name": "MuonMassNLO",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 694,
  "source_line_end": 703,
  "registry_ids": [
    "IV.T148"
  ],
  "related_registry_items": [
    {
      "id": "IV.T148",
      "title": "m_μ/m_e Best NLO Formula: ι_τ⁻⁴·⁹⁶ at +307 ppm",
      "url": "/registry/object/IV.T148/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L694-L703",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L694-L703",
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
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L694-L703)
- Source range: L694-L703
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.T148` — m_μ/m_e Best NLO Formula: ι_τ⁻⁴·⁹⁶ at +307 ppm

## Immediate Comment / Docstring

```lean
/-- [IV.T148] NLO muon mass ratio structure (formalized). -/
```

## Source Excerpt

```lean
structure MuonMassNLO where
  /-- Effective exponent ×100. -/
  exponent_x100 : Nat := 496
  /-- Gap from integer ×100. -/
  gap_x100 : Nat := 4
  /-- Deviation from PDG in ppm. -/
  deviation_ppm : Nat := 307
  /-- Number of formulas scanned. -/
  n_formulas_scanned : Nat := 14
  deriving Repr
```
