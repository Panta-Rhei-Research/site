---
{
  "projection_kind": "taulib_declaration",
  "title": "bc_distinct_3",
  "permalink": "/verify/taulib/docs/book-iii-spectral-trichotomy/bc-distinct-3/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Spectral.Trichotomy`.",
  "declaration_id": "TauLib.BookIII.Spectral.Trichotomy::bc_distinct_3",
  "declaration_slug": "bc-distinct-3",
  "kind": "theorem",
  "name": "bc_distinct_3",
  "module_name": "TauLib.BookIII.Spectral.Trichotomy",
  "module_url": "/verify/taulib/docs/book-iii-spectral-trichotomy/",
  "source_line_start": 316,
  "source_line_end": 319,
  "registry_ids": [
    "III.T15"
  ],
  "related_registry_items": [
    {
      "id": "III.T15",
      "title": "B/C Non-Collapse Theorem",
      "url": "/registry/object/III.T15/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/Trichotomy.lean#L316-L319",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Spectral.Trichotomy",
        "url": "/verify/taulib/docs/book-iii-spectral-trichotomy/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/Trichotomy.lean#L316-L319",
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

- Module: [TauLib.BookIII.Spectral.Trichotomy](/verify/taulib/docs/book-iii-spectral-trichotomy/)
- Source path: [`TauLib/BookIII/Spectral/Trichotomy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/Trichotomy.lean#L316-L319)
- Source range: L316-L319
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.T15` — B/C Non-Collapse Theorem

## Immediate Comment / Docstring

```lean
/-- [III.T15] Structural: B-product ≠ C-product at depth 3. -/
```

## Source Excerpt

```lean
theorem bc_distinct_3 :
    compute_label_product .B 3 ≠ compute_label_product .C 3 := by native_decide

end Tau.BookIII.Spectral
```
