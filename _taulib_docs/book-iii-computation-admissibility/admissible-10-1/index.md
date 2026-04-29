---
{
  "projection_kind": "taulib_declaration",
  "title": "admissible_10_1",
  "permalink": "/verify/taulib/docs/book-iii-computation-admissibility/admissible-10-1/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Computation.Admissibility`.",
  "declaration_id": "TauLib.BookIII.Computation.Admissibility::admissible_10_1",
  "declaration_slug": "admissible-10-1",
  "kind": "theorem",
  "name": "admissible_10_1",
  "module_name": "TauLib.BookIII.Computation.Admissibility",
  "module_url": "/verify/taulib/docs/book-iii-computation-admissibility/",
  "source_line_start": 231,
  "source_line_end": 232,
  "registry_ids": [
    "III.D54"
  ],
  "related_registry_items": [
    {
      "id": "III.D54",
      "title": "τ-Admissibility (E₂)",
      "url": "/registry/object/III.D54/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/Admissibility.lean#L231-L232",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Computation.Admissibility",
        "url": "/verify/taulib/docs/book-iii-computation-admissibility/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/Admissibility.lean#L231-L232",
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

- Module: [TauLib.BookIII.Computation.Admissibility](/verify/taulib/docs/book-iii-computation-admissibility/)
- Source path: [`TauLib/BookIII/Computation/Admissibility.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/Admissibility.lean#L231-L232)
- Source range: L231-L232
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.D54` — τ-Admissibility (E₂)

## Immediate Comment / Docstring

```lean
/-- [III.D54] Structural: admissibility at depth 1. -/
```

## Source Excerpt

```lean
theorem admissible_10_1 :
    tau_admissible_check 10 1 = true := by native_decide
```
