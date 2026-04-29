---
{
  "projection_kind": "taulib_declaration",
  "title": "IndividualNeutrinoMasses",
  "permalink": "/verify/taulib/docs/book-v-cosmology-neutrino-background/individual-neutrino-masses/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.NeutrinoBackground`.",
  "declaration_id": "TauLib.BookV.Cosmology.NeutrinoBackground::IndividualNeutrinoMasses",
  "declaration_slug": "individual-neutrino-masses",
  "kind": "structure",
  "name": "IndividualNeutrinoMasses",
  "module_name": "TauLib.BookV.Cosmology.NeutrinoBackground",
  "module_url": "/verify/taulib/docs/book-v-cosmology-neutrino-background/",
  "source_line_start": 198,
  "source_line_end": 209,
  "registry_ids": [
    "V.D333"
  ],
  "related_registry_items": [
    {
      "id": "V.D333",
      "title": "Individual Neutrino Mass Table",
      "url": "/registry/object/V.D333/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/NeutrinoBackground.lean#L198-L209",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.NeutrinoBackground",
        "url": "/verify/taulib/docs/book-v-cosmology-neutrino-background/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/NeutrinoBackground.lean#L198-L209",
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

- Module: [TauLib.BookV.Cosmology.NeutrinoBackground](/verify/taulib/docs/book-v-cosmology-neutrino-background/)
- Source path: [`TauLib/BookV/Cosmology/NeutrinoBackground.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/NeutrinoBackground.lean#L198-L209)
- Source range: L198-L209
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D333` — Individual Neutrino Mass Table

## Immediate Comment / Docstring

```lean
/-- [V.D333] Individual neutrino masses from NNLO exponents.
    m₁ ≈ 6.94 meV, m₂ ≈ 22.68 meV, m₃ ≈ 59.40 meV.
    Sum = 89.02 meV ≈ 0.089 eV at +7.4 ppm. -/
```

## Source Excerpt

```lean
structure IndividualNeutrinoMasses where
  /-- m₁ in meV. -/
  m1_meV : Float := 6.94
  /-- m₂ in meV. -/
  m2_meV : Float := 22.68
  /-- m₃ in meV. -/
  m3_meV : Float := 59.40
  /-- Sum in meV. -/
  sum_meV : Float := 89.02
  /-- Hierarchy ratio m₃/m₁. -/
  hierarchy_ratio : Float := 8.56
  deriving Repr
```
