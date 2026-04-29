---
{
  "projection_kind": "taulib_declaration",
  "title": "pn_sign_positive",
  "permalink": "/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/pn-sign-positive/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Physics.NucleonMassSplitting`.",
  "declaration_id": "TauLib.BookIV.Physics.NucleonMassSplitting::pn_sign_positive",
  "declaration_slug": "pn-sign-positive",
  "kind": "theorem",
  "name": "pn_sign_positive",
  "module_name": "TauLib.BookIV.Physics.NucleonMassSplitting",
  "module_url": "/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/",
  "source_line_start": 263,
  "source_line_end": 265,
  "registry_ids": [
    "IV.P183"
  ],
  "related_registry_items": [
    {
      "id": "IV.P183",
      "title": "Sign of p-n splitting: QCD > EM",
      "url": "/registry/object/IV.P183/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/NucleonMassSplitting.lean#L263-L265",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/NucleonMassSplitting.lean#L263-L265",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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
- Source path: [`TauLib/BookIV/Physics/NucleonMassSplitting.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/NucleonMassSplitting.lean#L263-L265)
- Source range: L263-L265
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.P183` — Sign of p-n splitting: QCD > EM

## Immediate Comment / Docstring

```lean
/-- [IV.P183] QCD contribution exceeds EM: sign is correct (neutron heavier).
    Cross-multiplied: qcd_numer · em_denom > em_numer · qcd_denom.
    Numerically: QCD ≈ 1.504e-3 > EM ≈ 1.275e-4. -/
```

## Source Excerpt

```lean
theorem pn_sign_positive : qcd_numer * em_denom > em_numer * qcd_denom := by
  rw [qcd_numer_val, em_denom_val, em_numer_val, qcd_denom_val]
  native_decide
```
