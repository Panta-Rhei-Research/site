---
{
  "projection_kind": "taulib_declaration",
  "title": "obstruction_100_p3",
  "permalink": "/verify/taulib/docs/book-iii-spectral-goldbach-deep/obstruction-100-p3/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Spectral.GoldbachDeep`.",
  "declaration_id": "TauLib.BookIII.Spectral.GoldbachDeep::obstruction_100_p3",
  "declaration_slug": "obstruction-100-p3",
  "kind": "theorem",
  "name": "obstruction_100_p3",
  "module_name": "TauLib.BookIII.Spectral.GoldbachDeep",
  "module_url": "/verify/taulib/docs/book-iii-spectral-goldbach-deep/",
  "source_line_start": 214,
  "source_line_end": 215,
  "registry_ids": [
    "III.D104"
  ],
  "related_registry_items": [
    {
      "id": "III.D104",
      "title": "Goldbach Obstruction",
      "url": "/registry/object/III.D104/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/GoldbachDeep.lean#L214-L215",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Spectral.GoldbachDeep",
        "url": "/verify/taulib/docs/book-iii-spectral-goldbach-deep/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/GoldbachDeep.lean#L214-L215",
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

- Module: [TauLib.BookIII.Spectral.GoldbachDeep](/verify/taulib/docs/book-iii-spectral-goldbach-deep/)
- Source path: [`TauLib/BookIII/Spectral/GoldbachDeep.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/GoldbachDeep.lean#L214-L215)
- Source range: L214-L215
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.D104` — Goldbach Obstruction

## Immediate Comment / Docstring

```lean
/-- [III.D104] Obstruction at p=3 for n=100: 0 (100 mod 3 ≠ 0). -/
```

## Source Excerpt

```lean
theorem obstruction_100_p3 :
    goldbach_obstruction_count 100 3 = 0 := by native_decide
```
