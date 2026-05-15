---
{
  "projection_kind": "taulib_declaration",
  "title": "eval at L242",
  "permalink": "/corpus/taulib/docs/book-i-holomorphy-identity-theorem/eval-l242/",
  "summary_short": "`eval` declaration in `TauLib.BookI.Holomorphy.IdentityTheorem`.",
  "declaration_id": "TauLib.BookI.Holomorphy.IdentityTheorem::#eval:242",
  "declaration_slug": "eval-l242",
  "kind": "eval",
  "name": null,
  "module_name": "TauLib.BookI.Holomorphy.IdentityTheorem",
  "module_url": "/corpus/taulib/docs/book-i-holomorphy-identity-theorem/",
  "source_line_start": 242,
  "source_line_end": 244,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/IdentityTheorem.lean#L242-L244",
  "formal_status": "computed",
  "declaration_role": "computed check",
  "formal_status_label": "computed check",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Holomorphy.IdentityTheorem",
        "url": "/corpus/taulib/docs/book-i-holomorphy-identity-theorem/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/IdentityTheorem.lean#L242-L244",
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

- Module: [TauLib.BookI.Holomorphy.IdentityTheorem](/corpus/taulib/docs/book-i-holomorphy-identity-theorem/)
- Source path: [`TauLib/BookI/Holomorphy/IdentityTheorem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/IdentityTheorem.lean#L242-L244)
- Source range: L242-L244
- Kind: `eval`
- Public role: `computed check`
- Formal status hint: `computed check`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
-- Identity theorem witness: chi_plus and id disagree at stage 2 for n=3
```

## Source Excerpt

```lean
#eval agree_at_check chi_plus_stage id_stage 3 2   -- false: B agrees but C differs

end Tau.Holomorphy
```
