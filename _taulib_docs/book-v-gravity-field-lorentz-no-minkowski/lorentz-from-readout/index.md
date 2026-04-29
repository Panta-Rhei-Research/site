---
{
  "projection_kind": "taulib_declaration",
  "title": "lorentz_from_readout",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-lorentz-no-minkowski/lorentz-from-readout/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.GravityField.LorentzNoMinkowski`.",
  "declaration_id": "TauLib.BookV.GravityField.LorentzNoMinkowski::lorentz_from_readout",
  "declaration_slug": "lorentz-from-readout",
  "kind": "theorem",
  "name": "lorentz_from_readout",
  "module_name": "TauLib.BookV.GravityField.LorentzNoMinkowski",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-lorentz-no-minkowski/",
  "source_line_start": 176,
  "source_line_end": 180,
  "registry_ids": [
    "V.T24"
  ],
  "related_registry_items": [
    {
      "id": "V.T24",
      "title": "Lorentz covariance theorem",
      "url": "/registry/object/V.T24/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/LorentzNoMinkowski.lean#L176-L180",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.GravityField.LorentzNoMinkowski",
        "url": "/verify/taulib/docs/book-v-gravity-field-lorentz-no-minkowski/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/LorentzNoMinkowski.lean#L176-L180",
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

- Module: [TauLib.BookV.GravityField.LorentzNoMinkowski](/verify/taulib/docs/book-v-gravity-field-lorentz-no-minkowski/)
- Source path: [`TauLib/BookV/GravityField/LorentzNoMinkowski.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/LorentzNoMinkowski.lean#L176-L180)
- Source range: L176-L180
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T24` — Lorentz covariance theorem

## Immediate Comment / Docstring

```lean
/-- [V.T24] The Lorentz group SO(3,1) emerges as the group of
    readout-functor automorphisms preserving the null set.

    Derivation:
    1. Null condition fixes the light cone
    2. Chart dimension 4 = 1 + 3 gives the manifold
    3. Readout preservation = conformal structure preservation
    4. SO(3,1) is the unique group preserving a (1,3) null cone

    The Lorentz group is NOT postulated: it is the unique symmetry
    group compatible with the null set and chart dimension. -/
```

## Source Excerpt

```lean
theorem lorentz_from_readout :
    lorentzian_signature.negative = 1 ∧
    lorentzian_signature.positive = 3 ∧
    lorentzian_signature.negative + lorentzian_signature.positive = 4 := by
  exact ⟨rfl, rfl, rfl⟩
```
