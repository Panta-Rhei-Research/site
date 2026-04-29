---
{
  "projection_kind": "taulib_declaration",
  "title": "homology_trivial_check",
  "permalink": "/verify/taulib/docs/book-ii-enrichment-homological/homology-trivial-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Enrichment.Homological`.",
  "declaration_id": "TauLib.BookII.Enrichment.Homological::homology_trivial_check",
  "declaration_slug": "homology-trivial-check",
  "kind": "def",
  "name": "homology_trivial_check",
  "module_name": "TauLib.BookII.Enrichment.Homological",
  "module_url": "/verify/taulib/docs/book-ii-enrichment-homological/",
  "source_line_start": 115,
  "source_line_end": 119,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/Homological.lean#L115-L119",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/Homological.lean#L115-L119",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
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

- Module: [TauLib.BookII.Enrichment.Homological](/verify/taulib/docs/book-ii-enrichment-homological/)
- Source path: [`TauLib/BookII/Enrichment/Homological.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/Homological.lean#L115-L119)
- Source range: L115-L119
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D85` — Homology via SES

## Immediate Comment / Docstring

```lean
/-- [II.D85] Homology is trivial: |ker(g)| = |im(f)| = M_{k-1}. -/
```

## Source Excerpt

```lean
def homology_trivial_check (k : Nat) : Bool :=
  if k == 0 then true
  else
    let expected := primorial (k - 1)
    ses_kernel_size k == expected
```
