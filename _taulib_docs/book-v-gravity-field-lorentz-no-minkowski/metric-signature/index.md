---
{
  "projection_kind": "taulib_declaration",
  "title": "MetricSignature",
  "permalink": "/corpus/taulib/docs/book-v-gravity-field-lorentz-no-minkowski/metric-signature/",
  "summary_short": "`structure` declaration in `TauLib.BookV.GravityField.LorentzNoMinkowski`.",
  "declaration_id": "TauLib.BookV.GravityField.LorentzNoMinkowski::MetricSignature",
  "declaration_slug": "metric-signature",
  "kind": "structure",
  "name": "MetricSignature",
  "module_name": "TauLib.BookV.GravityField.LorentzNoMinkowski",
  "module_url": "/corpus/taulib/docs/book-v-gravity-field-lorentz-no-minkowski/",
  "source_line_start": 101,
  "source_line_end": 106,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/LorentzNoMinkowski.lean#L101-L106",
  "formal_status": "defined",
  "declaration_role": "type/data schema",
  "formal_status_label": "type/data schema",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.GravityField.LorentzNoMinkowski",
        "url": "/corpus/taulib/docs/book-v-gravity-field-lorentz-no-minkowski/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/LorentzNoMinkowski.lean#L101-L106",
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

- Module: [TauLib.BookV.GravityField.LorentzNoMinkowski](/corpus/taulib/docs/book-v-gravity-field-lorentz-no-minkowski/)
- Source path: [`TauLib/BookV/GravityField/LorentzNoMinkowski.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/LorentzNoMinkowski.lean#L101-L106)
- Source range: L101-L106
- Kind: `structure`
- Public role: `type/data schema`
- Formal status hint: `type/data schema`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Signature type for the chart metric: number of negative and
    positive eigenvalues. For Lorentzian: (1, 3). -/
```

## Source Excerpt

```lean
structure MetricSignature where
  /-- Number of negative eigenvalues (temporal dimensions). -/
  negative : Nat
  /-- Number of positive eigenvalues (spatial dimensions). -/
  positive : Nat
  deriving Repr, DecidableEq, BEq
```
