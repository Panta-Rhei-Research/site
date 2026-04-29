---
{
  "projection_kind": "taulib_declaration",
  "title": "obstruction_bounded_5",
  "permalink": "/verify/taulib/docs/book-iii-spectral-goldbach-deep/obstruction-bounded-5/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Spectral.GoldbachDeep`.",
  "declaration_id": "TauLib.BookIII.Spectral.GoldbachDeep::obstruction_bounded_5",
  "declaration_slug": "obstruction-bounded-5",
  "kind": "theorem",
  "name": "obstruction_bounded_5",
  "module_name": "TauLib.BookIII.Spectral.GoldbachDeep",
  "module_url": "/verify/taulib/docs/book-iii-spectral-goldbach-deep/",
  "source_line_start": 186,
  "source_line_end": 187,
  "registry_ids": [
    "III.T71"
  ],
  "related_registry_items": [
    {
      "id": "III.T71",
      "title": "Obstruction Bounded",
      "url": "/registry/object/III.T71/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/GoldbachDeep.lean#L186-L187",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/GoldbachDeep.lean#L186-L187",
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
- Source path: [`TauLib/BookIII/Spectral/GoldbachDeep.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/GoldbachDeep.lean#L186-L187)
- Source range: L186-L187
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.T71` — Obstruction Bounded

## Immediate Comment / Docstring

```lean
/-- [III.T71] Obstruction bounded by 1 at each prime, for even n ≤ 100. -/
```

## Source Excerpt

```lean
theorem obstruction_bounded_5 :
    obstruction_bounded_check 100 5 = true := by native_decide
```
