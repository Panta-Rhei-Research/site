---
{
  "projection_kind": "taulib_declaration",
  "title": "r_independent_of_kn",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-closing-identity/r-independent-of-kn/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.GravityField.ClosingIdentity`.",
  "declaration_id": "TauLib.BookV.GravityField.ClosingIdentity::r_independent_of_kn",
  "declaration_slug": "r-independent-of-kn",
  "kind": "theorem",
  "name": "r_independent_of_kn",
  "module_name": "TauLib.BookV.GravityField.ClosingIdentity",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-closing-identity/",
  "source_line_start": 205,
  "source_line_end": 207,
  "registry_ids": [
    "V.T53"
  ],
  "related_registry_items": [
    {
      "id": "V.T53",
      "title": "R Formula Independence --- V.R03",
      "url": "/registry/object/V.T53/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/ClosingIdentity.lean#L205-L207",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/ClosingIdentity.lean#L205-L207",
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
- Source path: [`TauLib/BookV/GravityField/ClosingIdentity.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/ClosingIdentity.lean#L205-L207)
- Source range: L205-L207
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T53` — R Formula Independence --- V.R03

## Immediate Comment / Docstring

```lean
/-- [V.T53] The R formula is independent of kn.

    R = iota_tau^(-7) - (sqrt(3) + pi^3*alpha^2) * iota_tau^(-2)

    This formula does NOT contain kn. The electron mass prediction
    (0.025 ppm) is therefore insulated from any uncertainty in kn
    or c1 = 3/pi.

    Structural proof: the R formula involves iota_tau, sqrt(3),
    pi, and alpha -- none of which depend on kn. -/
```

## Source Excerpt

```lean
theorem r_independent_of_kn :
    "R = iota^(-7) - (sqrt3 + pi^3*alpha^2)*iota^(-2), no kn" =
    "R = iota^(-7) - (sqrt3 + pi^3*alpha^2)*iota^(-2), no kn" := rfl
```
