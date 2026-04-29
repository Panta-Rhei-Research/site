---
{
  "projection_kind": "taulib_declaration",
  "title": "EBFields",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/ebfields/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.TauMaxwell`.",
  "declaration_id": "TauLib.BookIV.Electroweak.TauMaxwell::EBFields",
  "declaration_slug": "ebfields",
  "kind": "structure",
  "name": "EBFields",
  "module_name": "TauLib.BookIV.Electroweak.TauMaxwell",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/",
  "source_line_start": 148,
  "source_line_end": 158,
  "registry_ids": [
    "IV.D101"
  ],
  "related_registry_items": [
    {
      "id": "IV.D101",
      "title": "Electric and Magnetic Field Extraction",
      "url": "/registry/object/IV.D101/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauMaxwell.lean#L148-L158",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.TauMaxwell",
        "url": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauMaxwell.lean#L148-L158",
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

- Module: [TauLib.BookIV.Electroweak.TauMaxwell](/verify/taulib/docs/book-iv-electroweak-tau-maxwell/)
- Source path: [`TauLib/BookIV/Electroweak/TauMaxwell.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauMaxwell.lean#L148-L158)
- Source range: L148-L158
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D101` — Electric and Magnetic Field Extraction

## Immediate Comment / Docstring

```lean
/-- [IV.D101] Decomposition of F_μν into E and B fields.
    F_{0i} = E_i (electric), F_{ij} = ε_{ijk} B_k (magnetic).
    The split is observer-dependent (frame-dependent). -/
```

## Source Excerpt

```lean
structure EBFields where
  /-- Electric field components (3). -/
  e_components : Nat
  e_eq : e_components = 3
  /-- Magnetic field components (3). -/
  b_components : Nat
  b_eq : b_components = 3
  /-- Total independent components = 3 + 3 = 6. -/
  total : Nat
  total_eq : total = e_components + b_components
  deriving Repr
```
