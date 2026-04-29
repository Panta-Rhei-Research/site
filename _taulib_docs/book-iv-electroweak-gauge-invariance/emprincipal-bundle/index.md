---
{
  "projection_kind": "taulib_declaration",
  "title": "EMPrincipalBundle",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance/emprincipal-bundle/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.GaugeInvariance`.",
  "declaration_id": "TauLib.BookIV.Electroweak.GaugeInvariance::EMPrincipalBundle",
  "declaration_slug": "emprincipal-bundle",
  "kind": "structure",
  "name": "EMPrincipalBundle",
  "module_name": "TauLib.BookIV.Electroweak.GaugeInvariance",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance/",
  "source_line_start": 63,
  "source_line_end": 76,
  "registry_ids": [
    "IV.D85"
  ],
  "related_registry_items": [
    {
      "id": "IV.D85",
      "title": "EM Principal Bundle",
      "url": "/registry/object/IV.D85/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/GaugeInvariance.lean#L63-L76",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.GaugeInvariance",
        "url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/GaugeInvariance.lean#L63-L76",
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

- Module: [TauLib.BookIV.Electroweak.GaugeInvariance](/verify/taulib/docs/book-iv-electroweak-gauge-invariance/)
- Source path: [`TauLib/BookIV/Electroweak/GaugeInvariance.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/GaugeInvariance.lean#L63-L76)
- Source range: L63-L76
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D85` — EM Principal Bundle

## Immediate Comment / Docstring

```lean
/-- [IV.D85] The EM principal bundle P_EM → T² with structure group U(1).
    The B-sector gauge field lives on this bundle. -/
```

## Source Excerpt

```lean
structure EMPrincipalBundle where
  /-- Base space dimension (T² = 2). -/
  base_dim : Nat
  base_eq : base_dim = 2
  /-- Structure group dimension (U(1) = 1). -/
  group_dim : Nat
  group_eq : group_dim = 1
  /-- Total space dimension = base + group. -/
  total_dim : Nat
  total_eq : total_dim = base_dim + group_dim
  /-- The sector: must be B (EM). -/
  sector : Sector
  sector_eq : sector = .B
  deriving Repr
```
