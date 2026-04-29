---
{
  "projection_kind": "taulib_declaration",
  "title": "trichotomy_depth_1",
  "permalink": "/verify/taulib/docs/book-iii-spectral-trichotomy/trichotomy-depth-1/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Spectral.Trichotomy`.",
  "declaration_id": "TauLib.BookIII.Spectral.Trichotomy::trichotomy_depth_1",
  "declaration_slug": "trichotomy-depth-1",
  "kind": "theorem",
  "name": "trichotomy_depth_1",
  "module_name": "TauLib.BookIII.Spectral.Trichotomy",
  "module_url": "/verify/taulib/docs/book-iii-spectral-trichotomy/",
  "source_line_start": 300,
  "source_line_end": 301,
  "registry_ids": [
    "III.T14"
  ],
  "related_registry_items": [
    {
      "id": "III.T14",
      "title": "Spectral Trichotomy Lemma",
      "url": "/registry/object/III.T14/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/Trichotomy.lean#L300-L301",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/Trichotomy.lean#L300-L301",
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
- Source path: [`TauLib/BookIII/Spectral/Trichotomy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/Trichotomy.lean#L300-L301)
- Source range: L300-L301
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.T14` — Spectral Trichotomy Lemma

## Immediate Comment / Docstring

```lean
/-- [III.T14] Structural: trichotomy at depth 1 has only X-component
    (only prime is 2, which is X-type). -/
```

## Source Excerpt

```lean
theorem trichotomy_depth_1 :
    (trichotomy_decompose [1] 1).1 = [0] := by native_decide
```
