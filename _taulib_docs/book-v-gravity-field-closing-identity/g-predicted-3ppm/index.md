---
{
  "projection_kind": "taulib_declaration",
  "title": "g_predicted_3ppm",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-closing-identity/g-predicted-3ppm/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.GravityField.ClosingIdentity`.",
  "declaration_id": "TauLib.BookV.GravityField.ClosingIdentity::g_predicted_3ppm",
  "declaration_slug": "g-predicted-3ppm",
  "kind": "theorem",
  "name": "g_predicted_3ppm",
  "module_name": "TauLib.BookV.GravityField.ClosingIdentity",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-closing-identity/",
  "source_line_start": 191,
  "source_line_end": 193,
  "registry_ids": [
    "V.T52"
  ],
  "related_registry_items": [
    {
      "id": "V.T52",
      "title": "G Prediction --- V.T04, V.T05",
      "url": "/registry/object/V.T52/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/ClosingIdentity.lean#L191-L193",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.GravityField.ClosingIdentity",
        "url": "/verify/taulib/docs/book-v-gravity-field-closing-identity/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/ClosingIdentity.lean#L191-L193",
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

- Module: [TauLib.BookV.GravityField.ClosingIdentity](/verify/taulib/docs/book-v-gravity-field-closing-identity/)
- Source path: [`TauLib/BookV/GravityField/ClosingIdentity.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/ClosingIdentity.lean#L191-L193)
- Source range: L191-L193
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T52` — G Prediction --- V.T04, V.T05

## Immediate Comment / Docstring

```lean
/-- [V.T52] G predicted to 3 ppm of CODATA.

    With c1 = 3/pi, the closing identity gives:
    G_predicted / G_CODATA = 1.000003 (3 ppm)

    This is within the CODATA measurement uncertainty of G
    (~ 22 ppm), so the prediction is effectively exact.

    Verification: |c1(3/pi) - c1(target)| < 0.05%.
    (Proved in CoRotorCoupling.lean as c1_matches_three_over_pi.) -/
```

## Source Excerpt

```lean
theorem g_predicted_3ppm :
    c1_three_over_pi_numer < c1_target_numer + 5000 :=
  (c1_matches_three_over_pi).1
```
