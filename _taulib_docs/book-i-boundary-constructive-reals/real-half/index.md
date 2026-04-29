---
{
  "projection_kind": "taulib_declaration",
  "title": "real_half",
  "permalink": "/verify/taulib/docs/book-i-boundary-constructive-reals/real-half/",
  "summary_short": "`def` declaration in `TauLib.BookI.Boundary.ConstructiveReals`.",
  "declaration_id": "TauLib.BookI.Boundary.ConstructiveReals::real_half",
  "declaration_slug": "real-half",
  "kind": "def",
  "name": "real_half",
  "module_name": "TauLib.BookI.Boundary.ConstructiveReals",
  "module_url": "/verify/taulib/docs/book-i-boundary-constructive-reals/",
  "source_line_start": 417,
  "source_line_end": 417,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/ConstructiveReals.lean#L417-L417",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.ConstructiveReals",
        "url": "/verify/taulib/docs/book-i-boundary-constructive-reals/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/ConstructiveReals.lean#L417-L417",
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

- Module: [TauLib.BookI.Boundary.ConstructiveReals](/verify/taulib/docs/book-i-boundary-constructive-reals/)
- Source path: [`TauLib/BookI/Boundary/ConstructiveReals.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/ConstructiveReals.lean#L417-L417)
- Source range: L417-L417
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
-- ============================================================
-- SMOKE TESTS
-- ============================================================
```

## Source Excerpt

```lean
private def real_half : TauReal := TauReal.fromTauRat ⟨⟨1, 0⟩, 2, by norm_num⟩
```
