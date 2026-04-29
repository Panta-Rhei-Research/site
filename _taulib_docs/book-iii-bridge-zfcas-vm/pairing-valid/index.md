---
{
  "projection_kind": "taulib_declaration",
  "title": "pairing_valid",
  "permalink": "/verify/taulib/docs/book-iii-bridge-zfcas-vm/pairing-valid/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Bridge.ZFCasVM`.",
  "declaration_id": "TauLib.BookIII.Bridge.ZFCasVM::pairing_valid",
  "declaration_slug": "pairing-valid",
  "kind": "theorem",
  "name": "pairing_valid",
  "module_name": "TauLib.BookIII.Bridge.ZFCasVM",
  "module_url": "/verify/taulib/docs/book-iii-bridge-zfcas-vm/",
  "source_line_start": 301,
  "source_line_end": 302,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/ZFCasVM.lean#L301-L302",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/ZFCasVM.lean#L301-L302",
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
- Source path: [`TauLib/BookIII/Bridge/ZFCasVM.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/ZFCasVM.lean#L301-L302)
- Source range: L301-L302
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.D67` — ZFC as E₂ VM

## Immediate Comment / Docstring

```lean
/-- [III.D67] Structural: pairing at depth 3 produces valid result. -/
```

## Source Excerpt

```lean
theorem pairing_valid :
    axiom_operation .pairing 3 5 3 < 30 := by native_decide
```
