---
{
  "projection_kind": "taulib_declaration",
  "title": "em_numer",
  "permalink": "/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/em-numer/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Physics.NucleonMassSplitting`.",
  "declaration_id": "TauLib.BookIV.Physics.NucleonMassSplitting::em_numer",
  "declaration_slug": "em-numer",
  "kind": "def",
  "name": "em_numer",
  "module_name": "TauLib.BookIV.Physics.NucleonMassSplitting",
  "module_url": "/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/",
  "source_line_start": 176,
  "source_line_end": 176,
  "registry_ids": [
    "IV.D342"
  ],
  "related_registry_items": [
    {
      "id": "IV.D342",
      "title": "EM Coulomb Contribution to p-n splitting",
      "url": "/registry/object/IV.D342/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/NucleonMassSplitting.lean#L176-L176",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Physics.NucleonMassSplitting",
        "url": "/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/NucleonMassSplitting.lean#L176-L176",
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

- Module: [TauLib.BookIV.Physics.NucleonMassSplitting](/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/)
- Source path: [`TauLib/BookIV/Physics/NucleonMassSplitting.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/NucleonMassSplitting.lean#L176-L176)
- Source range: L176-L176
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `IV.D342` — EM Coulomb Contribution to p-n splitting

## Immediate Comment / Docstring

```lean
/-- [IV.D342] EM contribution numerator: 363 · ι_τ⁶_numer.
    363 = 3 × 121 = N_c × α_tower_coeff_numer -/
```

## Source Excerpt

```lean
def em_numer : Nat := 363 * iota6_numer
```
