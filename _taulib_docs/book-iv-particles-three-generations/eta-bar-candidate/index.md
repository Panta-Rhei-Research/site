---
{
  "projection_kind": "taulib_declaration",
  "title": "EtaBarCandidate",
  "permalink": "/corpus/taulib/docs/book-iv-particles-three-generations/eta-bar-candidate/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::EtaBarCandidate",
  "declaration_slug": "eta-bar-candidate",
  "kind": "structure",
  "name": "EtaBarCandidate",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/corpus/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 1285,
  "source_line_end": 1292,
  "registry_ids": [
    "IV.P197"
  ],
  "related_registry_items": [
    {
      "id": "IV.P197",
      "title": "eta_bar from CP Phase Structure: Best tau-Candidate sqrt(5)/(2*pi)",
      "url": "/registry/object/IV.P197/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1285-L1292",
  "formal_status": "defined",
  "declaration_role": "type/data schema",
  "formal_status_label": "type/data schema",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Particles.ThreeGenerations",
        "url": "/corpus/taulib/docs/book-iv-particles-three-generations/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1285-L1292",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
      "role": "type/data schema",
      "status": "type/data schema"
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

- Module: [TauLib.BookIV.Particles.ThreeGenerations](/corpus/taulib/docs/book-iv-particles-three-generations/)
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1285-L1292)
- Source range: L1285-L1292
- Kind: `structure`
- Public role: `type/data schema`
- Formal status hint: `type/data schema`

## Registry Links

- `IV.P197` — eta_bar from CP Phase Structure: Best tau-Candidate sqrt(5)/(2*pi)

## Immediate Comment / Docstring

```lean
/-- [IV.P197] η̄ candidate structure. -/
```

## Source Excerpt

```lean
structure EtaBarCandidate where
  /-- Radicand under √ in formula: √5. -/
  sqrt_radicand : Nat := 5
  /-- ω-period multiplier in denominator: 2π. -/
  omega_period_multiplier : Nat := 2
  /-- Deviation from PDG in ppm (superseded by pentagon at 2285 ppm). -/
  deviation_ppm : Nat := 22647
  deriving Repr
```
