---
{
  "projection_kind": "taulib_declaration",
  "title": "abc_quality_100",
  "permalink": "/verify/taulib/docs/book-iii-arithmetic-abcdeep/abc-quality-100/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Arithmetic.ABCDeep`.",
  "declaration_id": "TauLib.BookIII.Arithmetic.ABCDeep::abc_quality_100",
  "declaration_slug": "abc-quality-100",
  "kind": "theorem",
  "name": "abc_quality_100",
  "module_name": "TauLib.BookIII.Arithmetic.ABCDeep",
  "module_url": "/verify/taulib/docs/book-iii-arithmetic-abcdeep/",
  "source_line_start": 195,
  "source_line_end": 196,
  "registry_ids": [
    "III.T76"
  ],
  "related_registry_items": [
    {
      "id": "III.T76",
      "title": "ABC Quality 100",
      "url": "/registry/object/III.T76/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/ABCDeep.lean#L195-L196",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/ABCDeep.lean#L195-L196",
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
- Source path: [`TauLib/BookIII/Arithmetic/ABCDeep.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/ABCDeep.lean#L195-L196)
- Source range: L195-L196
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.T76` — ABC Quality 100

## Immediate Comment / Docstring

```lean
/-- [III.T76] Weak ABC (c < rad(abc)²) for all coprime pairs up to 100. -/
```

## Source Excerpt

```lean
theorem abc_quality_100 :
    abc_sieve_check 100 = true := by native_decide
```
