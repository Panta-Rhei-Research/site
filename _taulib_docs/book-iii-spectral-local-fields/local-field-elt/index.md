---
{
  "projection_kind": "taulib_declaration",
  "title": "LocalFieldElt",
  "permalink": "/corpus/taulib/docs/book-iii-spectral-local-fields/local-field-elt/",
  "summary_short": "`structure` declaration in `TauLib.BookIII.Spectral.LocalFields`.",
  "declaration_id": "TauLib.BookIII.Spectral.LocalFields::LocalFieldElt",
  "declaration_slug": "local-field-elt",
  "kind": "structure",
  "name": "LocalFieldElt",
  "module_name": "TauLib.BookIII.Spectral.LocalFields",
  "module_url": "/corpus/taulib/docs/book-iii-spectral-local-fields/",
  "source_line_start": 36,
  "source_line_end": 40,
  "registry_ids": [
    "III.D21"
  ],
  "related_registry_items": [
    {
      "id": "III.D21",
      "title": "τ-Native Local Field",
      "url": "/registry/object/III.D21/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/LocalFields.lean#L36-L40",
  "formal_status": "defined",
  "declaration_role": "type/data schema",
  "formal_status_label": "type/data schema",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Spectral.LocalFields",
        "url": "/corpus/taulib/docs/book-iii-spectral-local-fields/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/LocalFields.lean#L36-L40",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
      "role": "type/data schema",
      "status": "type/data schema"
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

- Module: [TauLib.BookIII.Spectral.LocalFields](/corpus/taulib/docs/book-iii-spectral-local-fields/)
- Source path: [`TauLib/BookIII/Spectral/LocalFields.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/LocalFields.lean#L36-L40)
- Source range: L36-L40
- Kind: `structure`
- Public role: `type/data schema`
- Formal status hint: `type/data schema`

## Registry Links

- `III.D21` — τ-Native Local Field

## Immediate Comment / Docstring

```lean
/-- [III.D21] A τ-native local field element at finite depth.
    Represents an element of ℤ_p^τ = lim← ℤ/p^nℤ at depth d. -/
```

## Source Excerpt

```lean
structure LocalFieldElt where
  prime : TauIdx         -- the prime p
  depth : TauIdx         -- truncation depth d
  value : TauIdx         -- value mod p^d
  deriving Repr, DecidableEq, BEq
```
