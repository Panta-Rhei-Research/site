---
{
  "projection_kind": "taulib_declaration",
  "title": "mz_gt_mw",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-weak-holonomy2/mz-gt-mw/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Electroweak.WeakHolonomy2`.",
  "declaration_id": "TauLib.BookIV.Electroweak.WeakHolonomy2::mz_gt_mw",
  "declaration_slug": "mz-gt-mw",
  "kind": "theorem",
  "name": "mz_gt_mw",
  "module_name": "TauLib.BookIV.Electroweak.WeakHolonomy2",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-weak-holonomy2/",
  "source_line_start": 190,
  "source_line_end": 192,
  "registry_ids": [
    "IV.P62"
  ],
  "related_registry_items": [
    {
      "id": "IV.P62",
      "title": "Z Heavier Than W",
      "url": "/registry/object/IV.P62/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakHolonomy2.lean#L190-L192",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakHolonomy2.lean#L190-L192",
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
- Source path: [`TauLib/BookIV/Electroweak/WeakHolonomy2.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakHolonomy2.lean#L190-L192)
- Source range: L190-L192
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.P62` — Z Heavier Than W

## Immediate Comment / Docstring

```lean
/-- [IV.P62] M_Z > M_W: the Z boson is heavier than the W boson.
    This follows from cos(theta_W) < 1, so M_Z = M_W/cos > M_W. -/
```

## Source Excerpt

```lean
theorem mz_gt_mw :
    z_mass_mev.mass_numer > w_mass_mev.mass_numer := by
  simp [z_mass_mev, w_mass_mev]
```
