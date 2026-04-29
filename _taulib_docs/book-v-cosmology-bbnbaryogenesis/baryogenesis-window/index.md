---
{
  "projection_kind": "taulib_declaration",
  "title": "BaryogenesisWindow",
  "permalink": "/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/baryogenesis-window/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.BBNBaryogenesis`.",
  "declaration_id": "TauLib.BookV.Cosmology.BBNBaryogenesis::BaryogenesisWindow",
  "declaration_slug": "baryogenesis-window",
  "kind": "structure",
  "name": "BaryogenesisWindow",
  "module_name": "TauLib.BookV.Cosmology.BBNBaryogenesis",
  "module_url": "/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/",
  "source_line_start": 116,
  "source_line_end": 125,
  "registry_ids": [
    "V.D198"
  ],
  "related_registry_items": [
    {
      "id": "V.D198",
      "title": "Baryogenesis Window",
      "url": "/registry/object/V.D198/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BBNBaryogenesis.lean#L116-L125",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.BBNBaryogenesis",
        "url": "/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BBNBaryogenesis.lean#L116-L125",
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

- Module: [TauLib.BookV.Cosmology.BBNBaryogenesis](/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/)
- Source path: [`TauLib/BookV/Cosmology/BBNBaryogenesis.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BBNBaryogenesis.lean#L116-L125)
- Source range: L116-L125
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D198` — Baryogenesis Window

## Immediate Comment / Docstring

```lean
/-- [V.D198] Baryogenesis window: the finite interval [L_B, L_N]
    (depths 2–3) during which baryon number violation is structurally
    permitted. The window opens at the baryogenesis threshold (depth 2)
    and closes at the neutron threshold (depth 3) when SA-i locks in.

    Below L_N, baryon number is absolutely conserved. -/
```

## Source Excerpt

```lean
structure BaryogenesisWindow where
  /-- Start depth (baryogenesis threshold L_B). -/
  depth_start : Nat := 2
  /-- End depth (neutron threshold L_N). -/
  depth_end : Nat := 3
  /-- Window is non-empty: start < end. -/
  window_nonempty : depth_start < depth_end
  /-- Start is positive. -/
  start_pos : depth_start > 0
  deriving Repr
```
