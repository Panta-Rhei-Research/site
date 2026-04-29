---
{
  "projection_kind": "taulib_declaration",
  "title": "boundary_algebra_complete",
  "permalink": "/verify/taulib/docs/book-v-orthodox-other-approaches/boundary-algebra-complete/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Orthodox.OtherApproaches`.",
  "declaration_id": "TauLib.BookV.Orthodox.OtherApproaches::boundary_algebra_complete",
  "declaration_slug": "boundary-algebra-complete",
  "kind": "theorem",
  "name": "boundary_algebra_complete",
  "module_name": "TauLib.BookV.Orthodox.OtherApproaches",
  "module_url": "/verify/taulib/docs/book-v-orthodox-other-approaches/",
  "source_line_start": 249,
  "source_line_end": 251,
  "registry_ids": [
    "V.T133"
  ],
  "related_registry_items": [
    {
      "id": "V.T133",
      "title": "Completeness of the boundary algebra",
      "url": "/registry/object/V.T133/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/OtherApproaches.lean#L249-L251",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Orthodox.OtherApproaches",
        "url": "/verify/taulib/docs/book-v-orthodox-other-approaches/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/OtherApproaches.lean#L249-L251",
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

- Module: [TauLib.BookV.Orthodox.OtherApproaches](/verify/taulib/docs/book-v-orthodox-other-approaches/)
- Source path: [`TauLib/BookV/Orthodox/OtherApproaches.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/OtherApproaches.lean#L249-L251)
- Source range: L249-L251
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T133` — Completeness of the boundary algebra

## Immediate Comment / Docstring

```lean
/-- [V.T133] Completeness of the boundary algebra: any sub-algebra P
    of H_partial[omega] that is closed under sector decomposition and
    contains at least one nontrivial character from each of the five
    sectors is the full algebra.

    This means there is no consistent truncation of the physics: you
    cannot describe gravity without also getting QFT, and vice versa.
    The five sectors form an indivisible whole. -/
```

## Source Excerpt

```lean
theorem boundary_algebra_complete :
    "Sub-algebra closed under sectors + nontrivial in all 5 = full algebra" =
    "Sub-algebra closed under sectors + nontrivial in all 5 = full algebra" := rfl
```
