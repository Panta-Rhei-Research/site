---
{
  "projection_kind": "taulib_declaration",
  "title": "example at L214",
  "permalink": "/verify/taulib/docs/book-i-holomorphy-identity-theorem/example-l214/",
  "summary_short": "`example` declaration in `TauLib.BookI.Holomorphy.IdentityTheorem`.",
  "declaration_id": "TauLib.BookI.Holomorphy.IdentityTheorem::#eval:214",
  "declaration_slug": "example-l214",
  "kind": "example",
  "name": null,
  "module_name": "TauLib.BookI.Holomorphy.IdentityTheorem",
  "module_url": "/verify/taulib/docs/book-i-holomorphy-identity-theorem/",
  "source_line_start": 214,
  "source_line_end": 214,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/IdentityTheorem.lean#L214-L214",
  "formal_status": "example",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Holomorphy.IdentityTheorem",
        "url": "/verify/taulib/docs/book-i-holomorphy-identity-theorem/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/IdentityTheorem.lean#L214-L214",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "example",
      "status": "example"
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

- Module: [TauLib.BookI.Holomorphy.IdentityTheorem](/verify/taulib/docs/book-i-holomorphy-identity-theorem/)
- Source path: [`TauLib/BookI/Holomorphy/IdentityTheorem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/IdentityTheorem.lean#L214-L214)
- Source range: L214-L214
- Kind: `example`
- Formal status hint: `example`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Verification: χ₊ and χ₋ disagree at stage 1 for input 1.
    (Input 2 gives reduce(2,1)=0, so they vacuously agree there.) -/
```

## Source Excerpt

```lean
example : agree_at_check chi_plus_stage chi_minus_stage 1 1 = false := by native_decide
```
