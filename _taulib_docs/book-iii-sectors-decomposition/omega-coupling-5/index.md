---
{
  "projection_kind": "taulib_declaration",
  "title": "omega_coupling_5",
  "permalink": "/verify/taulib/docs/book-iii-sectors-decomposition/omega-coupling-5/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Sectors.Decomposition`.",
  "declaration_id": "TauLib.BookIII.Sectors.Decomposition::omega_coupling_5",
  "declaration_slug": "omega-coupling-5",
  "kind": "theorem",
  "name": "omega_coupling_5",
  "module_name": "TauLib.BookIII.Sectors.Decomposition",
  "module_url": "/verify/taulib/docs/book-iii-sectors-decomposition/",
  "source_line_start": 186,
  "source_line_end": 187,
  "registry_ids": [
    "III.D14"
  ],
  "related_registry_items": [
    {
      "id": "III.D14",
      "title": "ω-Coupling Sector",
      "url": "/registry/object/III.D14/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Sectors/Decomposition.lean#L186-L187",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Sectors.Decomposition",
        "url": "/verify/taulib/docs/book-iii-sectors-decomposition/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Sectors/Decomposition.lean#L186-L187",
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

- Module: [TauLib.BookIII.Sectors.Decomposition](/verify/taulib/docs/book-iii-sectors-decomposition/)
- Source path: [`TauLib/BookIII/Sectors/Decomposition.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Sectors/Decomposition.lean#L186-L187)
- Source range: L186-L187
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.D14` — ω-Coupling Sector

## Immediate Comment / Docstring

```lean
-- ω-coupling [III.D14]
```

## Source Excerpt

```lean
theorem omega_coupling_5 :
    omega_coupling_check 5 = true := by native_decide
```
