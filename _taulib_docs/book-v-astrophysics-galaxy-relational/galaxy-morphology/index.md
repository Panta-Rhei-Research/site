---
{
  "projection_kind": "taulib_declaration",
  "title": "GalaxyMorphology",
  "permalink": "/corpus/taulib/docs/book-v-astrophysics-galaxy-relational/galaxy-morphology/",
  "summary_short": "`inductive` declaration in `TauLib.BookV.Astrophysics.GalaxyRelational`.",
  "declaration_id": "TauLib.BookV.Astrophysics.GalaxyRelational::GalaxyMorphology",
  "declaration_slug": "galaxy-morphology",
  "kind": "inductive",
  "name": "GalaxyMorphology",
  "module_name": "TauLib.BookV.Astrophysics.GalaxyRelational",
  "module_url": "/corpus/taulib/docs/book-v-astrophysics-galaxy-relational/",
  "source_line_start": 62,
  "source_line_end": 73,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/GalaxyRelational.lean#L62-L73",
  "formal_status": "defined",
  "declaration_role": "type/data schema",
  "formal_status_label": "type/data schema",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Astrophysics.GalaxyRelational",
        "url": "/corpus/taulib/docs/book-v-astrophysics-galaxy-relational/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/GalaxyRelational.lean#L62-L73",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "inductive",
      "role": "type/data schema",
      "status": "type/data schema"
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

- Module: [TauLib.BookV.Astrophysics.GalaxyRelational](/corpus/taulib/docs/book-v-astrophysics-galaxy-relational/)
- Source path: [`TauLib/BookV/Astrophysics/GalaxyRelational.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/GalaxyRelational.lean#L62-L73)
- Source range: L62-L73
- Kind: `inductive`
- Public role: `type/data schema`
- Formal status hint: `type/data schema`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Galaxy morphology classification (Hubble sequence). -/
```

## Source Excerpt

```lean
inductive GalaxyMorphology where
  /-- Spiral galaxy (disk + arms + bulge). -/
  | Spiral
  /-- Barred spiral (bar + arms + bulge). -/
  | BarredSpiral
  /-- Elliptical galaxy (relaxed, no disk). -/
  | Elliptical
  /-- Lenticular (disk, no arms). -/
  | Lenticular
  /-- Irregular (no regular structure). -/
  | Irregular
  deriving Repr, DecidableEq, BEq
```
