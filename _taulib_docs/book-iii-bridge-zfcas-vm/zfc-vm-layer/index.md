---
{
  "projection_kind": "taulib_declaration",
  "title": "zfc_vm_layer",
  "permalink": "/verify/taulib/docs/book-iii-bridge-zfcas-vm/zfc-vm-layer/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Bridge.ZFCasVM`.",
  "declaration_id": "TauLib.BookIII.Bridge.ZFCasVM::zfc_vm_layer",
  "declaration_slug": "zfc-vm-layer",
  "kind": "def",
  "name": "zfc_vm_layer",
  "module_name": "TauLib.BookIII.Bridge.ZFCasVM",
  "module_url": "/verify/taulib/docs/book-iii-bridge-zfcas-vm/",
  "source_line_start": 103,
  "source_line_end": 116,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/ZFCasVM.lean#L103-L116",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/ZFCasVM.lean#L103-L116",
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

- Module: [TauLib.BookIII.Bridge.ZFCasVM](/verify/taulib/docs/book-iii-bridge-zfcas-vm/)
- Source path: [`TauLib/BookIII/Bridge/ZFCasVM.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/ZFCasVM.lean#L103-L116)
- Source range: L103-L116
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D67` — ZFC as E₂ VM

## Immediate Comment / Docstring

```lean
/-- [III.D67] ZFC VM layer template: the four-component template specialized
    for the ZFC virtual machine at E2. -/
```

## Source Excerpt

```lean
def zfc_vm_layer (bound db : TauIdx) : LayerTemplate :=
  { carrier_check := fun x k =>
      -- Carrier: x is a valid "sentence" (tau-address at depth k)
      x < primorial k || primorial k == 0
  , predicate_check := fun x k =>
      -- Predicate: "derivable" = reduce-stable (self-consistent)
      reduce x k == x || x >= primorial k
  , decoder := fun x k =>
      -- Decoder: Godel numbering = reduce (projection to canonical form)
      reduce x k
  , invariant_check := fun x k =>
      -- Invariant: consistency = idempotence of derivability
      reduce (reduce x k) k == reduce x k
  }
```
