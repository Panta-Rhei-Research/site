---
{
  "projection_kind": "taulib_declaration",
  "title": "bh_toroidal_structural",
  "permalink": "/verify/taulib/docs/book-v-cosmology-bhbirth-topology/bh-toroidal-structural/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Cosmology.BHBirthTopology`.",
  "declaration_id": "TauLib.BookV.Cosmology.BHBirthTopology::bh_toroidal_structural",
  "declaration_slug": "bh-toroidal-structural",
  "kind": "theorem",
  "name": "bh_toroidal_structural",
  "module_name": "TauLib.BookV.Cosmology.BHBirthTopology",
  "module_url": "/verify/taulib/docs/book-v-cosmology-bhbirth-topology/",
  "source_line_start": 310,
  "source_line_end": 311,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BHBirthTopology.lean#L310-L311",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BHBirthTopology.lean#L310-L311",
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
- Source path: [`TauLib/BookV/Cosmology/BHBirthTopology.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BHBirthTopology.lean#L310-L311)
- Source range: L310-L311
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [V.T110 upgrade] BH toroidal topology: structural proof
    using LinkingClass and fiber homology.

    Non-trivial linking classes in H₁(T²; ℤ) ≅ ℤ ⊕ ℤ
    trace T²-shaped loci. The linking class (a, b) with
    a ≠ 0 or b ≠ 0 wraps both generators of π₁(T²).

    This is structural: a BH with horizon in H₁(T²) must
    have T²-topology, not S²-topology, because S² has
    H₁(S²) = 0 (no non-trivial 1-cycles). -/
```

## Source Excerpt

```lean
theorem bh_toroidal_structural (lc : LinkingClass) :
    lc.a ≠ 0 ∨ lc.b ≠ 0 := lc.nontrivial
```
