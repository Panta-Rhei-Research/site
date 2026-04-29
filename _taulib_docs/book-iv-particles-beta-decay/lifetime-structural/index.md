---
{
  "projection_kind": "taulib_declaration",
  "title": "LifetimeStructural",
  "permalink": "/verify/taulib/docs/book-iv-particles-beta-decay/lifetime-structural/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.BetaDecay`.",
  "declaration_id": "TauLib.BookIV.Particles.BetaDecay::LifetimeStructural",
  "declaration_slug": "lifetime-structural",
  "kind": "structure",
  "name": "LifetimeStructural",
  "module_name": "TauLib.BookIV.Particles.BetaDecay",
  "module_url": "/verify/taulib/docs/book-iv-particles-beta-decay/",
  "source_line_start": 111,
  "source_line_end": 118,
  "registry_ids": [
    "IV.R122"
  ],
  "related_registry_items": [
    {
      "id": "IV.R122",
      "title": "Structural lifetime estimate",
      "url": "/registry/object/IV.R122/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/BetaDecay.lean#L111-L118",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Particles.BetaDecay",
        "url": "/verify/taulib/docs/book-iv-particles-beta-decay/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/BetaDecay.lean#L111-L118",
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

- Module: [TauLib.BookIV.Particles.BetaDecay](/verify/taulib/docs/book-iv-particles-beta-decay/)
- Source path: [`TauLib/BookIV/Particles/BetaDecay.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/BetaDecay.lean#L111-L118)
- Source range: L111-L118
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.R122` — Structural lifetime estimate

## Immediate Comment / Docstring

```lean
/-- [IV.R122] Neutron lifetime involves G_F, m_e, Q_β (all ι_τ-determined)
    but the axial coupling g_A ≈ 1.276 requires detailed quark-level
    T² breathing mode structure — conjectural scope. -/
```

## Source Excerpt

```lean
structure LifetimeStructural where
  /-- Axial coupling (×1000). -/
  g_A_x1000 : Nat := 1276
  /-- Free neutron lifetime (seconds, approx). -/
  lifetime_s : Nat := 879
  /-- Scope (upgraded from conjectural at Wave 46B). -/
  scope : String := "tau-effective"
  deriving Repr
```
