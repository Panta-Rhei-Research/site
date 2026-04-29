---
{
  "projection_kind": "taulib_declaration",
  "title": "id_admissible",
  "permalink": "/verify/taulib/docs/book-iii-computation-admissibility/id-admissible/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Computation.Admissibility`.",
  "declaration_id": "TauLib.BookIII.Computation.Admissibility::id_admissible",
  "declaration_slug": "id-admissible",
  "kind": "theorem",
  "name": "id_admissible",
  "module_name": "TauLib.BookIII.Computation.Admissibility",
  "module_url": "/verify/taulib/docs/book-iii-computation-admissibility/",
  "source_line_start": 235,
  "source_line_end": 238,
  "registry_ids": [
    "III.P21"
  ],
  "related_registry_items": [
    {
      "id": "III.P21",
      "title": "Earned Admissibility",
      "url": "/registry/object/III.P21/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/Admissibility.lean#L235-L238",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/Admissibility.lean#L235-L238",
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
- Source path: [`TauLib/BookIII/Computation/Admissibility.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/Admissibility.lean#L235-L238)
- Source range: L235-L238
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.P21` — Earned Admissibility

## Immediate Comment / Docstring

```lean
/-- [III.P21] Structural: identity is trivially admissible. -/
```

## Source Excerpt

```lean
theorem id_admissible :
    earned_admissibility_check 10 1 = true := by native_decide

end Tau.BookIII.Computation
```
