---
{
  "projection_kind": "taulib_declaration",
  "title": "WolfensteinOmegaDerivation",
  "permalink": "/corpus/taulib/docs/book-iv-particles-three-generations/wolfenstein-omega-derivation-l1209/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::WolfensteinOmegaDerivation",
  "declaration_slug": "wolfenstein-omega-derivation-l1209",
  "kind": "structure",
  "name": "WolfensteinOmegaDerivation",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/corpus/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 1209,
  "source_line_end": 1218,
  "registry_ids": [
    "IV.D357"
  ],
  "related_registry_items": [
    {
      "id": "IV.D357",
      "title": "Wolfenstein CP Parameters from omega-Sector Holonomy Period",
      "url": "/registry/object/IV.D357/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1209-L1218",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1209-L1218",
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
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1209-L1218)
- Source range: L1209-L1218
- Kind: `structure`
- Public role: `type/data schema`
- Formal status hint: `type/data schema`

## Registry Links

- `IV.D357` — Wolfenstein CP Parameters from omega-Sector Holonomy Period

## Immediate Comment / Docstring

```lean
/-- [IV.D357] Wolfenstein ω-derivation structure (formalized). -/
```

## Source Excerpt

```lean
structure WolfensteinOmegaDerivation where
  /-- ρ̄ deviation from PDG in ppm. -/
  rho_deviation_ppm : Nat := 975
  /-- A deviation from PDG in ppm. -/
  a_deviation_ppm : Nat := 887
  /-- η̄ deviation from PDG in ppm (conjectural stage). -/
  eta_deviation_ppm : Nat := 22647
  /-- Number of τ-effective parameters so far. -/
  n_tau_effective : Nat := 3
  deriving Repr
```
