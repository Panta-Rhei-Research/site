---
{
  "projection_kind": "taulib_declaration",
  "title": "eval at L289",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-weak-holonomy2/eval-l289/",
  "summary_short": "`eval` declaration in `TauLib.BookIV.Electroweak.WeakHolonomy2`.",
  "declaration_id": "TauLib.BookIV.Electroweak.WeakHolonomy2::#eval:289",
  "declaration_slug": "eval-l289",
  "kind": "eval",
  "name": null,
  "module_name": "TauLib.BookIV.Electroweak.WeakHolonomy2",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-weak-holonomy2/",
  "source_line_start": 289,
  "source_line_end": 289,
  "registry_ids": [
    "IV.R29"
  ],
  "related_registry_items": [
    {
      "id": "IV.R29",
      "title": "Hierarchy Problem in Category Tau",
      "url": "/registry/object/IV.R29/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakHolonomy2.lean#L289-L289",
  "formal_status": "computed",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakHolonomy2.lean#L289-L289",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "eval",
      "status": "computed"
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
- Source path: [`TauLib/BookIV/Electroweak/WeakHolonomy2.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakHolonomy2.lean#L289-L289)
- Source range: L289-L289
- Kind: `eval`
- Formal status hint: `computed`

## Registry Links

- `IV.R29` — Hierarchy Problem in Category Tau

## Immediate Comment / Docstring

```lean
-- [IV.R29] Hierarchy problem dissolution: in the tau-framework, the
-- Higgs mass is set by the omega-crossing coherence scale, which is
-- a fixed-point readout of iota_tau. There is no fine-tuning because
-- there is no free parameter to tune: the scale is determined by
-- categorical structure, not by cancellation of large corrections.
-- The "hierarchy problem" is an artifact of treating the Higgs mass
-- as a free parameter in a Lagrangian framework.
-- (Structural remark)

-- ============================================================
-- SMOKE TESTS
-- ============================================================
```

## Source Excerpt

```lean
#eval weinberg_sin2_float                       -- ~0.2312
```
