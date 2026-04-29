---
{
  "projection_kind": "taulib_declaration",
  "title": "no_knobs_check",
  "permalink": "/verify/taulib/docs/book-iii-hinge-hinge-theorem/no-knobs-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Hinge.HingeTheorem`.",
  "declaration_id": "TauLib.BookIII.Hinge.HingeTheorem::no_knobs_check",
  "declaration_slug": "no-knobs-check",
  "kind": "def",
  "name": "no_knobs_check",
  "module_name": "TauLib.BookIII.Hinge.HingeTheorem",
  "module_url": "/verify/taulib/docs/book-iii-hinge-hinge-theorem/",
  "source_line_start": 260,
  "source_line_end": 263,
  "registry_ids": [
    "III.T42"
  ],
  "related_registry_items": [
    {
      "id": "III.T42",
      "title": "No Knobs Theorem",
      "url": "/registry/object/III.T42/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Hinge/HingeTheorem.lean#L260-L263",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Hinge.HingeTheorem",
        "url": "/verify/taulib/docs/book-iii-hinge-hinge-theorem/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Hinge/HingeTheorem.lean#L260-L263",
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

- Module: [TauLib.BookIII.Hinge.HingeTheorem](/verify/taulib/docs/book-iii-hinge-hinge-theorem/)
- Source path: [`TauLib/BookIII/Hinge/HingeTheorem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Hinge/HingeTheorem.lean#L260-L263)
- Source range: L260-L263
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.T42` — No Knobs Theorem

## Immediate Comment / Docstring

```lean
/-- [III.T42] No-knobs check: iota_tau determines ratio + no free parameters
    + coupling uniqueness. The single constant 341304/1000000 controls
    everything downstream of the seven axioms. -/
```

## Source Excerpt

```lean
def no_knobs_check (bound db : TauIdx) : Bool :=
  iota_determines_ratio db &&
  no_free_parameters_check bound db &&
  coupling_uniqueness_check bound db
```
