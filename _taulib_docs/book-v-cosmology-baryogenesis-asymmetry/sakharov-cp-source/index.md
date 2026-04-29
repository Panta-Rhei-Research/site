---
{
  "projection_kind": "taulib_declaration",
  "title": "sakharov_cp_source",
  "permalink": "/verify/taulib/docs/book-v-cosmology-baryogenesis-asymmetry/sakharov-cp-source/",
  "summary_short": "`def` declaration in `TauLib.BookV.Cosmology.BaryogenesisAsymmetry`.",
  "declaration_id": "TauLib.BookV.Cosmology.BaryogenesisAsymmetry::sakharov_cp_source",
  "declaration_slug": "sakharov-cp-source",
  "kind": "def",
  "name": "sakharov_cp_source",
  "module_name": "TauLib.BookV.Cosmology.BaryogenesisAsymmetry",
  "module_url": "/verify/taulib/docs/book-v-cosmology-baryogenesis-asymmetry/",
  "source_line_start": 164,
  "source_line_end": 169,
  "registry_ids": [
    "V.P126"
  ],
  "related_registry_items": [
    {
      "id": "V.P126",
      "title": "Sakharov CP Source: A-Sector Balanced Polarity via Parity Bridge",
      "url": "/registry/object/V.P126/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean#L164-L169",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.BaryogenesisAsymmetry",
        "url": "/verify/taulib/docs/book-v-cosmology-baryogenesis-asymmetry/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean#L164-L169",
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

- Module: [TauLib.BookV.Cosmology.BaryogenesisAsymmetry](/verify/taulib/docs/book-v-cosmology-baryogenesis-asymmetry/)
- Source path: [`TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean#L164-L169)
- Source range: L164-L169
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `V.P126` — Sakharov CP Source: A-Sector Balanced Polarity via Parity Bridge

## Immediate Comment / Docstring

```lean
/-- All three Sakharov conditions are structurally met in τ. [V.P126]

    1. B-violation: baryogenesis window [L_B, L_N] (V.D198, pre-confinement)
    2. CP violation: A-sector balanced polarity κ(A;1) = ι_τ (this proposition)
    3. Out-of-equilibrium: directed α-orbit (V.T06)

    The CP asymmetry scale is ι_τ. The baryon suppression relative to
    this scale is η_B/ι_τ = α·ι_τ¹⁴·(5/6) ≈ 1.770 × 10⁻⁹. -/
```

## Source Excerpt

```lean
def sakharov_cp_source : String :=
  "Sakharov conditions all structural in τ: " ++
  "(1) B-violation: baryogenesis window [L_B,L_N], depth 2–3 (V.D198). " ++
  "(2) CP violation: A-sector balanced polarity κ(A;1)=ι_τ, parity bridge III.T07. " ++
  "(3) Out-of-equilibrium: directed α-orbit (V.T06), cooling monotone. " ++
  "Suppression: η_B/ι_τ = α·ι_τ¹⁴·(5/6) ≈ 1.770×10⁻⁹."
```
