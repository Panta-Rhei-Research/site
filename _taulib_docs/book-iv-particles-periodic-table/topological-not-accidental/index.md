---
{
  "projection_kind": "taulib_declaration",
  "title": "topological_not_accidental",
  "permalink": "/corpus/taulib/docs/book-iv-particles-periodic-table/topological-not-accidental/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Particles.PeriodicTable`.",
  "declaration_id": "TauLib.BookIV.Particles.PeriodicTable::topological_not_accidental",
  "declaration_slug": "topological-not-accidental",
  "kind": "def",
  "name": "topological_not_accidental",
  "module_name": "TauLib.BookIV.Particles.PeriodicTable",
  "module_url": "/corpus/taulib/docs/book-iv-particles-periodic-table/",
  "source_line_start": 200,
  "source_line_end": 201,
  "registry_ids": [
    "IV.R141"
  ],
  "related_registry_items": [
    {
      "id": "IV.R141",
      "title": "Topological not accidental",
      "url": "/registry/object/IV.R141/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/PeriodicTable.lean#L200-L201",
  "formal_status": "defined",
  "declaration_role": "docstring/data record",
  "formal_status_label": "docstring/data record",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Particles.PeriodicTable",
        "url": "/corpus/taulib/docs/book-iv-particles-periodic-table/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/PeriodicTable.lean#L200-L201",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "role": "docstring/data record",
      "status": "docstring/data record"
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

- Module: [TauLib.BookIV.Particles.PeriodicTable](/corpus/taulib/docs/book-iv-particles-periodic-table/)
- Source path: [`TauLib/BookIV/Particles/PeriodicTable.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/PeriodicTable.lean#L200-L201)
- Source range: L200-L201
- Kind: `def`
- Public role: `docstring/data record`
- Formal status hint: `docstring/data record`

## Registry Links

- `IV.R141` — Topological not accidental

## Immediate Comment / Docstring

```lean
/-- [IV.R141] The sequence 2, 8, 8, 18, 18, 32,... is a topological
    invariant of T²: the periodic table has its shape because the
    fiber torus has its shape. -/
```

## Source Excerpt

```lean
def topological_not_accidental : String :=
  "Period sequence is topological invariant of T^2, not accidental"
```
