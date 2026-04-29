---
{
  "projection_kind": "taulib_declaration",
  "title": "t2_shadow_correction_factor",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-ehtreread/t2-shadow-correction-factor/",
  "summary_short": "`def` declaration in `TauLib.BookV.Astrophysics.EHTReread`.",
  "declaration_id": "TauLib.BookV.Astrophysics.EHTReread::t2_shadow_correction_factor",
  "declaration_slug": "t2-shadow-correction-factor",
  "kind": "def",
  "name": "t2_shadow_correction_factor",
  "module_name": "TauLib.BookV.Astrophysics.EHTReread",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-ehtreread/",
  "source_line_start": 259,
  "source_line_end": 259,
  "registry_ids": [
    "V.D241"
  ],
  "related_registry_items": [
    {
      "id": "V.D241",
      "title": "T² Quadrupole Shadow Correction Factor: f = 1 + ι_τ²/4",
      "url": "/registry/object/V.D241/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/EHTReread.lean#L259-L259",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Astrophysics.EHTReread",
        "url": "/verify/taulib/docs/book-v-astrophysics-ehtreread/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/EHTReread.lean#L259-L259",
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

- Module: [TauLib.BookV.Astrophysics.EHTReread](/verify/taulib/docs/book-v-astrophysics-ehtreread/)
- Source path: [`TauLib/BookV/Astrophysics/EHTReread.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/EHTReread.lean#L259-L259)
- Source range: L259-L259
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `V.D241` — T² Quadrupole Shadow Correction Factor: f = 1 + ι_τ²/4

## Immediate Comment / Docstring

```lean
/-- [V.D241] T² Quadrupole Shadow Correction Factor.
    f(ι_τ) = 1+ι_τ²/4 = 1.02912. Shadow radius enlarged by 2.91% over GR S². -/
```

## Source Excerpt

```lean
def t2_shadow_correction_factor : Float := 1.0 + iota_float * iota_float / 4.0
```
