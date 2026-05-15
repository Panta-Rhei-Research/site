---
{
  "projection_kind": "taulib_declaration",
  "title": "rite_boundary_crossing",
  "permalink": "/corpus/taulib/docs/book-vii-social-ontology/rite-boundary-crossing/",
  "summary_short": "`theorem` declaration in `TauLib.BookVII.Social.Ontology`.",
  "declaration_id": "TauLib.BookVII.Social.Ontology::rite_boundary_crossing",
  "declaration_slug": "rite-boundary-crossing",
  "kind": "theorem",
  "name": "rite_boundary_crossing",
  "module_name": "TauLib.BookVII.Social.Ontology",
  "module_url": "/corpus/taulib/docs/book-vii-social-ontology/",
  "source_line_start": 500,
  "source_line_end": 506,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Social/Ontology.lean#L500-L506",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVII.Social.Ontology",
        "url": "/corpus/taulib/docs/book-vii-social-ontology/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Social/Ontology.lean#L500-L506",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "role": "proof obligation",
      "status": "formal proof obligation checked"
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

- Module: [TauLib.BookVII.Social.Ontology](/corpus/taulib/docs/book-vii-social-ontology/)
- Source path: [`TauLib/BookVII/Social/Ontology.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Social/Ontology.lean#L500-L506)
- Source range: L500-L506
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [VII.Lxx-R8C10] Rite of Passage as Boundary Crossing: a rite of
    passage is an instance of the Boundary Archetype (VII.D18) in the
    social category. The before/after states correspond to the two lobes
    of L = S¹ ∨ S¹; the ritual itself is the crossing through p₀.
    Uses: BoundaryArchetype carrier_is_lemniscate, pi1_free_rank = 2. -/
```

## Source Excerpt

```lean
theorem rite_boundary_crossing :
    rite_of_passage.is_morphism = true ∧
    rite_of_passage.factors_through_crossing = true ∧
    rite_of_passage.crosses_components = true ∧
    boundary_archetype.carrier_is_lemniscate = true ∧
    boundary_archetype.lobe_count = 2 :=
  ⟨rfl, rfl, rfl, rfl, rfl⟩
```
