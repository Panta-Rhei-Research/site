---
{
  "projection_kind": "taulib_declaration",
  "title": "VacuumEnergyComparison",
  "permalink": "/corpus/taulib/docs/book-iv-strong-vacuum-catastrophe/vacuum-energy-comparison/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Strong.VacuumCatastrophe`.",
  "declaration_id": "TauLib.BookIV.Strong.VacuumCatastrophe::VacuumEnergyComparison",
  "declaration_slug": "vacuum-energy-comparison",
  "kind": "structure",
  "name": "VacuumEnergyComparison",
  "module_name": "TauLib.BookIV.Strong.VacuumCatastrophe",
  "module_url": "/corpus/taulib/docs/book-iv-strong-vacuum-catastrophe/",
  "source_line_start": 247,
  "source_line_end": 258,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/VacuumCatastrophe.lean#L247-L258",
  "formal_status": "defined",
  "declaration_role": "type/data schema",
  "formal_status_label": "type/data schema",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Strong.VacuumCatastrophe",
        "url": "/corpus/taulib/docs/book-iv-strong-vacuum-catastrophe/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/VacuumCatastrophe.lean#L247-L258",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
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

- Module: [TauLib.BookIV.Strong.VacuumCatastrophe](/corpus/taulib/docs/book-iv-strong-vacuum-catastrophe/)
- Source path: [`TauLib/BookIV/Strong/VacuumCatastrophe.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/VacuumCatastrophe.lean#L247-L258)
- Source range: L247-L258
- Kind: `structure`
- Public role: `type/data schema`
- Formal status hint: `type/data schema`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Summary comparing tau and orthodox vacuum energy. -/
```

## Source Excerpt

```lean
structure VacuumEnergyComparison where
  /-- Framework name. -/
  framework : String
  /-- Mode count type. -/
  mode_count : ModeCountType
  /-- Divergent? -/
  divergent : Bool
  /-- Requires renormalization? -/
  requires_renorm : Bool
  /-- Cosmological constant problem? -/
  cc_problem : Bool
  deriving Repr
```
