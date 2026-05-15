---
{
  "projection_kind": "taulib_declaration",
  "title": "val_zero",
  "permalink": "/corpus/taulib/docs/book-iii-spectral-local-fields/val-zero/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Spectral.LocalFields`.",
  "declaration_id": "TauLib.BookIII.Spectral.LocalFields::val_zero",
  "declaration_slug": "val-zero",
  "kind": "theorem",
  "name": "val_zero",
  "module_name": "TauLib.BookIII.Spectral.LocalFields",
  "module_url": "/corpus/taulib/docs/book-iii-spectral-local-fields/",
  "source_line_start": 224,
  "source_line_end": 224,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/LocalFields.lean#L224-L224",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/LocalFields.lean#L224-L224",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "role": "proof obligation",
      "status": "formal proof obligation checked"
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
- Source path: [`TauLib/BookIII/Spectral/LocalFields.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/LocalFields.lean#L224-L224)
- Source range: L224-L224
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- `III.D21` — τ-Native Local Field

## Immediate Comment / Docstring

```lean
/-- [III.D21] Structural: p-adic valuation of 0 is 0 (convention). -/
```

## Source Excerpt

```lean
theorem val_zero : padic_val 0 3 = 0 := by native_decide
```
