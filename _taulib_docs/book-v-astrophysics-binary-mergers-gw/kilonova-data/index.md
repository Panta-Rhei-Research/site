---
{
  "projection_kind": "taulib_declaration",
  "title": "KilonovaData",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-binary-mergers-gw/kilonova-data/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Astrophysics.BinaryMergersGW`.",
  "declaration_id": "TauLib.BookV.Astrophysics.BinaryMergersGW::KilonovaData",
  "declaration_slug": "kilonova-data",
  "kind": "structure",
  "name": "KilonovaData",
  "module_name": "TauLib.BookV.Astrophysics.BinaryMergersGW",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-binary-mergers-gw/",
  "source_line_start": 206,
  "source_line_end": 217,
  "registry_ids": [
    "V.D136"
  ],
  "related_registry_items": [
    {
      "id": "V.D136",
      "title": "Standard Siren (tau)",
      "url": "/registry/object/V.D136/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/BinaryMergersGW.lean#L206-L217",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Astrophysics.BinaryMergersGW",
        "url": "/verify/taulib/docs/book-v-astrophysics-binary-mergers-gw/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/BinaryMergersGW.lean#L206-L217",
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

- Module: [TauLib.BookV.Astrophysics.BinaryMergersGW](/verify/taulib/docs/book-v-astrophysics-binary-mergers-gw/)
- Source path: [`TauLib/BookV/Astrophysics/BinaryMergersGW.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/BinaryMergersGW.lean#L206-L217)
- Source range: L206-L217
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D136` — Standard Siren (tau)

## Immediate Comment / Docstring

```lean
/-- [V.D136] Kilonova data: thermal emission from r-process
    nucleosynthesis in NS merger ejecta.

    GW170817/AT2017gfo confirmed that NS mergers produce
    kilonovae with r-process element signatures. -/
```

## Source Excerpt

```lean
structure KilonovaData where
  /-- Ejecta mass (10⁻² M_☉, scaled × 100). -/
  ejecta_mass_scaled : Nat
  /-- Ejecta mass positive. -/
  ejecta_pos : ejecta_mass_scaled > 0
  /-- Peak luminosity (10⁴⁰ erg/s, scaled × 10). -/
  peak_luminosity : Nat
  /-- Duration (days). -/
  duration_days : Nat
  /-- Whether lanthanide-rich (red kilonova). -/
  lanthanide_rich : Bool
  deriving Repr
```
