---
{
  "projection_kind": "taulib_declaration",
  "title": "remark_quark_lepton",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/remark-quark-lepton/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::remark_quark_lepton",
  "declaration_slug": "remark-quark-lepton",
  "kind": "def",
  "name": "remark_quark_lepton",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 624,
  "source_line_end": 628,
  "registry_ids": [
    "IV.R396"
  ],
  "related_registry_items": [
    {
      "id": "IV.R396",
      "title": "Quark-Lepton Universality Conjecture",
      "url": "/registry/object/IV.R396/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L624-L628",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L624-L628",
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
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L624-L628)
- Source range: L624-L628
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `IV.R396` — Quark-Lepton Universality Conjecture

## Immediate Comment / Docstring

```lean
/-- [IV.R396] Quark-lepton universality conjecture (scope: conjectural).
    Quark sigma-matrices M_q = [[a',b',0],[b',c',b'],[0,b',a']] use the same
    structure as M_ℓ but with entries scaled by sector coupling ratios:
    - Up-sector (u,c,t): entries scaled by kappa(C;3)/kappa(B;2) = iota/(1-iota)
    - Down-sector (d,s,b): entries scaled by kappa(A;2)/kappa(B;2)
    Sigma-equivariance is topological (from L), not sector-specific. -/
```

## Source Excerpt

```lean
def remark_quark_lepton : String :=
  "Quark sigma-matrices M_q: same structure as M_l but different sector couplings. " ++
  "Up-sector: scale factor kappa(C;3)/kappa(B;2) = iota/(1-iota). " ++
  "Down-sector: scale factor kappa(A;2)/kappa(B;2). " ++
  "Universality: sigma-equivariance is topological, not sector-specific."
```
