---
{
  "projection_kind": "taulib_declaration",
  "title": "ses_exact_2",
  "permalink": "/verify/taulib/docs/book-ii-enrichment-homological/ses-exact-2/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Enrichment.Homological`.",
  "declaration_id": "TauLib.BookII.Enrichment.Homological::ses_exact_2",
  "declaration_slug": "ses-exact-2",
  "kind": "theorem",
  "name": "ses_exact_2",
  "module_name": "TauLib.BookII.Enrichment.Homological",
  "module_url": "/verify/taulib/docs/book-ii-enrichment-homological/",
  "source_line_start": 179,
  "source_line_end": 180,
  "registry_ids": [
    "II.D85"
  ],
  "related_registry_items": [
    {
      "id": "II.D85",
      "title": "Homology via SES",
      "url": "/registry/object/II.D85/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/Homological.lean#L179-L180",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Enrichment.Homological",
        "url": "/verify/taulib/docs/book-ii-enrichment-homological/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/Homological.lean#L179-L180",
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

- Module: [TauLib.BookII.Enrichment.Homological](/verify/taulib/docs/book-ii-enrichment-homological/)
- Source path: [`TauLib/BookII/Enrichment/Homological.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/Homological.lean#L179-L180)
- Source range: L179-L180
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `II.D85` — Homology via SES

## Immediate Comment / Docstring

```lean
/-- [II.D85] SES exactness at stage 2. -/
```

## Source Excerpt

```lean
theorem ses_exact_2 :
    ses_exactness_check 2 = true := by native_decide
```
