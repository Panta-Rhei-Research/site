---
{
  "projection_kind": "taulib_declaration",
  "title": "no_singularity_from_linking",
  "permalink": "/verify/taulib/docs/book-v-cosmology-bhbirth-topology/no-singularity-from-linking/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Cosmology.BHBirthTopology`.",
  "declaration_id": "TauLib.BookV.Cosmology.BHBirthTopology::no_singularity_from_linking",
  "declaration_slug": "no-singularity-from-linking",
  "kind": "theorem",
  "name": "no_singularity_from_linking",
  "module_name": "TauLib.BookV.Cosmology.BHBirthTopology",
  "module_url": "/verify/taulib/docs/book-v-cosmology-bhbirth-topology/",
  "source_line_start": 316,
  "source_line_end": 321,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BHBirthTopology.lean#L316-L321",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BHBirthTopology.lean#L316-L321",
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
- Source path: [`TauLib/BookV/Cosmology/BHBirthTopology.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BHBirthTopology.lean#L316-L321)
- Source range: L316-L321
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- No interior singularity: structural proof from linking class.
    A BH with linking class lc and smooth birth event has
    bounded boundary characters everywhere in the neighborhood. -/
```

## Source Excerpt

```lean
theorem no_singularity_from_linking (bh : BlackHoleTopologicalEvent)
    (hs : bh.is_smooth = true) (lc_eq : bh.linking = unit_linking) :
    bh.is_smooth = true ∧ bh.linking.a ≠ 0 := by
  constructor
  · exact hs
  · rw [lc_eq]; decide
```
