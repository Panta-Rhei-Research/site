---
{
  "projection_kind": "taulib_declaration",
  "title": "base_change_10_1",
  "permalink": "/verify/taulib/docs/book-iii-arithmetic-langlands/base-change-10-1/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Arithmetic.Langlands`.",
  "declaration_id": "TauLib.BookIII.Arithmetic.Langlands::base_change_10_1",
  "declaration_slug": "base-change-10-1",
  "kind": "theorem",
  "name": "base_change_10_1",
  "module_name": "TauLib.BookIII.Arithmetic.Langlands",
  "module_url": "/verify/taulib/docs/book-iii-arithmetic-langlands/",
  "source_line_start": 231,
  "source_line_end": 234,
  "registry_ids": [
    "III.T37"
  ],
  "related_registry_items": [
    {
      "id": "III.T37",
      "title": "Base Change-Transfer Naturality",
      "url": "/registry/object/III.T37/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/Langlands.lean#L231-L234",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Arithmetic.Langlands",
        "url": "/verify/taulib/docs/book-iii-arithmetic-langlands/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/Langlands.lean#L231-L234",
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

- Module: [TauLib.BookIII.Arithmetic.Langlands](/verify/taulib/docs/book-iii-arithmetic-langlands/)
- Source path: [`TauLib/BookIII/Arithmetic/Langlands.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/Langlands.lean#L231-L234)
- Source range: L231-L234
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.T37` — Base Change-Transfer Naturality

## Immediate Comment / Docstring

```lean
/-- [III.T37] Structural: base change at depth 1. -/
```

## Source Excerpt

```lean
theorem base_change_10_1 :
    base_change_check 10 1 = true := by native_decide

end Tau.BookIII.Arithmetic
```
