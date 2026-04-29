---
{
  "projection_kind": "taulib_declaration",
  "title": "compute_e1_export",
  "permalink": "/verify/taulib/docs/book-ii-closure-forward-book3/compute-e1-export/",
  "summary_short": "`def` declaration in `TauLib.BookII.Closure.ForwardBook3`.",
  "declaration_id": "TauLib.BookII.Closure.ForwardBook3::compute_e1_export",
  "declaration_slug": "compute-e1-export",
  "kind": "def",
  "name": "compute_e1_export",
  "module_name": "TauLib.BookII.Closure.ForwardBook3",
  "module_url": "/verify/taulib/docs/book-ii-closure-forward-book3/",
  "source_line_start": 63,
  "source_line_end": 70,
  "registry_ids": [
    "II.D66"
  ],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/ForwardBook3.lean#L63-L70",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Closure.ForwardBook3",
        "url": "/verify/taulib/docs/book-ii-closure-forward-book3/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/ForwardBook3.lean#L63-L70",
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

- Module: [TauLib.BookII.Closure.ForwardBook3](/verify/taulib/docs/book-ii-closure-forward-book3/)
- Source path: [`TauLib/BookII/Closure/ForwardBook3.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/ForwardBook3.lean#L63-L70)
- Source range: L63-L70
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [II.D66] Compute the E1 Export Package by evaluating all components.
    Parameters control the verification depth:
    - db: max stage depth for tower checks
    - bound: max input value for range checks
    - k_max: max stage for Code/Decode checks -/
```

## Source Excerpt

```lean
def compute_e1_export (db bound k_max : TauIdx) : E1ExportPackage :=
  { e1_layer_complete := e1_layer_check bound db k_max
  , central_theorem_verified := central_theorem_check db bound
  , categoricity_verified := categoricity_check db bound
  , enrichment_ladder_verified := full_enrichment_ladder_check bound db k_max
  , tau_manifold_verified := tau_manifold_check db bound
  , proto_rationality_verified := proto_rational_check bound 5
  }
```
