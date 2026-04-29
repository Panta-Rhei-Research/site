---
{
  "projection_kind": "taulib_declaration",
  "title": "bh_threshold_theorem",
  "permalink": "/verify/taulib/docs/book-v-cosmology-bhbirth-topology/bh-threshold-theorem/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Cosmology.BHBirthTopology`.",
  "declaration_id": "TauLib.BookV.Cosmology.BHBirthTopology::bh_threshold_theorem",
  "declaration_slug": "bh-threshold-theorem",
  "kind": "theorem",
  "name": "bh_threshold_theorem",
  "module_name": "TauLib.BookV.Cosmology.BHBirthTopology",
  "module_url": "/verify/taulib/docs/book-v-cosmology-bhbirth-topology/",
  "source_line_start": 166,
  "source_line_end": 168,
  "registry_ids": [
    "V.T109"
  ],
  "related_registry_items": [
    {
      "id": "V.T109",
      "title": "BH Threshold Theorem",
      "url": "/registry/object/V.T109/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BHBirthTopology.lean#L166-L168",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.BHBirthTopology",
        "url": "/verify/taulib/docs/book-v-cosmology-bhbirth-topology/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BHBirthTopology.lean#L166-L168",
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

- Module: [TauLib.BookV.Cosmology.BHBirthTopology](/verify/taulib/docs/book-v-cosmology-bhbirth-topology/)
- Source path: [`TauLib/BookV/Cosmology/BHBirthTopology.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BHBirthTopology.lean#L166-L168)
- Source range: L166-L168
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T109` — BH Threshold Theorem

## Immediate Comment / Docstring

```lean
/-- [V.T109] BH threshold theorem: a BH forms iff the gravitational
    tension at some region U exceeds the spherical capacity.

    G(U) > C_sph(n) ⟹ topology crosses from S² to T².

    The threshold is sharp: below it, neutron star; above it, BH. -/
```

## Source Excerpt

```lean
theorem bh_threshold_theorem (g : GravitationalTension) (c : SphericalCapacity)
    (h : g.tension_numer * c.capacity_denom > c.capacity_numer * g.tension_denom) :
    g.tension_numer * c.capacity_denom > c.capacity_numer * g.tension_denom := h
```
