---
{
  "projection_kind": "taulib_declaration",
  "title": "canonical_measurement_dissolution",
  "permalink": "/verify/taulib/docs/book-v-orthodox-measurement-unification/canonical-measurement-dissolution/",
  "summary_short": "`def` declaration in `TauLib.BookV.Orthodox.MeasurementUnification`.",
  "declaration_id": "TauLib.BookV.Orthodox.MeasurementUnification::canonical_measurement_dissolution",
  "declaration_slug": "canonical-measurement-dissolution",
  "kind": "def",
  "name": "canonical_measurement_dissolution",
  "module_name": "TauLib.BookV.Orthodox.MeasurementUnification",
  "module_url": "/verify/taulib/docs/book-v-orthodox-measurement-unification/",
  "source_line_start": 131,
  "source_line_end": 132,
  "registry_ids": [
    "V.T134"
  ],
  "related_registry_items": [
    {
      "id": "V.T134",
      "title": "Measurement problem dissolution",
      "url": "/registry/object/V.T134/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/MeasurementUnification.lean#L131-L132",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Orthodox.MeasurementUnification",
        "url": "/verify/taulib/docs/book-v-orthodox-measurement-unification/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/MeasurementUnification.lean#L131-L132",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
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

- Module: [TauLib.BookV.Orthodox.MeasurementUnification](/verify/taulib/docs/book-v-orthodox-measurement-unification/)
- Source path: [`TauLib/BookV/Orthodox/MeasurementUnification.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/MeasurementUnification.lean#L131-L132)
- Source range: L131-L132
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `V.T134` — Measurement problem dissolution

## Immediate Comment / Docstring

```lean
/-- [V.T134] The measurement problem is dissolved.

    There is no wavefunction collapse in the ontic layer. There is
    address resolution in H_partial[omega], which the VM readout
    functor describes as "collapse."

    Formally:
    - Read(rho^n(chi)) = U^n |psi_chi>  (unitary evolution)
    - Read(resolve(chi)) = P_a |psi_chi> / ||P_a|psi_chi>||
      (address resolution -> "collapse" in VM)

    The Born rule |<a|psi>|^2 is the Pythagorean theorem: the
    squared projection of one boundary character onto another. -/
```

## Source Excerpt

```lean
def canonical_measurement_dissolution : MeasurementDissolution where
  unitary_is_readout := true
```
