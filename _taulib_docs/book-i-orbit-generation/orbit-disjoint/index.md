---
{
  "projection_kind": "taulib_declaration",
  "title": "orbit_disjoint",
  "permalink": "/verify/taulib/docs/book-i-orbit-generation/orbit-disjoint/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Orbit.Generation`.",
  "declaration_id": "TauLib.BookI.Orbit.Generation::orbit_disjoint",
  "declaration_slug": "orbit-disjoint",
  "kind": "theorem",
  "name": "orbit_disjoint",
  "module_name": "TauLib.BookI.Orbit.Generation",
  "module_url": "/verify/taulib/docs/book-i-orbit-generation/",
  "source_line_start": 119,
  "source_line_end": 122,
  "registry_ids": [
    "I.P03"
  ],
  "related_registry_items": [
    {
      "id": "I.P03",
      "title": "Pairwise Disjointness of Orbits",
      "url": "/registry/object/I.P03/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/Generation.lean#L119-L122",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Orbit.Generation",
        "url": "/verify/taulib/docs/book-i-orbit-generation/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/Generation.lean#L119-L122",
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

- Module: [TauLib.BookI.Orbit.Generation](/verify/taulib/docs/book-i-orbit-generation/)
- Source path: [`TauLib/BookI/Orbit/Generation.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/Generation.lean#L119-L122)
- Source range: L119-L122
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `I.P03` — Pairwise Disjointness of Orbits

## Immediate Comment / Docstring

```lean
/-- [I.P03] Orbit rays are pairwise disjoint: if g ≠ h, no object
    belongs to both O_g and O_h. -/
```

## Source Excerpt

```lean
theorem orbit_disjoint (g h : Generator) (hgh : g ≠ h)
    (x : TauObj) : ¬(OrbitRay g x ∧ OrbitRay h x) := by
  intro ⟨⟨hsg, _⟩, ⟨hsh, _⟩⟩
  exact hgh (hsg.symm.trans hsh)
```
