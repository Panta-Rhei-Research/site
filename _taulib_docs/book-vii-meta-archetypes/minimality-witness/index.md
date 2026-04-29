---
{
  "projection_kind": "taulib_declaration",
  "title": "minimality_witness",
  "permalink": "/verify/taulib/docs/book-vii-meta-archetypes/minimality-witness/",
  "summary_short": "`theorem` declaration in `TauLib.BookVII.Meta.Archetypes`.",
  "declaration_id": "TauLib.BookVII.Meta.Archetypes::minimality_witness",
  "declaration_slug": "minimality-witness",
  "kind": "theorem",
  "name": "minimality_witness",
  "module_name": "TauLib.BookVII.Meta.Archetypes",
  "module_url": "/verify/taulib/docs/book-vii-meta-archetypes/",
  "source_line_start": 213,
  "source_line_end": 217,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Archetypes.lean#L213-L217",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVII.Meta.Archetypes",
        "url": "/verify/taulib/docs/book-vii-meta-archetypes/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Archetypes.lean#L213-L217",
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

- Module: [TauLib.BookVII.Meta.Archetypes](/verify/taulib/docs/book-vii-meta-archetypes/)
- Source path: [`TauLib/BookVII/Meta/Archetypes.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Archetypes.lean#L213-L217)
- Source range: L213-L217
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [VII.Lxx] Minimality Witness: the archetype is the unique element
    satisfying all three conditions (A1)–(A3). Any other element satisfying
    (A1)–(A2) contains the archetype. The archetype is contained in every
    j-closed I-exhibiting subobject. -/
```

## Source Excerpt

```lean
theorem minimality_witness :
    canonical_archetype.a3_minimal = true ∧
    canonical_archetype.a1_j_closed = true ∧
    canonical_archetype.a2_exhibits_invariant = true :=
  ⟨rfl, rfl, rfl⟩
```
