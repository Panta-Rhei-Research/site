---
{
  "projection_kind": "taulib_declaration",
  "title": "HybridizationType",
  "permalink": "/corpus/taulib/docs/book-iv-particles-periodic-table/hybridization-type/",
  "summary_short": "`inductive` declaration in `TauLib.BookIV.Particles.PeriodicTable`.",
  "declaration_id": "TauLib.BookIV.Particles.PeriodicTable::HybridizationType",
  "declaration_slug": "hybridization-type",
  "kind": "inductive",
  "name": "HybridizationType",
  "module_name": "TauLib.BookIV.Particles.PeriodicTable",
  "module_url": "/corpus/taulib/docs/book-iv-particles-periodic-table/",
  "source_line_start": 312,
  "source_line_end": 319,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/PeriodicTable.lean#L312-L319",
  "formal_status": "defined",
  "declaration_role": "type/data schema",
  "formal_status_label": "type/data schema",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/PeriodicTable.lean#L312-L319",
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

- Module: [TauLib.BookIV.Particles.PeriodicTable](/corpus/taulib/docs/book-iv-particles-periodic-table/)
- Source path: [`TauLib/BookIV/Particles/PeriodicTable.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/PeriodicTable.lean#L312-L319)
- Source range: L312-L319
- Kind: `inductive`
- Public role: `type/data schema`
- Formal status hint: `type/data schema`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Hybridization type. -/
```

## Source Excerpt

```lean
inductive HybridizationType where
  /-- sp: 2 linear hybrids (180°). -/
  | sp
  /-- sp²: 3 planar hybrids (120°). -/
  | sp2
  /-- sp³: 4 tetrahedral hybrids (109.5°). -/
  | sp3
  deriving Repr, DecidableEq, BEq
```
