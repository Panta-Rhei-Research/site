---
{
  "projection_kind": "taulib_declaration",
  "title": "tauEq",
  "permalink": "/verify/taulib/docs/book-i-addressability-address-resolution/tau-eq/",
  "summary_short": "`def` declaration in `TauLib.BookI.Addressability.AddressResolution`.",
  "declaration_id": "TauLib.BookI.Addressability.AddressResolution::tauEq",
  "declaration_slug": "tau-eq",
  "kind": "def",
  "name": "tauEq",
  "module_name": "TauLib.BookI.Addressability.AddressResolution",
  "module_url": "/verify/taulib/docs/book-i-addressability-address-resolution/",
  "source_line_start": 88,
  "source_line_end": 92,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Addressability/AddressResolution.lean#L88-L92",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Addressability.AddressResolution",
        "url": "/verify/taulib/docs/book-i-addressability-address-resolution/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Addressability/AddressResolution.lean#L88-L92",
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

- Module: [TauLib.BookI.Addressability.AddressResolution](/verify/taulib/docs/book-i-addressability-address-resolution/)
- Source path: [`TauLib/BookI/Addressability/AddressResolution.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Addressability/AddressResolution.lean#L88-L92)
- Source range: L88-L92
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Two programs are **τ-equivalent** iff their canonical normal forms
    are NF-equivalent. -/
```

## Source Excerpt

```lean
def tauEq (p q : Program) : Prop :=
  nfEquiv (normalize p) (normalize q)

instance (p q : Program) : Decidable (tauEq p q) := by
  unfold tauEq; infer_instance
```
