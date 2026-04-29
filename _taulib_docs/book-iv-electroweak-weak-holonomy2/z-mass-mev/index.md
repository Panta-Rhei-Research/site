---
{
  "projection_kind": "taulib_declaration",
  "title": "z_mass_mev",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-weak-holonomy2/z-mass-mev/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Electroweak.WeakHolonomy2`.",
  "declaration_id": "TauLib.BookIV.Electroweak.WeakHolonomy2::z_mass_mev",
  "declaration_slug": "z-mass-mev",
  "kind": "def",
  "name": "z_mass_mev",
  "module_name": "TauLib.BookIV.Electroweak.WeakHolonomy2",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-weak-holonomy2/",
  "source_line_start": 68,
  "source_line_end": 69,
  "registry_ids": [
    "IV.D122"
  ],
  "related_registry_items": [
    {
      "id": "IV.D122",
      "title": "Z Boson Parameters",
      "url": "/registry/object/IV.D122/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakHolonomy2.lean#L68-L69",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.WeakHolonomy2",
        "url": "/verify/taulib/docs/book-iv-electroweak-weak-holonomy2/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakHolonomy2.lean#L68-L69",
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

- Module: [TauLib.BookIV.Electroweak.WeakHolonomy2](/verify/taulib/docs/book-iv-electroweak-weak-holonomy2/)
- Source path: [`TauLib/BookIV/Electroweak/WeakHolonomy2.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakHolonomy2.lean#L68-L69)
- Source range: L68-L69
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `IV.D122` — Z Boson Parameters

## Immediate Comment / Docstring

```lean
/-- [IV.D122] Z boson observed mass: M_Z = 91188 MeV (PDG 2022). -/
```

## Source Excerpt

```lean
def z_mass_mev : ObservedMass where
  name := "Z"; mass_numer := 91188; mass_denom := 1; denom_pos := by omega
```
