---
{
  "projection_kind": "taulib_declaration",
  "title": "d_polarity_zero",
  "permalink": "/verify/taulib/docs/book-iii-sectors-langlands-reflection/d-polarity-zero/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Sectors.LanglandsReflection`.",
  "declaration_id": "TauLib.BookIII.Sectors.LanglandsReflection::d_polarity_zero",
  "declaration_slug": "d-polarity-zero",
  "kind": "theorem",
  "name": "d_polarity_zero",
  "module_name": "TauLib.BookIII.Sectors.LanglandsReflection",
  "module_url": "/verify/taulib/docs/book-iii-sectors-langlands-reflection/",
  "source_line_start": 269,
  "source_line_end": 269,
  "registry_ids": [
    "III.D17"
  ],
  "related_registry_items": [
    {
      "id": "III.D17",
      "title": "Spectral Polarity",
      "url": "/registry/object/III.D17/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Sectors/LanglandsReflection.lean#L269-L269",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Sectors.LanglandsReflection",
        "url": "/verify/taulib/docs/book-iii-sectors-langlands-reflection/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Sectors/LanglandsReflection.lean#L269-L269",
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

- Module: [TauLib.BookIII.Sectors.LanglandsReflection](/verify/taulib/docs/book-iii-sectors-langlands-reflection/)
- Source path: [`TauLib/BookIII/Sectors/LanglandsReflection.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Sectors/LanglandsReflection.lean#L269-L269)
- Source range: L269-L269
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.D17` — Spectral Polarity

## Immediate Comment / Docstring

```lean
/-- [III.D17] Structural: D-sector polarity is (0, 0)
    because only the trivial character (0,0) is in D. -/
```

## Source Excerpt

```lean
theorem d_polarity_zero : spectral_polarity .D 10 = (0, 0) := by native_decide
```
