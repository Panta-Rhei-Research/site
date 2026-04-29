---
{
  "projection_kind": "taulib_declaration",
  "title": "eval at L361",
  "permalink": "/verify/taulib/docs/book-ii-central-theorem-central-theorem/eval-l361/",
  "summary_short": "`eval` declaration in `TauLib.BookII.CentralTheorem.CentralTheorem`.",
  "declaration_id": "TauLib.BookII.CentralTheorem.CentralTheorem::#eval:361",
  "declaration_slug": "eval-l361",
  "kind": "eval",
  "name": null,
  "module_name": "TauLib.BookII.CentralTheorem.CentralTheorem",
  "module_url": "/verify/taulib/docs/book-ii-central-theorem-central-theorem/",
  "source_line_start": 361,
  "source_line_end": 364,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/CentralTheorem.lean#L361-L364",
  "formal_status": "computed",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.CentralTheorem.CentralTheorem",
        "url": "/verify/taulib/docs/book-ii-central-theorem-central-theorem/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/CentralTheorem.lean#L361-L364",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "eval",
      "status": "computed"
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

- Module: [TauLib.BookII.CentralTheorem.CentralTheorem](/verify/taulib/docs/book-ii-central-theorem-central-theorem/)
- Source path: [`TauLib/BookII/CentralTheorem/CentralTheorem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/CentralTheorem.lean#L361-L364)
- Source range: L361-L364
- Kind: `eval`
- Formal status hint: `computed`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
-- Round-trip example
```

## Source Excerpt

```lean
#eval let rx := reduce 7 2
      let hol := hol_to_spectral id_stage 7 2
      let sp := spectral_to_hol (fun n => (n : Int)) (fun n => (n : Int)) 7 2
      (rx, hol, sp)  -- (1, (1, 1), (1, 1))
```
