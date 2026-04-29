---
{
  "projection_kind": "taulib_declaration",
  "title": "all_rational_1",
  "permalink": "/verify/taulib/docs/book-iii-arithmetic-rational-points/all-rational-1/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Arithmetic.RationalPoints`.",
  "declaration_id": "TauLib.BookIII.Arithmetic.RationalPoints::all_rational_1",
  "declaration_slug": "all-rational-1",
  "kind": "theorem",
  "name": "all_rational_1",
  "module_name": "TauLib.BookIII.Arithmetic.RationalPoints",
  "module_url": "/verify/taulib/docs/book-iii-arithmetic-rational-points/",
  "source_line_start": 184,
  "source_line_end": 187,
  "registry_ids": [
    "III.P25"
  ],
  "related_registry_items": [
    {
      "id": "III.P25",
      "title": "Mordell-Weil Analogue",
      "url": "/registry/object/III.P25/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/RationalPoints.lean#L184-L187",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Arithmetic.RationalPoints",
        "url": "/verify/taulib/docs/book-iii-arithmetic-rational-points/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/RationalPoints.lean#L184-L187",
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

- Module: [TauLib.BookIII.Arithmetic.RationalPoints](/verify/taulib/docs/book-iii-arithmetic-rational-points/)
- Source path: [`TauLib/BookIII/Arithmetic/RationalPoints.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/RationalPoints.lean#L184-L187)
- Source range: L184-L187
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.P25` — Mordell-Weil Analogue

## Immediate Comment / Docstring

```lean
/-- [III.P25] Structural: all points rational at depth 1. -/
```

## Source Excerpt

```lean
theorem all_rational_1 :
    rational_point_check 10 1 = true := by native_decide

end Tau.BookIII.Arithmetic
```
