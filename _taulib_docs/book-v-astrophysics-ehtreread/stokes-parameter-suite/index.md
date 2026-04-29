---
{
  "projection_kind": "taulib_declaration",
  "title": "StokesParameterSuite",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-ehtreread/stokes-parameter-suite/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Astrophysics.EHTReread`.",
  "declaration_id": "TauLib.BookV.Astrophysics.EHTReread::StokesParameterSuite",
  "declaration_slug": "stokes-parameter-suite",
  "kind": "structure",
  "name": "StokesParameterSuite",
  "module_name": "TauLib.BookV.Astrophysics.EHTReread",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-ehtreread/",
  "source_line_start": 550,
  "source_line_end": 566,
  "registry_ids": [
    "V.D287"
  ],
  "related_registry_items": [
    {
      "id": "V.D287",
      "title": "Stokes Parameter Decomposition on T²",
      "url": "/registry/object/V.D287/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/EHTReread.lean#L550-L566",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/EHTReread.lean#L550-L566",
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

- Module: [TauLib.BookV.Astrophysics.EHTReread](/verify/taulib/docs/book-v-astrophysics-ehtreread/)
- Source path: [`TauLib/BookV/Astrophysics/EHTReread.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/EHTReread.lean#L550-L566)
- Source range: L550-L566
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D287` — Stokes Parameter Decomposition on T²

## Immediate Comment / Docstring

```lean
/-- [V.D287] Stokes Parameter Suite on T²: decomposition of polarization
    state into I, Q, U, V components with T² topology. EVPA winding = 2,
    circular polarization winding = 2, both from toroidal field geometry. -/
```

## Source Excerpt

```lean
structure StokesParameterSuite where
  /-- Source name. -/
  source : String
  /-- EVPA winding number. -/
  w_evpa : Nat := 2
  /-- RM winding number. -/
  w_rm : Nat := 2
  /-- Circular polarization winding number. -/
  w_v : Nat := 2
  /-- Linear polarization fraction (percent × 10). -/
  m_linear_x10 : Nat
  /-- Circular polarization |V/I| (percent × 100). -/
  v_over_i_x100 : Nat
  deriving Repr

instance : Inhabited StokesParameterSuite :=
  ⟨⟨"generic", 2, 2, 2, 200, 50⟩⟩
```
