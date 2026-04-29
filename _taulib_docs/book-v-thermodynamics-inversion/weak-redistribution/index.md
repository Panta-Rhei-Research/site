---
{
  "projection_kind": "taulib_declaration",
  "title": "WeakRedistribution",
  "permalink": "/verify/taulib/docs/book-v-thermodynamics-inversion/weak-redistribution/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Thermodynamics.Inversion`.",
  "declaration_id": "TauLib.BookV.Thermodynamics.Inversion::WeakRedistribution",
  "declaration_slug": "weak-redistribution",
  "kind": "structure",
  "name": "WeakRedistribution",
  "module_name": "TauLib.BookV.Thermodynamics.Inversion",
  "module_url": "/verify/taulib/docs/book-v-thermodynamics-inversion/",
  "source_line_start": 161,
  "source_line_end": 168,
  "registry_ids": [
    "V.P25"
  ],
  "related_registry_items": [
    {
      "id": "V.P25",
      "title": "Weak redistribution preserves defect count",
      "url": "/registry/object/V.P25/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/Inversion.lean#L161-L168",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Thermodynamics.Inversion",
        "url": "/verify/taulib/docs/book-v-thermodynamics-inversion/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/Inversion.lean#L161-L168",
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

- Module: [TauLib.BookV.Thermodynamics.Inversion](/verify/taulib/docs/book-v-thermodynamics-inversion/)
- Source path: [`TauLib/BookV/Thermodynamics/Inversion.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/Inversion.lean#L161-L168)
- Source range: L161-L168
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.P25` — Weak redistribution preserves defect count

## Immediate Comment / Docstring

```lean
/-- [V.P25] Weak redistribution preserves defect count: the A-sector
    (generator pi, coupling iota_tau) permutes defect content among
    sub-cells without reducing total defect support.

    The weak sector redistributes but does not absorb.
    Only the D-sector (gravity) absorbs defects. -/
```

## Source Excerpt

```lean
structure WeakRedistribution where
  /-- Defect count before weak redistribution. -/
  count_before : Nat
  /-- Defect count after weak redistribution. -/
  count_after : Nat
  /-- Weak redistribution preserves total count. -/
  preserves_count : count_after = count_before
  deriving Repr
```
