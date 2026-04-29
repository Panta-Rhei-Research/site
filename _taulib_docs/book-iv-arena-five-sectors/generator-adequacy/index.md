---
{
  "projection_kind": "taulib_declaration",
  "title": "generator_adequacy",
  "permalink": "/verify/taulib/docs/book-iv-arena-five-sectors/generator-adequacy/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Arena.FiveSectors`.",
  "declaration_id": "TauLib.BookIV.Arena.FiveSectors::generator_adequacy",
  "declaration_slug": "generator-adequacy",
  "kind": "theorem",
  "name": "generator_adequacy",
  "module_name": "TauLib.BookIV.Arena.FiveSectors",
  "module_url": "/verify/taulib/docs/book-iv-arena-five-sectors/",
  "source_line_start": 175,
  "source_line_end": 179,
  "registry_ids": [
    "IV.T101"
  ],
  "related_registry_items": [
    {
      "id": "IV.T101",
      "title": "Generator Adequacy",
      "url": "/registry/object/IV.T101/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/FiveSectors.lean#L175-L179",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Arena.FiveSectors",
        "url": "/verify/taulib/docs/book-iv-arena-five-sectors/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/FiveSectors.lean#L175-L179",
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

- Module: [TauLib.BookIV.Arena.FiveSectors](/verify/taulib/docs/book-iv-arena-five-sectors/)
- Source path: [`TauLib/BookIV/Arena/FiveSectors.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/FiveSectors.lean#L175-L179)
- Source range: L175-L179
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.T101` — Generator Adequacy

## Immediate Comment / Docstring

```lean
/-- [IV.T101] Generator Adequacy: the 5 generators span the full
    coupling ledger. Every coupling in the ledger is expressible
    as a function of sector couplings, which are functions of ι_τ. -/
```

## Source Excerpt

```lean
theorem generator_adequacy :
    holonomy_generators.length = 5 ∧
    -- All sectors covered
    (holonomy_generators.map (·.sector)).length = 5 := by
  simp [holonomy_generators]
```
