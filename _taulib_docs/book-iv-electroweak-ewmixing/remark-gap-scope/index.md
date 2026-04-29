---
{
  "projection_kind": "taulib_declaration",
  "title": "remark_gap_scope",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-ewmixing/remark-gap-scope/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Electroweak.EWMixing`.",
  "declaration_id": "TauLib.BookIV.Electroweak.EWMixing::remark_gap_scope",
  "declaration_slug": "remark-gap-scope",
  "kind": "def",
  "name": "remark_gap_scope",
  "module_name": "TauLib.BookIV.Electroweak.EWMixing",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-ewmixing/",
  "source_line_start": 441,
  "source_line_end": 442,
  "registry_ids": [
    "IV.R31"
  ],
  "related_registry_items": [
    {
      "id": "IV.R31",
      "title": "Weinberg Angle Gap Assessment",
      "url": "/registry/object/IV.R31/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/EWMixing.lean#L441-L442",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.EWMixing",
        "url": "/verify/taulib/docs/book-iv-electroweak-ewmixing/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/EWMixing.lean#L441-L442",
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

- Module: [TauLib.BookIV.Electroweak.EWMixing](/verify/taulib/docs/book-iv-electroweak-ewmixing/)
- Source path: [`TauLib/BookIV/Electroweak/EWMixing.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/EWMixing.lean#L441-L442)
- Source range: L441-L442
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `IV.R31` — Weinberg Angle Gap Assessment

## Immediate Comment / Docstring

```lean
/-- [IV.R31] The 2.7% tree-level deviation between the τ-predicted
    sin²(θ_W) ≈ 0.2249 and the experimental value ≈ 0.2312 is
    expected to be closed by radiative corrections.

    The deviation is comparable in magnitude to the 1-loop EW
    corrections in the Standard Model, and has the correct sign
    (τ predicts BELOW the Z-pole value, as expected for a
    tree-level coupling evaluated at the fundamental scale). -/
```

## Source Excerpt

```lean
def remark_gap_scope : String :=
  "Tree-level deviation 2.7%: expected loop-level closure, correct sign"
```
