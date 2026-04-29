---
{
  "projection_kind": "taulib_declaration",
  "title": "TauYukawaCoupling",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/tau-yukawa-coupling/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.TauHiggs2`.",
  "declaration_id": "TauLib.BookIV.Electroweak.TauHiggs2::TauYukawaCoupling",
  "declaration_slug": "tau-yukawa-coupling",
  "kind": "structure",
  "name": "TauYukawaCoupling",
  "module_name": "TauLib.BookIV.Electroweak.TauHiggs2",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/",
  "source_line_start": 114,
  "source_line_end": 123,
  "registry_ids": [
    "IV.D142"
  ],
  "related_registry_items": [
    {
      "id": "IV.D142",
      "title": "τ-Yukawa Coupling (Ch34)",
      "url": "/registry/object/IV.D142/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs2.lean#L114-L123",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs2.lean#L114-L123",
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

- Module: [TauLib.BookIV.Electroweak.TauHiggs2](/verify/taulib/docs/book-iv-electroweak-tau-higgs2/)
- Source path: [`TauLib/BookIV/Electroweak/TauHiggs2.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs2.lean#L114-L123)
- Source range: L114-L123
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D142` — τ-Yukawa Coupling (Ch34)

## Immediate Comment / Docstring

```lean
/-- [IV.D142] A τ-Yukawa coupling: the coupling of a fermion
    to the ω-sector VEV, determining the fermion's mass via
    m_f = y_f · v_EW / √2.

    In the τ-framework, Yukawa couplings are NOT free parameters —
    they are determined by the sector hierarchy and ι_τ. -/
```

## Source Excerpt

```lean
structure TauYukawaCoupling where
  /-- Fermion label. -/
  fermion : String
  /-- Yukawa coupling numerator (scaled ×10⁶). -/
  y_numer : Nat
  /-- Yukawa coupling denominator. -/
  y_denom : Nat
  /-- Denominator positive. -/
  denom_pos : y_denom > 0 := by omega
  deriving Repr
```
