---
{
  "projection_kind": "taulib_declaration",
  "title": "tauEq_implies_execNF_eq",
  "permalink": "/verify/taulib/docs/book-i-addressability-address-resolution/tau-eq-implies-exec-nf-eq/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Addressability.AddressResolution`.",
  "declaration_id": "TauLib.BookI.Addressability.AddressResolution::tauEq_implies_execNF_eq",
  "declaration_slug": "tau-eq-implies-exec-nf-eq",
  "kind": "theorem",
  "name": "tauEq_implies_execNF_eq",
  "module_name": "TauLib.BookI.Addressability.AddressResolution",
  "module_url": "/verify/taulib/docs/book-i-addressability-address-resolution/",
  "source_line_start": 153,
  "source_line_end": 161,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Addressability/AddressResolution.lean#L153-L161",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Addressability/AddressResolution.lean#L153-L161",
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

- Module: [TauLib.BookI.Addressability.AddressResolution](/verify/taulib/docs/book-i-addressability-address-resolution/)
- Source path: [`TauLib/BookI/Addressability/AddressResolution.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Addressability/AddressResolution.lean#L153-L161)
- Source range: L153-L161
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Two τ-equivalent programs have the same NF, hence the same
    behaviour under `execNF`.  This is the operational content of
    address-resolution: equality of canonical addresses entails
    equal execution. -/
```

## Source Excerpt

```lean
theorem tauEq_implies_execNF_eq (a b : Program) (x : Tau.Kernel.TauObj)
    (h : tauEq a b)
    (h_seed : (normalize a).seedMap = (normalize b).seedMap) :
    execNF (normalize a) x = execNF (normalize b) x := by
  unfold execNF
  obtain ⟨h_rho, _⟩ := h
  rw [h_seed, h_rho]

end Tau.Addressability
```
