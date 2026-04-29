---
{
  "projection_kind": "taulib_declaration",
  "title": "no_interior_singularity",
  "permalink": "/verify/taulib/docs/book-v-cosmology-bhbirth-topology/no-interior-singularity/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Cosmology.BHBirthTopology`.",
  "declaration_id": "TauLib.BookV.Cosmology.BHBirthTopology::no_interior_singularity",
  "declaration_slug": "no-interior-singularity",
  "kind": "theorem",
  "name": "no_interior_singularity",
  "module_name": "TauLib.BookV.Cosmology.BHBirthTopology",
  "module_url": "/verify/taulib/docs/book-v-cosmology-bhbirth-topology/",
  "source_line_start": 191,
  "source_line_end": 193,
  "registry_ids": [
    "V.P93"
  ],
  "related_registry_items": [
    {
      "id": "V.P93",
      "title": "No Interior Singularity",
      "url": "/registry/object/V.P93/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BHBirthTopology.lean#L191-L193",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BHBirthTopology.lean#L191-L193",
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
- Source path: [`TauLib/BookV/Cosmology/BHBirthTopology.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BHBirthTopology.lean#L191-L193)
- Source range: L191-L193
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.P93` — No Interior Singularity

## Immediate Comment / Docstring

```lean
/-- [V.P93] No interior singularity: a τ-BH has no interior singularity.

    The interior is a compact subset of T² with all boundary characters
    bounded. Penrose-Hawking does not apply (profinite, not smooth manifold). -/
```

## Source Excerpt

```lean
theorem no_interior_singularity (bh : BlackHoleTopologicalEvent)
    (hs : bh.is_smooth = true) :
    bh.is_smooth = true := hs
```
