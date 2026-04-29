---
{
  "projection_kind": "taulib_declaration",
  "title": "full_sheaf_coherence_check",
  "permalink": "/verify/taulib/docs/book-ii-hartogs-sheaf-coherence/full-sheaf-coherence-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Hartogs.SheafCoherence`.",
  "declaration_id": "TauLib.BookII.Hartogs.SheafCoherence::full_sheaf_coherence_check",
  "declaration_slug": "full-sheaf-coherence-check",
  "kind": "def",
  "name": "full_sheaf_coherence_check",
  "module_name": "TauLib.BookII.Hartogs.SheafCoherence",
  "module_url": "/verify/taulib/docs/book-ii-hartogs-sheaf-coherence/",
  "source_line_start": 371,
  "source_line_end": 387,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/SheafCoherence.lean#L371-L387",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Hartogs.SheafCoherence",
        "url": "/verify/taulib/docs/book-ii-hartogs-sheaf-coherence/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/SheafCoherence.lean#L371-L387",
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

- Module: [TauLib.BookII.Hartogs.SheafCoherence](/verify/taulib/docs/book-ii-hartogs-sheaf-coherence/)
- Source path: [`TauLib/BookII/Hartogs/SheafCoherence.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/SheafCoherence.lean#L371-L387)
- Source range: L371-L387
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [II.D47 + II.L06 + II.T32] Complete sheaf coherence verification:
    presheaf structure, gluing, sheaf axioms, and functoriality. -/
```

## Source Excerpt

```lean
def full_sheaf_coherence_check (k_max bound : TauIdx) : Bool :=
  -- Cylinder partition
  cylinder_partition_check 1 &&
  cylinder_partition_check 2 &&
  -- Disjointness (II.L06)
  batch_disjoint_check 1 &&
  batch_disjoint_check 2 &&
  -- Cross-stage containment
  containment_check k_max bound &&
  -- Gluing lemma (II.L06)
  gluing_lemma_check k_max &&
  -- Sheaf axioms (II.T32)
  sheaf_axioms_check k_max &&
  -- Functoriality
  functoriality_check k_max bound &&
  -- Section compatibility
  section_compatibility_check k_max
```
