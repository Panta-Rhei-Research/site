---
{
  "projection_kind": "taulib_declaration",
  "title": "spectral_support_3_30",
  "permalink": "/verify/taulib/docs/book-ii-hartogs-canonical-basis/spectral-support-3-30/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Hartogs.CanonicalBasis`.",
  "declaration_id": "TauLib.BookII.Hartogs.CanonicalBasis::spectral_support_3_30",
  "declaration_slug": "spectral-support-3-30",
  "kind": "theorem",
  "name": "spectral_support_3_30",
  "module_name": "TauLib.BookII.Hartogs.CanonicalBasis",
  "module_url": "/verify/taulib/docs/book-ii-hartogs-canonical-basis/",
  "source_line_start": 403,
  "source_line_end": 404,
  "registry_ids": [
    "II.T31"
  ],
  "related_registry_items": [
    {
      "id": "II.T31",
      "title": "Finite Spectral Support",
      "url": "/registry/object/II.T31/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/CanonicalBasis.lean#L403-L404",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Hartogs.CanonicalBasis",
        "url": "/verify/taulib/docs/book-ii-hartogs-canonical-basis/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/CanonicalBasis.lean#L403-L404",
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

- Module: [TauLib.BookII.Hartogs.CanonicalBasis](/verify/taulib/docs/book-ii-hartogs-canonical-basis/)
- Source path: [`TauLib/BookII/Hartogs/CanonicalBasis.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/CanonicalBasis.lean#L403-L404)
- Source range: L403-L404
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `II.T31` — Finite Spectral Support

## Immediate Comment / Docstring

```lean
-- Finite spectral support [II.T31]
```

## Source Excerpt

```lean
theorem spectral_support_3_30 :
    finite_spectral_support_check 3 30 = true := by native_decide
```
