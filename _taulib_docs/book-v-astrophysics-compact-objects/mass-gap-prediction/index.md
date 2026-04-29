---
{
  "projection_kind": "taulib_declaration",
  "title": "mass_gap_prediction",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-compact-objects/mass-gap-prediction/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Astrophysics.CompactObjects`.",
  "declaration_id": "TauLib.BookV.Astrophysics.CompactObjects::mass_gap_prediction",
  "declaration_slug": "mass-gap-prediction",
  "kind": "theorem",
  "name": "mass_gap_prediction",
  "module_name": "TauLib.BookV.Astrophysics.CompactObjects",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-compact-objects/",
  "source_line_start": 201,
  "source_line_end": 202,
  "registry_ids": [
    "V.T88"
  ],
  "related_registry_items": [
    {
      "id": "V.T88",
      "title": "Compact-Object Classification --- V.T40",
      "url": "/registry/object/V.T88/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/CompactObjects.lean#L201-L202",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Astrophysics.CompactObjects",
        "url": "/verify/taulib/docs/book-v-astrophysics-compact-objects/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/CompactObjects.lean#L201-L202",
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

- Module: [TauLib.BookV.Astrophysics.CompactObjects](/verify/taulib/docs/book-v-astrophysics-compact-objects/)
- Source path: [`TauLib/BookV/Astrophysics/CompactObjects.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/CompactObjects.lean#L201-L202)
- Source range: L201-L202
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T88` — Compact-Object Classification --- V.T40

## Immediate Comment / Docstring

```lean
/-- [V.T88] Mass gap prediction: the τ-framework predicts a mass gap
    between the maximum NS mass (~2.5 M_☉) and the minimum BH mass
    (~5 M_☉).

    The gap arises because the topology crossing (S² → T²) has a
    finite defect cost barrier. The system cannot continuously
    transition but must jump, creating a gap in the compact-object
    mass spectrum.

    This prediction is testable via gravitational wave observations
    of merger remnants. -/
```

## Source Excerpt

```lean
theorem mass_gap_prediction :
    mass_gap_lower < mass_gap_upper := by native_decide
```
