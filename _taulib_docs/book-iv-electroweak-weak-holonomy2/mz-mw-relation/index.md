---
{
  "projection_kind": "taulib_declaration",
  "title": "mz_mw_relation",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-weak-holonomy2/mz-mw-relation/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Electroweak.WeakHolonomy2`.",
  "declaration_id": "TauLib.BookIV.Electroweak.WeakHolonomy2::mz_mw_relation",
  "declaration_slug": "mz-mw-relation",
  "kind": "theorem",
  "name": "mz_mw_relation",
  "module_name": "TauLib.BookIV.Electroweak.WeakHolonomy2",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-weak-holonomy2/",
  "source_line_start": 108,
  "source_line_end": 110,
  "registry_ids": [
    "IV.T55"
  ],
  "related_registry_items": [
    {
      "id": "IV.T55",
      "title": "Z Mass from Coherence Fixing",
      "url": "/registry/object/IV.T55/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakHolonomy2.lean#L108-L110",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.WeakHolonomy2",
        "url": "/verify/taulib/docs/book-iv-electroweak-weak-holonomy2/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakHolonomy2.lean#L108-L110",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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

- Module: [TauLib.BookIV.Electroweak.WeakHolonomy2](/verify/taulib/docs/book-iv-electroweak-weak-holonomy2/)
- Source path: [`TauLib/BookIV/Electroweak/WeakHolonomy2.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakHolonomy2.lean#L108-L110)
- Source range: L108-L110
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.T55` — Z Mass from Coherence Fixing

## Immediate Comment / Docstring

```lean
/-- [IV.T55] Z mass from W mass via Weinberg angle:
    M_Z = M_W / cos(theta_W).
    Since cos^2(theta_W) = 1 - sin^2(theta_W) = 7688/10000,
    M_Z^2 = M_W^2 / cos^2(theta_W).
    Structural check: M_Z^2 * cos^2 should approximate M_W^2.
    M_W^2 = 80379^2 = 6460781641, M_Z^2 = 91188^2 = 8315246544.
    M_Z^2 * 7688 / 10000 = 6393525297 (within 1% of M_W^2). -/
```

## Source Excerpt

```lean
theorem mz_mw_relation :
    z_mass_mev.mass_numer > w_mass_mev.mass_numer := by
  simp [z_mass_mev, w_mass_mev]
```
