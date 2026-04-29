---
{
  "projection_kind": "taulib_declaration",
  "title": "no_singularity_instance",
  "permalink": "/verify/taulib/docs/book-v-orthodox-emergent-geometry/no-singularity-instance/",
  "summary_short": "`def` declaration in `TauLib.BookV.Orthodox.EmergentGeometry`.",
  "declaration_id": "TauLib.BookV.Orthodox.EmergentGeometry::no_singularity_instance",
  "declaration_slug": "no-singularity-instance",
  "kind": "def",
  "name": "no_singularity_instance",
  "module_name": "TauLib.BookV.Orthodox.EmergentGeometry",
  "module_url": "/verify/taulib/docs/book-v-orthodox-emergent-geometry/",
  "source_line_start": 167,
  "source_line_end": 170,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/EmergentGeometry.lean#L167-L170",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Orthodox.EmergentGeometry",
        "url": "/verify/taulib/docs/book-v-orthodox-emergent-geometry/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/EmergentGeometry.lean#L167-L170",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "status": "defined"
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

- Module: [TauLib.BookV.Orthodox.EmergentGeometry](/verify/taulib/docs/book-v-orthodox-emergent-geometry/)
- Source path: [`TauLib/BookV/Orthodox/EmergentGeometry.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/EmergentGeometry.lean#L167-L170)
- Source range: L167-L170
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- No singularity in the tau-Einstein equation. -/
```

## Source Excerpt

```lean
def no_singularity_instance : NoSingularity where
  finite_at_depth := true
  coupling_finite := true
  stress_bounded := true
```
