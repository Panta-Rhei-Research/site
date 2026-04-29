---
{
  "projection_kind": "taulib_declaration",
  "title": "crt_roundtrip_42",
  "permalink": "/verify/taulib/docs/book-iii-spectral-crt/crt-roundtrip-42/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Spectral.CRT`.",
  "declaration_id": "TauLib.BookIII.Spectral.CRT::crt_roundtrip_42",
  "declaration_slug": "crt-roundtrip-42",
  "kind": "theorem",
  "name": "crt_roundtrip_42",
  "module_name": "TauLib.BookIII.Spectral.CRT",
  "module_url": "/verify/taulib/docs/book-iii-spectral-crt/",
  "source_line_start": 244,
  "source_line_end": 245,
  "registry_ids": [
    "III.T10"
  ],
  "related_registry_items": [
    {
      "id": "III.T10",
      "title": "CRT Decomposition Theorem",
      "url": "/registry/object/III.T10/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/CRT.lean#L244-L245",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Spectral.CRT",
        "url": "/verify/taulib/docs/book-iii-spectral-crt/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/CRT.lean#L244-L245",
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

- Module: [TauLib.BookIII.Spectral.CRT](/verify/taulib/docs/book-iii-spectral-crt/)
- Source path: [`TauLib/BookIII/Spectral/CRT.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/CRT.lean#L244-L245)
- Source range: L244-L245
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.T10` — CRT Decomposition Theorem

## Immediate Comment / Docstring

```lean
/-- [III.T10] Structural: CRT round-trip at depth 3 for x = 42. -/
```

## Source Excerpt

```lean
theorem crt_roundtrip_42 :
    crt_reconstruct (crt_decompose 42 3) 3 = reduce 42 3 := by native_decide
```
