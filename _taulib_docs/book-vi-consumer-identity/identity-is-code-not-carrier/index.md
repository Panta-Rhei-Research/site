---
{
  "projection_kind": "taulib_declaration",
  "title": "identity_is_code_not_carrier",
  "permalink": "/verify/taulib/docs/book-vi-consumer-identity/identity-is-code-not-carrier/",
  "summary_short": "`theorem` declaration in `TauLib.BookVI.Consumer.Identity`.",
  "declaration_id": "TauLib.BookVI.Consumer.Identity::identity_is_code_not_carrier",
  "declaration_slug": "identity-is-code-not-carrier",
  "kind": "theorem",
  "name": "identity_is_code_not_carrier",
  "module_name": "TauLib.BookVI.Consumer.Identity",
  "module_url": "/verify/taulib/docs/book-vi-consumer-identity/",
  "source_line_start": 65,
  "source_line_end": 68,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/Identity.lean#L65-L68",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.Consumer.Identity",
        "url": "/verify/taulib/docs/book-vi-consumer-identity/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/Identity.lean#L65-L68",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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

- Module: [TauLib.BookVI.Consumer.Identity](/verify/taulib/docs/book-vi-consumer-identity/)
- Source path: [`TauLib/BookVI/Consumer/Identity.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/Identity.lean#L65-L68)
- Source range: L65-L68
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
No immediate Lean doc/comment block was detected for this declaration.
```

## Source Excerpt

```lean
theorem identity_is_code_not_carrier :
    selfdesc_code.not_carrier = true ∧
    selfdesc_code.profinite_invariant = true :=
  ⟨rfl, rfl⟩
```
