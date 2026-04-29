---
{
  "projection_kind": "taulib_declaration",
  "title": "zfc_has_9_axioms",
  "permalink": "/verify/taulib/docs/book-iii-bridge-zfcas-vm/zfc-has-9-axioms/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Bridge.ZFCasVM`.",
  "declaration_id": "TauLib.BookIII.Bridge.ZFCasVM::zfc_has_9_axioms",
  "declaration_slug": "zfc-has-9-axioms",
  "kind": "theorem",
  "name": "zfc_has_9_axioms",
  "module_name": "TauLib.BookIII.Bridge.ZFCasVM",
  "module_url": "/verify/taulib/docs/book-iii-bridge-zfcas-vm/",
  "source_line_start": 283,
  "source_line_end": 283,
  "registry_ids": [
    "III.D67"
  ],
  "related_registry_items": [
    {
      "id": "III.D67",
      "title": "ZFC as E₂ VM",
      "url": "/registry/object/III.D67/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/ZFCasVM.lean#L283-L283",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Bridge.ZFCasVM",
        "url": "/verify/taulib/docs/book-iii-bridge-zfcas-vm/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/ZFCasVM.lean#L283-L283",
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

- Module: [TauLib.BookIII.Bridge.ZFCasVM](/verify/taulib/docs/book-iii-bridge-zfcas-vm/)
- Source path: [`TauLib/BookIII/Bridge/ZFCasVM.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/ZFCasVM.lean#L283-L283)
- Source range: L283-L283
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.D67` — ZFC as E₂ VM

## Immediate Comment / Docstring

```lean
/-- [III.D67] Structural: ZFC has exactly 9 axioms. -/
```

## Source Excerpt

```lean
theorem zfc_has_9_axioms : zfc_axiom_count = 9 := rfl
```
