---
{
  "projection_kind": "taulib_declaration",
  "title": "qcd_denom",
  "permalink": "/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/qcd-denom/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Physics.NucleonMassSplitting`.",
  "declaration_id": "TauLib.BookIV.Physics.NucleonMassSplitting::qcd_denom",
  "declaration_slug": "qcd-denom",
  "kind": "def",
  "name": "qcd_denom",
  "module_name": "TauLib.BookIV.Physics.NucleonMassSplitting",
  "module_url": "/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/",
  "source_line_start": 130,
  "source_line_end": 130,
  "registry_ids": [
    "IV.D341"
  ],
  "related_registry_items": [
    {
      "id": "IV.D341",
      "title": "QCD Contribution to p-n splitting",
      "url": "/registry/object/IV.D341/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/NucleonMassSplitting.lean#L130-L130",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Physics.NucleonMassSplitting",
        "url": "/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/NucleonMassSplitting.lean#L130-L130",
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

- Module: [TauLib.BookIV.Physics.NucleonMassSplitting](/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/)
- Source path: [`TauLib/BookIV/Physics/NucleonMassSplitting.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/NucleonMassSplitting.lean#L130-L130)
- Source range: L130-L130
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `IV.D341` — QCD Contribution to p-n splitting

## Immediate Comment / Docstring

```lean
/-- [IV.D341] QCD contribution denominator: 16 · √3_denom · ι_τ⁵_denom. -/
```

## Source Excerpt

```lean
def qcd_denom : Nat := 16 * sqrt3_denom * iota5_denom
```
