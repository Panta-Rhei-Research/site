---
{
  "projection_kind": "taulib_declaration",
  "title": "DefectAbsorptionRate",
  "permalink": "/verify/taulib/docs/book-v-thermodynamics-inversion/defect-absorption-rate/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Thermodynamics.Inversion`.",
  "declaration_id": "TauLib.BookV.Thermodynamics.Inversion::DefectAbsorptionRate",
  "declaration_slug": "defect-absorption-rate",
  "kind": "structure",
  "name": "DefectAbsorptionRate",
  "module_name": "TauLib.BookV.Thermodynamics.Inversion",
  "module_url": "/verify/taulib/docs/book-v-thermodynamics-inversion/",
  "source_line_start": 140,
  "source_line_end": 149,
  "registry_ids": [
    "V.P24"
  ],
  "related_registry_items": [
    {
      "id": "V.P24",
      "title": "Defect absorption rate",
      "url": "/registry/object/V.P24/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/Inversion.lean#L140-L149",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/Inversion.lean#L140-L149",
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
- Source path: [`TauLib/BookV/Thermodynamics/Inversion.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/Inversion.lean#L140-L149)
- Source range: L140-L149
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.P24` — Defect absorption rate

## Immediate Comment / Docstring

```lean
/-- [V.P24] Defect absorption rate: at orbit depth n+1, the kernel
    condition reduces defect support by at least the gravitational
    self-coupling factor:

    |supp(d_{n+1})| <= (1 - iota_tau) |supp(d_n)|

    where (1 - iota_tau) = kappa(D;1) is the D-sector self-coupling.
    Gravity is the primary ordering mechanism. -/
```

## Source Excerpt

```lean
structure DefectAbsorptionRate where
  /-- Initial defect count at orbit depth n. -/
  defect_count_n : Nat
  /-- Defect count at orbit depth n+1. -/
  defect_count_n1 : Nat
  /-- The contraction bound holds (scaled to avoid rationals):
      defect_count_n1 * contraction_denom <= contraction_numer * defect_count_n. -/
  contraction_bound : defect_count_n1 * contraction_denom
                      ≤ contraction_numer * defect_count_n
  deriving Repr
```
