---
{
  "projection_kind": "taulib_declaration",
  "title": "eval at L206",
  "permalink": "/corpus/taulib/docs/tour-central-theorem/eval-l206/",
  "summary_short": "`eval` declaration in `TauLib.Tour.CentralTheorem`.",
  "declaration_id": "TauLib.Tour.CentralTheorem::#eval:206",
  "declaration_slug": "eval-l206",
  "kind": "eval",
  "name": null,
  "module_name": "TauLib.Tour.CentralTheorem",
  "module_url": "/corpus/taulib/docs/tour-central-theorem/",
  "source_line_start": 206,
  "source_line_end": 209,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/Tour/CentralTheorem.lean#L206-L209",
  "formal_status": "computed",
  "declaration_role": "computed check",
  "formal_status_label": "computed check",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.Tour.CentralTheorem",
        "url": "/corpus/taulib/docs/tour-central-theorem/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/Tour/CentralTheorem.lean#L206-L209",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "eval",
      "role": "computed check",
      "status": "computed check"
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

- Module: [TauLib.Tour.CentralTheorem](/corpus/taulib/docs/tour-central-theorem/)
- Source path: [`TauLib/Tour/CentralTheorem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/Tour/CentralTheorem.lean#L206-L209)
- Source range: L206-L209
- Kind: `eval`
- Public role: `computed check`
- Formal status hint: `computed check`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
-- ROUND-TRIP: both compositions are the identity.
-- forward . inverse = id AND inverse . forward = id.
```

## Source Excerpt

```lean
#eval central_theorem_roundtrip_check 3 15    -- true

-- Structural round-trip theorem (for identity function):
#check central_roundtrip
```
