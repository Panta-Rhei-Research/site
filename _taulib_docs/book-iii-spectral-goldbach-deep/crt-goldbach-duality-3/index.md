---
{
  "projection_kind": "taulib_declaration",
  "title": "crt_goldbach_duality_3",
  "permalink": "/verify/taulib/docs/book-iii-spectral-goldbach-deep/crt-goldbach-duality-3/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Spectral.GoldbachDeep`.",
  "declaration_id": "TauLib.BookIII.Spectral.GoldbachDeep::crt_goldbach_duality_3",
  "declaration_slug": "crt-goldbach-duality-3",
  "kind": "theorem",
  "name": "crt_goldbach_duality_3",
  "module_name": "TauLib.BookIII.Spectral.GoldbachDeep",
  "module_url": "/verify/taulib/docs/book-iii-spectral-goldbach-deep/",
  "source_line_start": 190,
  "source_line_end": 191,
  "registry_ids": [
    "III.P43"
  ],
  "related_registry_items": [
    {
      "id": "III.P43",
      "title": "CRT-Goldbach Duality",
      "url": "/registry/object/III.P43/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/GoldbachDeep.lean#L190-L191",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/GoldbachDeep.lean#L190-L191",
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
- Source path: [`TauLib/BookIII/Spectral/GoldbachDeep.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/GoldbachDeep.lean#L190-L191)
- Source range: L190-L191
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.P43` — CRT-Goldbach Duality

## Immediate Comment / Docstring

```lean
/-- [III.P43] CRT-Goldbach duality at depth 3, even n ≤ 100. -/
```

## Source Excerpt

```lean
theorem crt_goldbach_duality_3 :
    crt_goldbach_duality_check 100 3 = true := by native_decide
```
