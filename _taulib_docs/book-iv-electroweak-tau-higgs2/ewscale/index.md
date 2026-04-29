---
{
  "projection_kind": "taulib_declaration",
  "title": "EWScale",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/ewscale/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.TauHiggs2`.",
  "declaration_id": "TauLib.BookIV.Electroweak.TauHiggs2::EWScale",
  "declaration_slug": "ewscale",
  "kind": "structure",
  "name": "EWScale",
  "module_name": "TauLib.BookIV.Electroweak.TauHiggs2",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/",
  "source_line_start": 157,
  "source_line_end": 164,
  "registry_ids": [
    "IV.D320"
  ],
  "related_registry_items": [
    {
      "id": "IV.D320",
      "title": "Electroweak scale in Category~tau",
      "url": "/registry/object/IV.D320/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs2.lean#L157-L164",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs2.lean#L157-L164",
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
- Source path: [`TauLib/BookIV/Electroweak/TauHiggs2.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs2.lean#L157-L164)
- Source range: L157-L164
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D320` — Electroweak scale in Category~tau

## Immediate Comment / Docstring

```lean
/-- [IV.D320] The electroweak scale v_EW ≈ 246.2 GeV: the vacuum
    expectation value of the ω-sector coherence functional.
    v_EW = √(2) · M_W / g ≈ 246200 MeV.

    This is the single energy scale that determines all EW boson masses
    via M_W = g·v/2, M_Z = M_W/cos(θ_W), M_H = √(2λ)·v. -/
```

## Source Excerpt

```lean
structure EWScale where
  /-- v_EW in MeV. -/
  vev_MeV : Nat := 246200
  /-- Positive. -/
  vev_pos : vev_MeV > 0 := by omega
  /-- Determines all EW boson masses. -/
  determines_masses : Bool := true
  deriving Repr
```
