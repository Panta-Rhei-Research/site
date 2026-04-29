---
{
  "projection_kind": "taulib_declaration",
  "title": "high_quality_30",
  "permalink": "/verify/taulib/docs/book-iii-arithmetic-abcdeep/high-quality-30/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Arithmetic.ABCDeep`.",
  "declaration_id": "TauLib.BookIII.Arithmetic.ABCDeep::high_quality_30",
  "declaration_slug": "high-quality-30",
  "kind": "theorem",
  "name": "high_quality_30",
  "module_name": "TauLib.BookIII.Arithmetic.ABCDeep",
  "module_url": "/verify/taulib/docs/book-iii-arithmetic-abcdeep/",
  "source_line_start": 216,
  "source_line_end": 217,
  "registry_ids": [
    "III.D109"
  ],
  "related_registry_items": [
    {
      "id": "III.D109",
      "title": "High Quality Count",
      "url": "/registry/object/III.D109/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/ABCDeep.lean#L216-L217",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Arithmetic.ABCDeep",
        "url": "/verify/taulib/docs/book-iii-arithmetic-abcdeep/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/ABCDeep.lean#L216-L217",
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

- Module: [TauLib.BookIII.Arithmetic.ABCDeep](/verify/taulib/docs/book-iii-arithmetic-abcdeep/)
- Source path: [`TauLib/BookIII/Arithmetic/ABCDeep.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/ABCDeep.lean#L216-L217)
- Source range: L216-L217
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.D109` — High Quality Count

## Immediate Comment / Docstring

```lean
/-- [III.D109] Few high quality triples (q ≥ 1) up to 30: at most 5. -/
```

## Source Excerpt

```lean
theorem high_quality_30 :
    abc_high_quality_count 30 <= 5 := by native_decide
```
