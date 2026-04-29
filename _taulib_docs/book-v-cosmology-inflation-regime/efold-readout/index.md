---
{
  "projection_kind": "taulib_declaration",
  "title": "EFoldReadout",
  "permalink": "/verify/taulib/docs/book-v-cosmology-inflation-regime/efold-readout/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.InflationRegime`.",
  "declaration_id": "TauLib.BookV.Cosmology.InflationRegime::EFoldReadout",
  "declaration_slug": "efold-readout",
  "kind": "structure",
  "name": "EFoldReadout",
  "module_name": "TauLib.BookV.Cosmology.InflationRegime",
  "module_url": "/verify/taulib/docs/book-v-cosmology-inflation-regime/",
  "source_line_start": 161,
  "source_line_end": 166,
  "registry_ids": [
    "V.D157"
  ],
  "related_registry_items": [
    {
      "id": "V.D157",
      "title": "e-Fold Readout",
      "url": "/registry/object/V.D157/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/InflationRegime.lean#L161-L166",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.InflationRegime",
        "url": "/verify/taulib/docs/book-v-cosmology-inflation-regime/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/InflationRegime.lean#L161-L166",
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

- Module: [TauLib.BookV.Cosmology.InflationRegime](/verify/taulib/docs/book-v-cosmology-inflation-regime/)
- Source path: [`TauLib/BookV/Cosmology/InflationRegime.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/InflationRegime.lean#L161-L166)
- Source range: L161-L166
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D157` — e-Fold Readout

## Immediate Comment / Docstring

```lean
/-- [V.D157] e-fold readout N_e: the total number of e-folds
    accumulated during the inflationary regime.

    N_e = Σ_{n ∈ R_inf} ln(a_{n+1}/a_n), where a_n is the
    chart-level scale factor readout at tick n.

    In the τ-framework, N_e ≈ 60 follows from the refinement
    tower structure, not from inflaton potential fine-tuning. -/
```

## Source Excerpt

```lean
structure EFoldReadout where
  /-- Number of e-folds (scaled by 10 for rational encoding). -/
  efolds_times_10 : Nat
  /-- At least 500 (i.e., N_e ≥ 50). -/
  sufficient : efolds_times_10 ≥ 500
  deriving Repr
```
