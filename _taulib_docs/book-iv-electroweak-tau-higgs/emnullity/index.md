---
{
  "projection_kind": "taulib_declaration",
  "title": "EMNullity",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-tau-higgs/emnullity/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.TauHiggs`.",
  "declaration_id": "TauLib.BookIV.Electroweak.TauHiggs::EMNullity",
  "declaration_slug": "emnullity",
  "kind": "structure",
  "name": "EMNullity",
  "module_name": "TauLib.BookIV.Electroweak.TauHiggs",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs/",
  "source_line_start": 157,
  "source_line_end": 164,
  "registry_ids": [
    "IV.D138"
  ],
  "related_registry_items": [
    {
      "id": "IV.D138",
      "title": "EM-Nullity Condition",
      "url": "/registry/object/IV.D138/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs.lean#L157-L164",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.TauHiggs",
        "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs.lean#L157-L164",
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

- Module: [TauLib.BookIV.Electroweak.TauHiggs](/verify/taulib/docs/book-iv-electroweak-tau-higgs/)
- Source path: [`TauLib/BookIV/Electroweak/TauHiggs.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs.lean#L157-L164)
- Source range: L157-L164
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D138` — EM-Nullity Condition

## Immediate Comment / Docstring

```lean
/-- [IV.D138] EM-nullity: the photon remains massless after
    electroweak symmetry breaking.

    In the τ-framework, this is a THEOREM, not a tuning condition:
    the U(1)_EM generator is the unique combination of W³ and B
    that commutes with the ω-sector VEV. The VEV breaks SU(2)_L × U(1)_Y
    down to U(1)_EM, and the unbroken generator gives a massless photon. -/
```

## Source Excerpt

```lean
structure EMNullity where
  /-- The photon is massless. -/
  photon_massless : Bool := true
  /-- The unbroken symmetry is U(1)_EM. -/
  unbroken_symmetry : String := "U(1)_EM"
  /-- This is forced by the VEV structure. -/
  forced_by_vev : Bool := true
  deriving Repr
```
