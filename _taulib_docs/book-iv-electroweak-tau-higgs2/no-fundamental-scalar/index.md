---
{
  "projection_kind": "taulib_declaration",
  "title": "NoFundamentalScalar",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/no-fundamental-scalar/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.TauHiggs2`.",
  "declaration_id": "TauLib.BookIV.Electroweak.TauHiggs2::NoFundamentalScalar",
  "declaration_slug": "no-fundamental-scalar",
  "kind": "structure",
  "name": "NoFundamentalScalar",
  "module_name": "TauLib.BookIV.Electroweak.TauHiggs2",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/",
  "source_line_start": 203,
  "source_line_end": 212,
  "registry_ids": [
    "IV.T65"
  ],
  "related_registry_items": [
    {
      "id": "IV.T65",
      "title": "No Hierarchy Problem in Category τ",
      "url": "/registry/object/IV.T65/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs2.lean#L203-L212",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs2.lean#L203-L212",
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
- Source path: [`TauLib/BookIV/Electroweak/TauHiggs2.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs2.lean#L203-L212)
- Source range: L203-L212
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.T65` — No Hierarchy Problem in Category τ

## Immediate Comment / Docstring

```lean
/-- [IV.T65] The τ-Higgs is NOT a fundamental scalar field.
    It is a collective excitation of the ω-sector coherence.

    Consequences:
    1. No UV cutoff sensitivity → no hierarchy problem.
    2. No quadratic divergence in the mass renormalization.
    3. The Higgs mass is NATURALLY at the EW scale without fine-tuning.

    This is the τ-framework's resolution of the hierarchy problem:
    it simply does not arise because the Higgs is emergent, not fundamental. -/
```

## Source Excerpt

```lean
structure NoFundamentalScalar where
  /-- The Higgs is a collective/emergent excitation. -/
  is_emergent : Bool := true
  /-- No UV cutoff sensitivity. -/
  no_uv_sensitivity : Bool := true
  /-- No quadratic divergence. -/
  no_quadratic_divergence : Bool := true
  /-- Mass naturally at EW scale. -/
  natural_mass : Bool := true
  deriving Repr
```
