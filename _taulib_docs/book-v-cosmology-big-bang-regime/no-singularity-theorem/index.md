---
{
  "projection_kind": "taulib_declaration",
  "title": "no_singularity_theorem",
  "permalink": "/verify/taulib/docs/book-v-cosmology-big-bang-regime/no-singularity-theorem/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Cosmology.BigBangRegime`.",
  "declaration_id": "TauLib.BookV.Cosmology.BigBangRegime::no_singularity_theorem",
  "declaration_slug": "no-singularity-theorem",
  "kind": "theorem",
  "name": "no_singularity_theorem",
  "module_name": "TauLib.BookV.Cosmology.BigBangRegime",
  "module_url": "/verify/taulib/docs/book-v-cosmology-big-bang-regime/",
  "source_line_start": 178,
  "source_line_end": 182,
  "registry_ids": [
    "V.T103"
  ],
  "related_registry_items": [
    {
      "id": "V.T103",
      "title": "No-Singularity Theorem",
      "url": "/registry/object/V.T103/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BigBangRegime.lean#L178-L182",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.BigBangRegime",
        "url": "/verify/taulib/docs/book-v-cosmology-big-bang-regime/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BigBangRegime.lean#L178-L182",
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

- Module: [TauLib.BookV.Cosmology.BigBangRegime](/verify/taulib/docs/book-v-cosmology-big-bang-regime/)
- Source path: [`TauLib/BookV/Cosmology/BigBangRegime.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BigBangRegime.lean#L178-L182)
- Source range: L178-L182
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T103` — No-Singularity Theorem

## Immediate Comment / Docstring

```lean
/-- [V.T103] No-singularity theorem: no cosmological singularity
    exists in Category τ.

    The profinite boundary holonomy algebra H_∂[ω] has bounded
    norm at every level. There is a first element α₁ but no
    limit a → 0. Curvature is bounded, geodesics are complete,
    energy density is finite.

    The proof is structural: τ³ is profinite (discrete, with a
    first element), not a smooth manifold with a continuum limit. -/
```

## Source Excerpt

```lean
theorem no_singularity_theorem (o : TemporalOpening)
    (hu : o.is_unique = true)
    (hm : o.is_maximal = true) :
    o.first_tick > 0 := by
  rw [o.first_tick_is_one]; omega
```
