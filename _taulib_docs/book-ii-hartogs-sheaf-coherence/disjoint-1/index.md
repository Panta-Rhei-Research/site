---
{
  "projection_kind": "taulib_declaration",
  "title": "disjoint_1",
  "permalink": "/verify/taulib/docs/book-ii-hartogs-sheaf-coherence/disjoint-1/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Hartogs.SheafCoherence`.",
  "declaration_id": "TauLib.BookII.Hartogs.SheafCoherence::disjoint_1",
  "declaration_slug": "disjoint-1",
  "kind": "theorem",
  "name": "disjoint_1",
  "module_name": "TauLib.BookII.Hartogs.SheafCoherence",
  "module_url": "/verify/taulib/docs/book-ii-hartogs-sheaf-coherence/",
  "source_line_start": 459,
  "source_line_end": 460,
  "registry_ids": [
    "II.L06"
  ],
  "related_registry_items": [
    {
      "id": "II.L06",
      "title": "Gluing Lemma",
      "url": "/registry/object/II.L06/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/SheafCoherence.lean#L459-L460",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Hartogs.SheafCoherence",
        "url": "/verify/taulib/docs/book-ii-hartogs-sheaf-coherence/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/SheafCoherence.lean#L459-L460",
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

- Module: [TauLib.BookII.Hartogs.SheafCoherence](/verify/taulib/docs/book-ii-hartogs-sheaf-coherence/)
- Source path: [`TauLib/BookII/Hartogs/SheafCoherence.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/SheafCoherence.lean#L459-L460)
- Source range: L459-L460
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `II.L06` — Gluing Lemma

## Immediate Comment / Docstring

```lean
-- Same-stage disjointness [II.L06]
```

## Source Excerpt

```lean
theorem disjoint_1 :
    batch_disjoint_check 1 = true := by native_decide
```
