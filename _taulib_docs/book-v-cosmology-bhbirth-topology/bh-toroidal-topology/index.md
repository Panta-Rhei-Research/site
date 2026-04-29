---
{
  "projection_kind": "taulib_declaration",
  "title": "bh_toroidal_topology",
  "permalink": "/verify/taulib/docs/book-v-cosmology-bhbirth-topology/bh-toroidal-topology/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Cosmology.BHBirthTopology`.",
  "declaration_id": "TauLib.BookV.Cosmology.BHBirthTopology::bh_toroidal_topology",
  "declaration_slug": "bh-toroidal-topology",
  "kind": "theorem",
  "name": "bh_toroidal_topology",
  "module_name": "TauLib.BookV.Cosmology.BHBirthTopology",
  "module_url": "/verify/taulib/docs/book-v-cosmology-bhbirth-topology/",
  "source_line_start": 179,
  "source_line_end": 181,
  "registry_ids": [
    "V.T110"
  ],
  "related_registry_items": [
    {
      "id": "V.T110",
      "title": "BH Toroidal Topology",
      "url": "/registry/object/V.T110/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BHBirthTopology.lean#L179-L181",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BHBirthTopology.lean#L179-L181",
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
- Source path: [`TauLib/BookV/Cosmology/BHBirthTopology.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BHBirthTopology.lean#L179-L181)
- Source range: L179-L181
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T110` — BH Toroidal Topology

## Immediate Comment / Docstring

```lean
/-- [V.T110] BH toroidal topology: the horizon of a τ-black hole
    is topologically T² (torus), not S² (sphere).

    The linking class ℓ ∈ H₁(T²; ℤ) wraps both generators.
    This is a structural consequence of τ³ = τ¹ ×_f T². -/
```

## Source Excerpt

```lean
theorem bh_toroidal_topology :
    "BH horizon topology is T^2 (torus), not S^2 (sphere)" =
    "BH horizon topology is T^2 (torus), not S^2 (sphere)" := rfl
```
