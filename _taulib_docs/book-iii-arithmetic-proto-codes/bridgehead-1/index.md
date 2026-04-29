---
{
  "projection_kind": "taulib_declaration",
  "title": "bridgehead_1",
  "permalink": "/verify/taulib/docs/book-iii-arithmetic-proto-codes/bridgehead-1/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Arithmetic.ProtoCodes`.",
  "declaration_id": "TauLib.BookIII.Arithmetic.ProtoCodes::bridgehead_1",
  "declaration_slug": "bridgehead-1",
  "kind": "theorem",
  "name": "bridgehead_1",
  "module_name": "TauLib.BookIII.Arithmetic.ProtoCodes",
  "module_url": "/verify/taulib/docs/book-iii-arithmetic-proto-codes/",
  "source_line_start": 183,
  "source_line_end": 186,
  "registry_ids": [
    "III.P26"
  ],
  "related_registry_items": [
    {
      "id": "III.P26",
      "title": "Bridgehead Proposition",
      "url": "/registry/object/III.P26/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/ProtoCodes.lean#L183-L186",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Arithmetic.ProtoCodes",
        "url": "/verify/taulib/docs/book-iii-arithmetic-proto-codes/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/ProtoCodes.lean#L183-L186",
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

- Module: [TauLib.BookIII.Arithmetic.ProtoCodes](/verify/taulib/docs/book-iii-arithmetic-proto-codes/)
- Source path: [`TauLib/BookIII/Arithmetic/ProtoCodes.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/ProtoCodes.lean#L183-L186)
- Source range: L183-L186
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.P26` — Bridgehead Proposition

## Immediate Comment / Docstring

```lean
/-- [III.P26] Structural: bridgehead at depth 1. -/
```

## Source Excerpt

```lean
theorem bridgehead_1 :
    bridgehead_check 1 = true := by native_decide

end Tau.BookIII.Arithmetic
```
