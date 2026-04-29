---
{
  "projection_kind": "taulib_declaration",
  "title": "diagonal_mod",
  "permalink": "/verify/taulib/docs/book-iii-bridge-incompleteness/diagonal-mod/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Bridge.Incompleteness`.",
  "declaration_id": "TauLib.BookIII.Bridge.Incompleteness::diagonal_mod",
  "declaration_slug": "diagonal-mod",
  "kind": "theorem",
  "name": "diagonal_mod",
  "module_name": "TauLib.BookIII.Bridge.Incompleteness",
  "module_url": "/verify/taulib/docs/book-iii-bridge-incompleteness/",
  "source_line_start": 258,
  "source_line_end": 259,
  "registry_ids": [
    "III.T44"
  ],
  "related_registry_items": [
    {
      "id": "III.T44",
      "title": "Incompleteness as VM Boundary",
      "url": "/registry/object/III.T44/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/Incompleteness.lean#L258-L259",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Bridge.Incompleteness",
        "url": "/verify/taulib/docs/book-iii-bridge-incompleteness/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/Incompleteness.lean#L258-L259",
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

- Module: [TauLib.BookIII.Bridge.Incompleteness](/verify/taulib/docs/book-iii-bridge-incompleteness/)
- Source path: [`TauLib/BookIII/Bridge/Incompleteness.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/Incompleteness.lean#L258-L259)
- Source range: L258-L259
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.T44` — Incompleteness as VM Boundary

## Immediate Comment / Docstring

```lean
/-- [III.T44] Structural: diagonal at depth 3 is modular. -/
```

## Source Excerpt

```lean
theorem diagonal_mod :
    diagonal 7 3 = 14 := by native_decide
```
