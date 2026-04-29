---
{
  "projection_kind": "taulib_declaration",
  "title": "StrongCurvature",
  "permalink": "/verify/taulib/docs/book-iv-strong-yang-mills-gap/strong-curvature/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Strong.YangMillsGap`.",
  "declaration_id": "TauLib.BookIV.Strong.YangMillsGap::StrongCurvature",
  "declaration_slug": "strong-curvature",
  "kind": "structure",
  "name": "StrongCurvature",
  "module_name": "TauLib.BookIV.Strong.YangMillsGap",
  "module_url": "/verify/taulib/docs/book-iv-strong-yang-mills-gap/",
  "source_line_start": 92,
  "source_line_end": 99,
  "registry_ids": [
    "IV.D171"
  ],
  "related_registry_items": [
    {
      "id": "IV.D171",
      "title": "Strong curvature",
      "url": "/registry/object/IV.D171/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/YangMillsGap.lean#L92-L99",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Strong.YangMillsGap",
        "url": "/verify/taulib/docs/book-iv-strong-yang-mills-gap/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/YangMillsGap.lean#L92-L99",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
      "status": "defined"
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

- Module: [TauLib.BookIV.Strong.YangMillsGap](/verify/taulib/docs/book-iv-strong-yang-mills-gap/)
- Source path: [`TauLib/BookIV/Strong/YangMillsGap.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/YangMillsGap.lean#L92-L99)
- Source range: L92-L99
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D171` — Strong curvature

## Immediate Comment / Docstring

```lean
/-- [IV.D171] Strong curvature F_n^s(Box) at a plaquette:
    norm of ordered composition of connection automorphisms around
    an elementary closed path minus the identity.
    F = 0 iff the connection is flat on that plaquette. -/
```

## Source Excerpt

```lean
structure StrongCurvature where
  /-- Measures departure from flatness. -/
  measures_flatness_departure : Bool := true
  /-- Zero iff locally flat. -/
  zero_iff_flat : Bool := true
  /-- Non-negative valued. -/
  nonneg : Bool := true
  deriving Repr
```
