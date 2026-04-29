---
{
  "projection_kind": "taulib_declaration",
  "title": "coherence_correspondence_unification",
  "permalink": "/verify/taulib/docs/book-vii-meta-registers/coherence-correspondence-unification/",
  "summary_short": "`theorem` declaration in `TauLib.BookVII.Meta.Registers`.",
  "declaration_id": "TauLib.BookVII.Meta.Registers::coherence_correspondence_unification",
  "declaration_slug": "coherence-correspondence-unification",
  "kind": "theorem",
  "name": "coherence_correspondence_unification",
  "module_name": "TauLib.BookVII.Meta.Registers",
  "module_url": "/verify/taulib/docs/book-vii-meta-registers/",
  "source_line_start": 675,
  "source_line_end": 679,
  "registry_ids": [
    "VII.T11"
  ],
  "related_registry_items": [
    {
      "id": "VII.T11",
      "title": "Coherence-Correspondence Unification",
      "url": "/registry/object/VII.T11/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L675-L679",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVII.Meta.Registers",
        "url": "/verify/taulib/docs/book-vii-meta-registers/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L675-L679",
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

- Module: [TauLib.BookVII.Meta.Registers](/verify/taulib/docs/book-vii-meta-registers/)
- Source path: [`TauLib/BookVII/Meta/Registers.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L675-L679)
- Source range: L675-L679
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `VII.T11` — Coherence-Correspondence Unification

## Immediate Comment / Docstring

```lean
/-- [VII.T11] Coherence-Correspondence Unification (ch19). Sheaf gluing
    unifies coherence and correspondence theories of truth:
    - Coherence: local sections agree on overlaps (gluing axiom)
    - Correspondence: global section exists (descent condition)
    In τ, these are the same structural condition. -/
```

## Source Excerpt

```lean
theorem coherence_correspondence_unification :
    truth_maker_ontological.tm_section = true ∧
    truth_maker_ontological.tm_diagram = true ∧
    truth_maker_ontological.tm_count = 4 :=
  ⟨rfl, rfl, rfl⟩
```
