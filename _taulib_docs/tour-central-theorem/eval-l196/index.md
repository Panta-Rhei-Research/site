---
{
  "projection_kind": "taulib_declaration",
  "title": "eval at L196",
  "permalink": "/verify/taulib/docs/tour-central-theorem/eval-l196/",
  "summary_short": "`eval` declaration in `TauLib.Tour.CentralTheorem`.",
  "declaration_id": "TauLib.Tour.CentralTheorem::#eval:196",
  "declaration_slug": "eval-l196",
  "kind": "eval",
  "name": null,
  "module_name": "TauLib.Tour.CentralTheorem",
  "module_url": "/verify/taulib/docs/tour-central-theorem/",
  "source_line_start": 196,
  "source_line_end": 201,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/Tour/CentralTheorem.lean#L196-L201",
  "formal_status": "computed",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.Tour.CentralTheorem",
        "url": "/verify/taulib/docs/tour-central-theorem/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/Tour/CentralTheorem.lean#L196-L201",
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

- Module: [TauLib.Tour.CentralTheorem](/verify/taulib/docs/tour-central-theorem/)
- Source path: [`TauLib/Tour/CentralTheorem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/Tour/CentralTheorem.lean#L196-L201)
- Source range: L196-L201
- Kind: `eval`
- Formal status hint: `computed`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
No immediate Lean doc/comment block was detected for this declaration.
```

## Source Excerpt

```lean
#eval central_theorem_forward_check 3 15      -- true

-- INVERSE direction: every holomorphic function restricts to boundary data.
-- Given a tower-coherent function, its restriction to the primorial lattice
-- yields a well-defined spectral algebra element.
#check hol_to_spectral                -- StageFun -> (x, k) -> SectorPair
```
