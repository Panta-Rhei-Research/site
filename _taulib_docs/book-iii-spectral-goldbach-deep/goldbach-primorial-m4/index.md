---
{
  "projection_kind": "taulib_declaration",
  "title": "goldbach_primorial_m4",
  "permalink": "/verify/taulib/docs/book-iii-spectral-goldbach-deep/goldbach-primorial-m4/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Spectral.GoldbachDeep`.",
  "declaration_id": "TauLib.BookIII.Spectral.GoldbachDeep::goldbach_primorial_m4",
  "declaration_slug": "goldbach-primorial-m4",
  "kind": "theorem",
  "name": "goldbach_primorial_m4",
  "module_name": "TauLib.BookIII.Spectral.GoldbachDeep",
  "module_url": "/verify/taulib/docs/book-iii-spectral-goldbach-deep/",
  "source_line_start": 178,
  "source_line_end": 179,
  "registry_ids": [
    "III.T69"
  ],
  "related_registry_items": [
    {
      "id": "III.T69",
      "title": "Goldbach at Primorial M₄",
      "url": "/registry/object/III.T69/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/GoldbachDeep.lean#L178-L179",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/GoldbachDeep.lean#L178-L179",
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
- Source path: [`TauLib/BookIII/Spectral/GoldbachDeep.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/GoldbachDeep.lean#L178-L179)
- Source range: L178-L179
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.T69` — Goldbach at Primorial M₄

## Immediate Comment / Docstring

```lean
/-- [III.T69] Goldbach at primorial M₄=210: all even n ≤ 210 verified. -/
```

## Source Excerpt

```lean
theorem goldbach_primorial_m4 :
    goldbach_sieve_check 210 = true := by native_decide
```
