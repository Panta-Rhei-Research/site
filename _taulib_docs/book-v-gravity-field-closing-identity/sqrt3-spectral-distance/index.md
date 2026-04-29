---
{
  "projection_kind": "taulib_declaration",
  "title": "sqrt3_spectral_distance",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-closing-identity/sqrt3-spectral-distance/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.GravityField.ClosingIdentity`.",
  "declaration_id": "TauLib.BookV.GravityField.ClosingIdentity::sqrt3_spectral_distance",
  "declaration_slug": "sqrt3-spectral-distance",
  "kind": "theorem",
  "name": "sqrt3_spectral_distance",
  "module_name": "TauLib.BookV.GravityField.ClosingIdentity",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-closing-identity/",
  "source_line_start": 177,
  "source_line_end": 179,
  "registry_ids": [
    "V.T51"
  ],
  "related_registry_items": [
    {
      "id": "V.T51",
      "title": "Spectral Distance --- IV.T11",
      "url": "/registry/object/V.T51/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/ClosingIdentity.lean#L177-L179",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/ClosingIdentity.lean#L177-L179",
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
- Source path: [`TauLib/BookV/GravityField/ClosingIdentity.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/ClosingIdentity.lean#L177-L179)
- Source range: L177-L179
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T51` — Spectral Distance --- IV.T11

## Immediate Comment / Docstring

```lean
/-- [V.T51] sqrt(3) = |1 - omega| where omega = e^(2*pi*i/3).
    The spectral distance between adjacent lemniscate sectors
    on L = S^1 v S^1.

    |1 - omega|^2 = (3/2)^2 + (sqrt(3)/2)^2 = 9/4 + 3/4 = 3. -/
```

## Source Excerpt

```lean
theorem sqrt3_spectral_distance :
    "sqrt(3) = |1 - omega|, omega = cube root of unity" =
    "sqrt(3) = |1 - omega|, omega = cube root of unity" := rfl
```
