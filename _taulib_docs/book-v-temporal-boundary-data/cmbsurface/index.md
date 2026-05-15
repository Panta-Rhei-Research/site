---
{
  "projection_kind": "taulib_declaration",
  "title": "CMBSurface",
  "permalink": "/corpus/taulib/docs/book-v-temporal-boundary-data/cmbsurface/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Temporal.BoundaryData`.",
  "declaration_id": "TauLib.BookV.Temporal.BoundaryData::CMBSurface",
  "declaration_slug": "cmbsurface",
  "kind": "structure",
  "name": "CMBSurface",
  "module_name": "TauLib.BookV.Temporal.BoundaryData",
  "module_url": "/corpus/taulib/docs/book-v-temporal-boundary-data/",
  "source_line_start": 92,
  "source_line_end": 105,
  "registry_ids": [
    "V.D37"
  ],
  "related_registry_items": [
    {
      "id": "V.D37",
      "title": "CMB constraint surface",
      "url": "/registry/object/V.D37/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/BoundaryData.lean#L92-L105",
  "formal_status": "defined",
  "declaration_role": "type/data schema",
  "formal_status_label": "type/data schema",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Temporal.BoundaryData",
        "url": "/corpus/taulib/docs/book-v-temporal-boundary-data/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/BoundaryData.lean#L92-L105",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
      "role": "type/data schema",
      "status": "type/data schema"
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

- Module: [TauLib.BookV.Temporal.BoundaryData](/corpus/taulib/docs/book-v-temporal-boundary-data/)
- Source path: [`TauLib/BookV/Temporal/BoundaryData.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/BoundaryData.lean#L92-L105)
- Source range: L92-L105
- Kind: `structure`
- Public role: `type/data schema`
- Formal status hint: `type/data schema`

## Registry Links

- `V.D37` — CMB constraint surface

## Immediate Comment / Docstring

```lean
/-- [V.D37] CMB constraint surface Sigma_CMB = H_partial[omega]|_{n=n_rec}.

    The state of the boundary holonomy algebra at recombination,
    encoding mean temperature, anisotropy spectrum, and polarization.

    The multipole expansion has ~ 2500 independent ell-modes
    (up to Planck resolution). -/
```

## Source Excerpt

```lean
structure CMBSurface where
  /-- Orbit depth at which the surface is evaluated. -/
  depth : Nat
  /-- Depth is positive. -/
  depth_pos : depth > 0
  /-- Number of independent multipole modes (Planck resolution). -/
  multipole_count : Nat
  /-- At least one mode exists. -/
  has_modes : multipole_count > 0
  /-- Mean temperature numerator (mK, scaled: 2725 = 2.725 K). -/
  mean_temp_numer : Nat := 2725
  /-- Mean temperature denominator. -/
  mean_temp_denom : Nat := 1000
  deriving Repr
```
