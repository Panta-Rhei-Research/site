---
{
  "projection_kind": "taulib_declaration",
  "title": "cauchy_schwarz_stage2",
  "permalink": "/verify/taulib/docs/book-ii-hartogs-l2-space/cauchy-schwarz-stage2/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Hartogs.L2Space`.",
  "declaration_id": "TauLib.BookII.Hartogs.L2Space::cauchy_schwarz_stage2",
  "declaration_slug": "cauchy-schwarz-stage2",
  "kind": "theorem",
  "name": "cauchy_schwarz_stage2",
  "module_name": "TauLib.BookII.Hartogs.L2Space",
  "module_url": "/verify/taulib/docs/book-ii-hartogs-l2-space/",
  "source_line_start": 213,
  "source_line_end": 214,
  "registry_ids": [
    "II.T53"
  ],
  "related_registry_items": [
    {
      "id": "II.T53",
      "title": "Cauchy-Schwarz Inequality",
      "url": "/registry/object/II.T53/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/L2Space.lean#L213-L214",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Hartogs.L2Space",
        "url": "/verify/taulib/docs/book-ii-hartogs-l2-space/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/L2Space.lean#L213-L214",
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

- Module: [TauLib.BookII.Hartogs.L2Space](/verify/taulib/docs/book-ii-hartogs-l2-space/)
- Source path: [`TauLib/BookII/Hartogs/L2Space.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/L2Space.lean#L213-L214)
- Source range: L213-L214
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `II.T53` — Cauchy-Schwarz Inequality

## Immediate Comment / Docstring

```lean
/-- [II.T53] Cauchy-Schwarz exhaustive at stage 2. -/
```

## Source Excerpt

```lean
theorem cauchy_schwarz_stage2 :
    cauchy_schwarz_exhaustive 2 = true := by native_decide
```
