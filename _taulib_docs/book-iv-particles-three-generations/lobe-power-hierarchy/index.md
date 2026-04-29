---
{
  "projection_kind": "taulib_declaration",
  "title": "LobePowerHierarchy",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/lobe-power-hierarchy/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::LobePowerHierarchy",
  "declaration_slug": "lobe-power-hierarchy",
  "kind": "structure",
  "name": "LobePowerHierarchy",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 2977,
  "source_line_end": 2990,
  "registry_ids": [
    "IV.P223"
  ],
  "related_registry_items": [
    {
      "id": "IV.P223",
      "title": "Lobe-Power Hierarchy of Quark Exponents",
      "url": "/registry/object/IV.P223/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2977-L2990",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2977-L2990",
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
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2977-L2990)
- Source range: L2977-L2990
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P223` — Lobe-Power Hierarchy of Quark Exponents

## Immediate Comment / Docstring

```lean
/-- [IV.P223] Lobe-power hierarchy of quark exponents.
    lobes^k: k=0 (input), k=1 (isospin), k=2 (generation), k=6 (full). -/
```

## Source Excerpt

```lean
structure LobePowerHierarchy where
  /-- k=0: input exponent (m_t). -/
  k0_value : Nat := 1
  /-- k=1: isospin splitting (m_u/m_d). -/
  k1_value : Nat := 2
  /-- k=2: generation transition (m_s/m_b, m_t/m_b). -/
  k2_value : Nat := 4
  /-- k=2·dim: full phase space (m_d/m_s). -/
  k6_value : Nat := 64
  /-- k=2·dim = 2×3 = 6. -/
  full_dim : Nat := 6
  /-- Check: lobes^6 = 64. -/
  phase_check : 2 ^ 6 = k6_value := by decide
  deriving Repr
```
