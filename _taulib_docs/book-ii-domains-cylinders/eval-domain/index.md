---
{
  "projection_kind": "taulib_declaration",
  "title": "eval_domain",
  "permalink": "/verify/taulib/docs/book-ii-domains-cylinders/eval-domain/",
  "summary_short": "`def` declaration in `TauLib.BookII.Domains.Cylinders`.",
  "declaration_id": "TauLib.BookII.Domains.Cylinders::eval_domain",
  "declaration_slug": "eval-domain",
  "kind": "def",
  "name": "eval_domain",
  "module_name": "TauLib.BookII.Domains.Cylinders",
  "module_url": "/verify/taulib/docs/book-ii-domains-cylinders/",
  "source_line_start": 61,
  "source_line_end": 66,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Domains/Cylinders.lean#L61-L66",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Domains.Cylinders",
        "url": "/verify/taulib/docs/book-ii-domains-cylinders/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Domains/Cylinders.lean#L61-L66",
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

- Module: [TauLib.BookII.Domains.Cylinders](/verify/taulib/docs/book-ii-domains-cylinders/)
- Source path: [`TauLib/BookII/Domains/Cylinders.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Domains/Cylinders.lean#L61-L66)
- Source range: L61-L66
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Evaluate membership in a cylinder domain. -/
```

## Source Excerpt

```lean
def eval_domain (d : CylinderDomain) (y : TauIdx) : Bool :=
  match d with
  | .basic k c => cylinder_mem k c y
  | .inter a b => eval_domain a y && eval_domain b y
  | .union a b => eval_domain a y || eval_domain b y
  | .compl a   => !eval_domain a y
```
