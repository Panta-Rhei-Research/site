---
{
  "projection_kind": "taulib_declaration",
  "title": "EHTObservableData",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-ehtreread/ehtobservable-data/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Astrophysics.EHTReread`.",
  "declaration_id": "TauLib.BookV.Astrophysics.EHTReread::EHTObservableData",
  "declaration_slug": "ehtobservable-data",
  "kind": "structure",
  "name": "EHTObservableData",
  "module_name": "TauLib.BookV.Astrophysics.EHTReread",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-ehtreread/",
  "source_line_start": 146,
  "source_line_end": 157,
  "registry_ids": [
    "V.D138"
  ],
  "related_registry_items": [
    {
      "id": "V.D138",
      "title": "Photon Ring Winding Number",
      "url": "/registry/object/V.D138/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/EHTReread.lean#L146-L157",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/EHTReread.lean#L146-L157",
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
- Source path: [`TauLib/BookV/Astrophysics/EHTReread.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/EHTReread.lean#L146-L157)
- Source range: L146-L157
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D138` — Photon Ring Winding Number

## Immediate Comment / Docstring

```lean
/-- [V.D138] EHT observable data: the quantities measurable by the
    Event Horizon Telescope for a given BH target. -/
```

## Source Excerpt

```lean
structure EHTObservableData where
  /-- Target name. -/
  target : String
  /-- Shadow angular diameter (μas). -/
  shadow_diameter_uas : Nat
  /-- Shadow circularity (1.0 = perfect circle, scaled × 100). -/
  circularity_scaled : Nat
  /-- Photon ring brightness ratio (n=1 to n=0, percent). -/
  ring_ratio_pct : Nat
  /-- Whether the shadow is resolved. -/
  is_resolved : Bool := true
  deriving Repr
```
