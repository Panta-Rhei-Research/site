---
{
  "projection_kind": "taulib_declaration",
  "title": "TauHorizonDef",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-ehtreread/tau-horizon-def/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Astrophysics.EHTReread`.",
  "declaration_id": "TauLib.BookV.Astrophysics.EHTReread::TauHorizonDef",
  "declaration_slug": "tau-horizon-def",
  "kind": "structure",
  "name": "TauHorizonDef",
  "module_name": "TauLib.BookV.Astrophysics.EHTReread",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-ehtreread/",
  "source_line_start": 84,
  "source_line_end": 97,
  "registry_ids": [
    "V.D137"
  ],
  "related_registry_items": [
    {
      "id": "V.D137",
      "title": "Toroidal Shadow (T^2 Readout)",
      "url": "/registry/object/V.D137/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/EHTReread.lean#L84-L97",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/EHTReread.lean#L84-L97",
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
- Source path: [`TauLib/BookV/Astrophysics/EHTReread.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/EHTReread.lean#L84-L97)
- Source range: L84-L97
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D137` — Toroidal Shadow (T^2 Readout)

## Immediate Comment / Docstring

```lean
/-- [V.D137] Tau horizon definition: the τ-horizon is the topology
    crossing boundary where the defect-bundle topology transitions
    from S² (stellar surface) to T² (torus vacuum).

    Unlike the GR event horizon:
    - It is a PHYSICAL boundary (topology change), not a coordinate artifact
    - It preserves information (boundary characters are continuous)
    - It has finite local physics (no singularity) -/
```

## Source Excerpt

```lean
structure TauHorizonDef where
  /-- Mass of the BH (tenths of solar mass). -/
  mass_tenth_solar : Nat
  /-- Mass positive. -/
  mass_pos : mass_tenth_solar > 0
  /-- Horizon radius (Schwarzschild radii, scaled × 100). -/
  horizon_radius_scaled : Nat
  /-- Horizon type. -/
  horizon_type : HorizonType := .TauHorizon
  /-- Whether information is preserved. -/
  information_preserved : Bool := true
  /-- Whether a singularity exists. -/
  has_singularity : Bool := false
  deriving Repr
```
