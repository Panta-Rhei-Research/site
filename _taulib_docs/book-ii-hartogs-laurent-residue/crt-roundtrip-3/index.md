---
{
  "projection_kind": "taulib_declaration",
  "title": "crt_roundtrip_3",
  "permalink": "/verify/taulib/docs/book-ii-hartogs-laurent-residue/crt-roundtrip-3/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Hartogs.LaurentResidue`.",
  "declaration_id": "TauLib.BookII.Hartogs.LaurentResidue::crt_roundtrip_3",
  "declaration_slug": "crt-roundtrip-3",
  "kind": "theorem",
  "name": "crt_roundtrip_3",
  "module_name": "TauLib.BookII.Hartogs.LaurentResidue",
  "module_url": "/verify/taulib/docs/book-ii-hartogs-laurent-residue/",
  "source_line_start": 483,
  "source_line_end": 484,
  "registry_ids": [
    "II.T30"
  ],
  "related_registry_items": [
    {
      "id": "II.T30",
      "title": "Residue Theorem",
      "url": "/registry/object/II.T30/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/LaurentResidue.lean#L483-L484",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Hartogs.LaurentResidue",
        "url": "/verify/taulib/docs/book-ii-hartogs-laurent-residue/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/LaurentResidue.lean#L483-L484",
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

- Module: [TauLib.BookII.Hartogs.LaurentResidue](/verify/taulib/docs/book-ii-hartogs-laurent-residue/)
- Source path: [`TauLib/BookII/Hartogs/LaurentResidue.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/LaurentResidue.lean#L483-L484)
- Source range: L483-L484
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `II.T30` — Residue Theorem

## Immediate Comment / Docstring

```lean
-- CRT round-trip [II.T30]
```

## Source Excerpt

```lean
theorem crt_roundtrip_3 :
    crt_roundtrip_check 3 = true := by native_decide
```
