---
{
  "projection_kind": "taulib_declaration",
  "title": "PhysicalVacuum",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-tau-higgs/physical-vacuum/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.TauHiggs`.",
  "declaration_id": "TauLib.BookIV.Electroweak.TauHiggs::PhysicalVacuum",
  "declaration_slug": "physical-vacuum",
  "kind": "structure",
  "name": "PhysicalVacuum",
  "module_name": "TauLib.BookIV.Electroweak.TauHiggs",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs/",
  "source_line_start": 114,
  "source_line_end": 123,
  "registry_ids": [
    "IV.D136"
  ],
  "related_registry_items": [
    {
      "id": "IV.D136",
      "title": "Physical Vacuum Ω*[ω]",
      "url": "/registry/object/IV.D136/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs.lean#L114-L123",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs.lean#L114-L123",
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
- Source path: [`TauLib/BookIV/Electroweak/TauHiggs.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs.lean#L114-L123)
- Source range: L114-L123
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D136` — Physical Vacuum Ω*[ω]

## Immediate Comment / Docstring

```lean
/-- [IV.D136] The physical vacuum: the minimum of the coherence
    functional V_n. The vacuum expectation value (VEV) v_EW ≈ 246 GeV
    sets the electroweak scale.

    In the τ-framework, v_EW is determined by ι_τ and the
    neutron mass anchor m_n, NOT as a free parameter. -/
```

## Source Excerpt

```lean
structure PhysicalVacuum where
  /-- VEV in MeV (v_EW ≈ 246200 MeV). -/
  vev_MeV : Nat := 246200
  /-- VEV is unique (up to S¹ degeneracy). -/
  unique : Bool := true
  /-- Vacuum is stable (V_n has positive second derivative). -/
  stable : Bool := true
  /-- VEV is nonzero (spontaneous breaking occurs). -/
  vev_nonzero : vev_MeV > 0 := by omega
  deriving Repr
```
