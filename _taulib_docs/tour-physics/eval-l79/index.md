---
{
  "projection_kind": "taulib_declaration",
  "title": "eval at L79",
  "permalink": "/verify/taulib/docs/tour-physics/eval-l79/",
  "summary_short": "`eval` declaration in `TauLib.Tour.Physics`.",
  "declaration_id": "TauLib.Tour.Physics::#eval:79",
  "declaration_slug": "eval-l79",
  "kind": "eval",
  "name": null,
  "module_name": "TauLib.Tour.Physics",
  "module_url": "/verify/taulib/docs/tour-physics/",
  "source_line_start": 79,
  "source_line_end": 83,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/Tour/Physics.lean#L79-L83",
  "formal_status": "computed",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.Tour.Physics",
        "url": "/verify/taulib/docs/tour-physics/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/Tour/Physics.lean#L79-L83",
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

- Module: [TauLib.Tour.Physics](/verify/taulib/docs/tour-physics/)
- Source path: [`TauLib/Tour/Physics.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/Tour/Physics.lean#L79-L83)
- Source range: L79-L83
- Kind: `eval`
- Formal status hint: `computed`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
-- Three quark generations from primitive winding classes on T²:
```

## Source Excerpt

```lean
#eval quark_winding_classes.length  -- 3

-- The Koide relation Q = 2/3 is a structural consequence of
-- ℤ/3ℤ symmetry on the lemniscate:
#check koide_predicted_2_over_3     -- koide_relation.predicted_numer = 2 ∧ .predicted_denom = 3
```
