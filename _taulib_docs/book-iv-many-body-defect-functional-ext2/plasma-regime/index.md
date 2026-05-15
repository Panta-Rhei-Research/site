---
{
  "projection_kind": "taulib_declaration",
  "title": "PlasmaRegime",
  "permalink": "/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/plasma-regime/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.ManyBody.DefectFunctionalExt2`.",
  "declaration_id": "TauLib.BookIV.ManyBody.DefectFunctionalExt2::PlasmaRegime",
  "declaration_slug": "plasma-regime",
  "kind": "structure",
  "name": "PlasmaRegime",
  "module_name": "TauLib.BookIV.ManyBody.DefectFunctionalExt2",
  "module_url": "/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/",
  "source_line_start": 163,
  "source_line_end": 170,
  "registry_ids": [
    "IV.D225"
  ],
  "related_registry_items": [
    {
      "id": "IV.D225",
      "title": "Plasma regime",
      "url": "/registry/object/IV.D225/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L163-L170",
  "formal_status": "defined",
  "declaration_role": "type/data schema",
  "formal_status_label": "type/data schema",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.ManyBody.DefectFunctionalExt2",
        "url": "/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L163-L170",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
      "role": "type/data schema",
      "status": "type/data schema"
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

- Module: [TauLib.BookIV.ManyBody.DefectFunctionalExt2](/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/)
- Source path: [`TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L163-L170)
- Source range: L163-L170
- Kind: `structure`
- Public role: `type/data schema`
- Formal status hint: `type/data schema`

## Registry Links

- `IV.D225` — Plasma regime

## Immediate Comment / Docstring

```lean
/-- [IV.D225] The plasma regime: mu, |nu|, |kappa| > mu_crit and theta
    is fluctuating (not globally fixed). Topological charge can change
    through defect pair creation/annihilation. -/
```

## Source Excerpt

```lean
structure PlasmaRegime where
  /-- All transport components above threshold. -/
  all_above_threshold : Bool := true
  /-- Theta fluctuating. -/
  theta_fluctuating : Bool := true
  /-- Debye screening present. -/
  debye_screening : Bool := true
  deriving Repr
```
