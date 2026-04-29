---
{
  "projection_kind": "taulib_declaration",
  "title": "bianchi_from_einstein",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-tau-einstein-eq/bianchi-from-einstein/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.GravityField.TauEinsteinEq`.",
  "declaration_id": "TauLib.BookV.GravityField.TauEinsteinEq::bianchi_from_einstein",
  "declaration_slug": "bianchi-from-einstein",
  "kind": "theorem",
  "name": "bianchi_from_einstein",
  "module_name": "TauLib.BookV.GravityField.TauEinsteinEq",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-tau-einstein-eq/",
  "source_line_start": 191,
  "source_line_end": 194,
  "registry_ids": [
    "V.C03"
  ],
  "related_registry_items": [
    {
      "id": "V.C03",
      "title": "tau-Bianchi identity --- V.R01",
      "url": "/registry/object/V.C03/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TauEinsteinEq.lean#L191-L194",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.GravityField.TauEinsteinEq",
        "url": "/verify/taulib/docs/book-v-gravity-field-tau-einstein-eq/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TauEinsteinEq.lean#L191-L194",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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

- Module: [TauLib.BookV.GravityField.TauEinsteinEq](/verify/taulib/docs/book-v-gravity-field-tau-einstein-eq/)
- Source path: [`TauLib/BookV/GravityField/TauEinsteinEq.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TauEinsteinEq.lean#L191-L194)
- Source range: L191-L194
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.C03` — tau-Bianchi identity --- V.R01

## Immediate Comment / Docstring

```lean
/-- [V.C03] τ-Bianchi identity: conservation follows from the
    τ-Einstein equation as a COROLLARY.

    ∇ · R^H = ∇ · (κ_τ · T^mat) = 0

    No admissible refinement can change matter-character without
    compensating curvature change. Backreaction is automatic.

    Unlike orthodox GR where ∇_μ G^μν = 0 is an independent identity,
    in the τ-framework conservation is derived from the algebraic
    structure of H_∂[n]. -/
```

## Source Excerpt

```lean
theorem bianchi_from_einstein (e : TauEinsteinField) :
    e.curvature.defect_numer * e.kappa.kappa_denom * e.matter.denom =
    e.kappa.kappa_numer * e.matter.total_numer * e.curvature.defect_denom :=
  e.einstein_identity
```
