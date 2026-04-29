---
{
  "projection_kind": "taulib_declaration",
  "title": "ThermalCoherenceHorizon",
  "permalink": "/verify/taulib/docs/book-v-thermodynamics-inversion/thermal-coherence-horizon/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Thermodynamics.Inversion`.",
  "declaration_id": "TauLib.BookV.Thermodynamics.Inversion::ThermalCoherenceHorizon",
  "declaration_slug": "thermal-coherence-horizon",
  "kind": "structure",
  "name": "ThermalCoherenceHorizon",
  "module_name": "TauLib.BookV.Thermodynamics.Inversion",
  "module_url": "/verify/taulib/docs/book-v-thermodynamics-inversion/",
  "source_line_start": 229,
  "source_line_end": 236,
  "registry_ids": [
    "V.D84"
  ],
  "related_registry_items": [
    {
      "id": "V.D84",
      "title": "Coherence horizon",
      "url": "/registry/object/V.D84/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/Inversion.lean#L229-L236",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Thermodynamics.Inversion",
        "url": "/verify/taulib/docs/book-v-thermodynamics-inversion/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/Inversion.lean#L229-L236",
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

- Module: [TauLib.BookV.Thermodynamics.Inversion](/verify/taulib/docs/book-v-thermodynamics-inversion/)
- Source path: [`TauLib/BookV/Thermodynamics/Inversion.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/Inversion.lean#L229-L236)
- Source range: L229-L236
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D84` — Coherence horizon

## Immediate Comment / Docstring

```lean
/-- [V.D84] Coherence horizon: the orbit depth n_coh at which defect
    entropy first reaches zero. Beyond n_coh, the configuration is
    in categorical equilibrium.

    Existence and finiteness follow from the geometric contraction lemma.
    n_coh is bounded by ceil(ln|D_0| / ln(1/(1-iota_tau))). -/
```

## Source Excerpt

```lean
structure ThermalCoherenceHorizon where
  /-- Initial defect count |D_0|. -/
  initial_defect_count : Nat
  /-- The coherence horizon (orbit steps). -/
  n_coh : Nat
  /-- n_coh is positive when there are initial defects. -/
  positive_when_defects : initial_defect_count > 0 → n_coh > 0
  deriving Repr
```
