---
{
  "projection_kind": "taulib_declaration",
  "title": "remark_hierarchy_dissolution",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/remark-hierarchy-dissolution/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Electroweak.TauHiggs2`.",
  "declaration_id": "TauLib.BookIV.Electroweak.TauHiggs2::remark_hierarchy_dissolution",
  "declaration_slug": "remark-hierarchy-dissolution",
  "kind": "def",
  "name": "remark_hierarchy_dissolution",
  "module_name": "TauLib.BookIV.Electroweak.TauHiggs2",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/",
  "source_line_start": 325,
  "source_line_end": 326,
  "registry_ids": [
    "IV.R35"
  ],
  "related_registry_items": [
    {
      "id": "IV.R35",
      "title": "Structural Resolution of Hierarchy",
      "url": "/registry/object/IV.R35/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs2.lean#L325-L326",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.TauHiggs2",
        "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs2.lean#L325-L326",
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

- Module: [TauLib.BookIV.Electroweak.TauHiggs2](/verify/taulib/docs/book-iv-electroweak-tau-higgs2/)
- Source path: [`TauLib/BookIV/Electroweak/TauHiggs2.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs2.lean#L325-L326)
- Source range: L325-L326
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `IV.R35` — Structural Resolution of Hierarchy

## Immediate Comment / Docstring

```lean
/-- [IV.R35] The hierarchy problem (why is M_H ≪ M_Planck?) does not
    arise in the τ-framework because:
    1. The Higgs is emergent, not fundamental → no UV sensitivity.
    2. M_Planck is NOT a fundamental scale — it is derived from ι_τ.
    3. The ratio M_H/M_Planck ≈ 10⁻¹⁷ is a CONSEQUENCE of the
       sector coupling hierarchy, not a fine-tuning accident. -/
```

## Source Excerpt

```lean
def remark_hierarchy_dissolution : String :=
  "No hierarchy problem: Higgs is emergent, M_Planck derived from iota_tau, ratio is structural"
```
