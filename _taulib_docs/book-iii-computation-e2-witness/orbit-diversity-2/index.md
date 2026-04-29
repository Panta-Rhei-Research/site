---
{
  "projection_kind": "taulib_declaration",
  "title": "orbit_diversity_2",
  "permalink": "/verify/taulib/docs/book-iii-computation-e2-witness/orbit-diversity-2/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Computation.E2Witness`.",
  "declaration_id": "TauLib.BookIII.Computation.E2Witness::orbit_diversity_2",
  "declaration_slug": "orbit-diversity-2",
  "kind": "theorem",
  "name": "orbit_diversity_2",
  "module_name": "TauLib.BookIII.Computation.E2Witness",
  "module_url": "/verify/taulib/docs/book-iii-computation-e2-witness/",
  "source_line_start": 214,
  "source_line_end": 215,
  "registry_ids": [
    "III.D84"
  ],
  "related_registry_items": [
    {
      "id": "III.D84",
      "title": "E₂ Orbit Structure",
      "url": "/registry/object/III.D84/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/E2Witness.lean#L214-L215",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Computation.E2Witness",
        "url": "/verify/taulib/docs/book-iii-computation-e2-witness/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/E2Witness.lean#L214-L215",
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

- Module: [TauLib.BookIII.Computation.E2Witness](/verify/taulib/docs/book-iii-computation-e2-witness/)
- Source path: [`TauLib/BookIII/Computation/E2Witness.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/E2Witness.lean#L214-L215)
- Source range: L214-L215
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.D84` — E₂ Orbit Structure

## Immediate Comment / Docstring

```lean
/-- [III.D84] Orbit diversity at stage 2. -/
```

## Source Excerpt

```lean
theorem orbit_diversity_2 :
    orbit_diversity_check 2 = true := by native_decide
```
