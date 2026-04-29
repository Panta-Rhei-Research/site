---
{
  "projection_kind": "taulib_declaration",
  "title": "JarlskogInvariantTau",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/jarlskog-invariant-tau-l1438/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::JarlskogInvariantTau",
  "declaration_slug": "jarlskog-invariant-tau-l1438",
  "kind": "structure",
  "name": "JarlskogInvariantTau",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 1438,
  "source_line_end": 1445,
  "registry_ids": [
    "IV.T167"
  ],
  "related_registry_items": [
    {
      "id": "IV.T167",
      "title": "Jarlskog Invariant J from τ-Parameters",
      "url": "/registry/object/IV.T167/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1438-L1445",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1438-L1445",
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
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1438-L1445)
- Source range: L1438-L1445
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.T167` — Jarlskog Invariant J from τ-Parameters

## Immediate Comment / Docstring

```lean
/-- [IV.T167] Jarlskog invariant from τ-parameters structure (formalized). -/
```

## Source Excerpt

```lean
structure JarlskogInvariantTau where
  /-- Number of Wolfenstein parameters used. -/
  n_wolfenstein_params : Nat := 4
  /-- Deviation from PDG in ppm. -/
  deviation_ppm : Nat := 6479
  /-- Self-consistency gap in ppm (inverse vs forward). -/
  self_consistency_ppm : Nat := 6522
  deriving Repr
```
