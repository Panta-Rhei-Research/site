---
{
  "projection_kind": "taulib_declaration",
  "title": "ising_periodic_bc",
  "permalink": "/verify/taulib/docs/book-iv-many-body-magnetism/ising-periodic-bc/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.ManyBody.Magnetism`.",
  "declaration_id": "TauLib.BookIV.ManyBody.Magnetism::ising_periodic_bc",
  "declaration_slug": "ising-periodic-bc",
  "kind": "theorem",
  "name": "ising_periodic_bc",
  "module_name": "TauLib.BookIV.ManyBody.Magnetism",
  "module_url": "/verify/taulib/docs/book-iv-many-body-magnetism/",
  "source_line_start": 86,
  "source_line_end": 87,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/Magnetism.lean#L86-L87",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.ManyBody.Magnetism",
        "url": "/verify/taulib/docs/book-iv-many-body-magnetism/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/Magnetism.lean#L86-L87",
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

- Module: [TauLib.BookIV.ManyBody.Magnetism](/verify/taulib/docs/book-iv-many-body-magnetism/)
- Source path: [`TauLib/BookIV/ManyBody/Magnetism.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/Magnetism.lean#L86-L87)
- Source range: L86-L87
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
No immediate Lean doc/comment block was detected for this declaration.
```

## Source Excerpt

```lean
theorem ising_periodic_bc :
    ising_hamiltonian.periodic_from_torus = true := rfl
```
