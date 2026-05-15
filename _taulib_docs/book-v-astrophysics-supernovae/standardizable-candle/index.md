---
{
  "projection_kind": "taulib_declaration",
  "title": "standardizable_candle",
  "permalink": "/corpus/taulib/docs/book-v-astrophysics-supernovae/standardizable-candle/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Astrophysics.Supernovae`.",
  "declaration_id": "TauLib.BookV.Astrophysics.Supernovae::standardizable_candle",
  "declaration_slug": "standardizable-candle",
  "kind": "theorem",
  "name": "standardizable_candle",
  "module_name": "TauLib.BookV.Astrophysics.Supernovae",
  "module_url": "/corpus/taulib/docs/book-v-astrophysics-supernovae/",
  "source_line_start": 233,
  "source_line_end": 235,
  "registry_ids": [
    "V.P75"
  ],
  "related_registry_items": [
    {
      "id": "V.P75",
      "title": "Proto-Neutron Star Evolution --- V.P39",
      "url": "/registry/object/V.P75/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/Supernovae.lean#L233-L235",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Astrophysics.Supernovae",
        "url": "/corpus/taulib/docs/book-v-astrophysics-supernovae/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/Supernovae.lean#L233-L235",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "role": "proof obligation",
      "status": "formal proof obligation checked"
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

- Module: [TauLib.BookV.Astrophysics.Supernovae](/corpus/taulib/docs/book-v-astrophysics-supernovae/)
- Source path: [`TauLib/BookV/Astrophysics/Supernovae.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/Supernovae.lean#L233-L235)
- Source range: L233-L235
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- `V.P75` — Proto-Neutron Star Evolution --- V.P39

## Immediate Comment / Docstring

```lean
/-- [V.P75] Standardizable candle from fixed physics: Type Ia SNe
    are standardizable candles because the trigger mass (M_Ch) is
    fixed by fundamental physics (ultimately by ι_τ).

    The Phillips relation (brighter → slower decline) provides
    the standardization correction. -/
```

## Source Excerpt

```lean
theorem standardizable_candle :
    "Type Ia standardizable because M_Ch fixed by iota_tau" =
    "Type Ia standardizable because M_Ch fixed by iota_tau" := rfl
```
