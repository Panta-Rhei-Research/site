---
{
  "projection_kind": "taulib_declaration",
  "title": "ClassicalTestResult",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-linear-einstein/classical-test-result/",
  "summary_short": "`structure` declaration in `TauLib.BookV.GravityField.LinearEinstein`.",
  "declaration_id": "TauLib.BookV.GravityField.LinearEinstein::ClassicalTestResult",
  "declaration_slug": "classical-test-result",
  "kind": "structure",
  "name": "ClassicalTestResult",
  "module_name": "TauLib.BookV.GravityField.LinearEinstein",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-linear-einstein/",
  "source_line_start": 168,
  "source_line_end": 179,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/LinearEinstein.lean#L168-L179",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.GravityField.LinearEinstein",
        "url": "/verify/taulib/docs/book-v-gravity-field-linear-einstein/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/LinearEinstein.lean#L168-L179",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
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

- Module: [TauLib.BookV.GravityField.LinearEinstein](/verify/taulib/docs/book-v-gravity-field-linear-einstein/)
- Source path: [`TauLib/BookV/GravityField/LinearEinstein.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/LinearEinstein.lean#L168-L179)
- Source range: L168-L179
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Classical GR test result: a predicted value with units. -/
```

## Source Excerpt

```lean
structure ClassicalTestResult where
  /-- Test name. -/
  name : String
  /-- Predicted value numerator (scaled). -/
  value_numer : Nat
  /-- Predicted value denominator. -/
  value_denom : Nat
  /-- Denominator positive. -/
  denom_pos : value_denom > 0
  /-- Unit description. -/
  unit : String
  deriving Repr
```
