---
{
  "projection_kind": "taulib_declaration",
  "title": "HolonomySector",
  "permalink": "/verify/taulib/docs/book-iv-strong-gap-meta-theorem/holonomy-sector/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Strong.GapMetaTheorem`.",
  "declaration_id": "TauLib.BookIV.Strong.GapMetaTheorem::HolonomySector",
  "declaration_slug": "holonomy-sector",
  "kind": "structure",
  "name": "HolonomySector",
  "module_name": "TauLib.BookIV.Strong.GapMetaTheorem",
  "module_url": "/verify/taulib/docs/book-iv-strong-gap-meta-theorem/",
  "source_line_start": 59,
  "source_line_end": 72,
  "registry_ids": [
    "IV.D162"
  ],
  "related_registry_items": [
    {
      "id": "IV.D162",
      "title": "τ-Holonomy sector",
      "url": "/registry/object/IV.D162/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/GapMetaTheorem.lean#L59-L72",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Strong.GapMetaTheorem",
        "url": "/verify/taulib/docs/book-iv-strong-gap-meta-theorem/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/GapMetaTheorem.lean#L59-L72",
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

- Module: [TauLib.BookIV.Strong.GapMetaTheorem](/verify/taulib/docs/book-iv-strong-gap-meta-theorem/)
- Source path: [`TauLib/BookIV/Strong/GapMetaTheorem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/GapMetaTheorem.lean#L59-L72)
- Source range: L59-L72
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D162` — τ-Holonomy sector

## Immediate Comment / Docstring

```lean
/-- [IV.D162] A tau-holonomy sector: at each finite stage n, a finite
    configuration space C_n, a finite admissible subset C_n^{adm},
    a defect functional V_n, and refinement/restriction maps.

    This is the abstract template instantiated by each physical sector. -/
```

## Source Excerpt

```lean
structure HolonomySector where
  /-- Sector label. -/
  sector : Sector
  /-- Activation depth (minimum stage for nontrivial configurations). -/
  activation_depth : Nat
  /-- Configuration space is finite at each stage. -/
  config_finite : Bool := true
  /-- Admissible subset is nonempty. -/
  adm_nonempty : Bool := true
  /-- Defect functional is well-defined. -/
  defect_defined : Bool := true
  /-- Refinement maps exist. -/
  refinement_maps : Bool := true
  deriving Repr
```
