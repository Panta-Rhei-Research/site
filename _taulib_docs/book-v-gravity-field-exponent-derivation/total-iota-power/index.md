---
{
  "projection_kind": "taulib_declaration",
  "title": "total_iota_power",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-exponent-derivation/total-iota-power/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.GravityField.ExponentDerivation`.",
  "declaration_id": "TauLib.BookV.GravityField.ExponentDerivation::total_iota_power",
  "declaration_slug": "total-iota-power",
  "kind": "theorem",
  "name": "total_iota_power",
  "module_name": "TauLib.BookV.GravityField.ExponentDerivation",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-exponent-derivation/",
  "source_line_start": 292,
  "source_line_end": 292,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/ExponentDerivation.lean#L292-L292",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.GravityField.ExponentDerivation",
        "url": "/verify/taulib/docs/book-v-gravity-field-exponent-derivation/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/ExponentDerivation.lean#L292-L292",
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

- Module: [TauLib.BookV.GravityField.ExponentDerivation](/verify/taulib/docs/book-v-gravity-field-exponent-derivation/)
- Source path: [`TauLib/BookV/GravityField/ExponentDerivation.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/ExponentDerivation.lean#L292-L292)
- Source range: L292-L292
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The total iota-power is 4 × passage_count = 72.
    Each passage contributes ι⁴ (from one factor of α = (121/225)·ι⁴). -/
```

## Source Excerpt

```lean
theorem total_iota_power : 4 * passage_count = 72 := by rfl
```
