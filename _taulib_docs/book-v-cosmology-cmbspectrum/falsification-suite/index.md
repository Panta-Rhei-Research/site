---
{
  "projection_kind": "taulib_declaration",
  "title": "FalsificationSuite",
  "permalink": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/falsification-suite/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.CMBSpectrum`.",
  "declaration_id": "TauLib.BookV.Cosmology.CMBSpectrum::FalsificationSuite",
  "declaration_slug": "falsification-suite",
  "kind": "structure",
  "name": "FalsificationSuite",
  "module_name": "TauLib.BookV.Cosmology.CMBSpectrum",
  "module_url": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/",
  "source_line_start": 327,
  "source_line_end": 334,
  "registry_ids": [
    "V.P138"
  ],
  "related_registry_items": [
    {
      "id": "V.P138",
      "title": "CMB-S4/PTOLEMY/DESI Falsification Suite",
      "url": "/registry/object/V.P138/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L327-L334",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.CMBSpectrum",
        "url": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L327-L334",
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

- Module: [TauLib.BookV.Cosmology.CMBSpectrum](/verify/taulib/docs/book-v-cosmology-cmbspectrum/)
- Source path: [`TauLib/BookV/Cosmology/CMBSpectrum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L327-L334)
- Source range: L327-L334
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.P138` — CMB-S4/PTOLEMY/DESI Falsification Suite

## Immediate Comment / Docstring

```lean
/-- [V.P138] CMB-S4/PTOLEMY/DESI Falsification Suite.
    6 targets: r (14σ), N_eff (1.5σ), Σm_ν (4.5σ), m_β (<1σ),
    Majorana/NH, ΔP/P (3σ). -/
```

## Source Excerpt

```lean
structure FalsificationSuite where
  /-- Number of targets. -/
  n_targets : Nat
  /-- Six targets. -/
  targets_eq : n_targets = 6
  /-- Most falsifiable significance: r at CMB-S4 (~14σ). -/
  most_falsifiable_sigma : Nat := 14
  deriving Repr
```
