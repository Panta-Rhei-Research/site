---
{
  "projection_kind": "taulib_declaration",
  "title": "QNMDiscriminator",
  "permalink": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/qnmdiscriminator/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Gravity.BHTopoModes`.",
  "declaration_id": "TauLib.BookV.Gravity.BHTopoModes::QNMDiscriminator",
  "declaration_slug": "qnmdiscriminator",
  "kind": "structure",
  "name": "QNMDiscriminator",
  "module_name": "TauLib.BookV.Gravity.BHTopoModes",
  "module_url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/",
  "source_line_start": 352,
  "source_line_end": 367,
  "registry_ids": [
    "V.T185"
  ],
  "related_registry_items": [
    {
      "id": "V.T185",
      "title": "QNM Frequency Ratio = ι_τ⁻¹ ≈ 2.930 as Clean S²/T² Discriminator",
      "url": "/registry/object/V.T185/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/BHTopoModes.lean#L352-L367",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Gravity.BHTopoModes",
        "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/BHTopoModes.lean#L352-L367",
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

- Module: [TauLib.BookV.Gravity.BHTopoModes](/verify/taulib/docs/book-v-gravity-bhtopo-modes/)
- Source path: [`TauLib/BookV/Gravity/BHTopoModes.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/BHTopoModes.lean#L352-L367)
- Source range: L352-L367
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.T185` — QNM Frequency Ratio = ι_τ⁻¹ ≈ 2.930 as Clean S²/T² Discriminator

## Immediate Comment / Docstring

```lean
/-- [V.T185] Structure capturing the QNM frequency ratio discriminator.
    T² range [2.5, 3.4] vs S² range [0.8, 1.1]: no overlap → clean discriminator.
    All values stored ×10 to use Nat arithmetic. -/
```

## Source Excerpt

```lean
structure QNMDiscriminator where
  /-- T² lower bound ×10 (= 2.5 → 25). -/
  t2_lower_x10 : Nat := 25
  /-- T² upper bound ×10 (= 3.4 → 34). -/
  t2_upper_x10 : Nat := 34
  /-- S² lower bound ×10 (= 0.8 → 8). -/
  s2_lower_x10 : Nat := 8
  /-- S² upper bound ×10 (= 1.1 → 11). -/
  s2_upper_x10 : Nat := 11
  /-- Range gap ×10 = t2_lower − s2_upper (>0 means no overlap). -/
  range_gap_x10 : Nat := 14
  /-- Gap equals t2_lower − s2_upper. -/
  gap_eq : range_gap_x10 = t2_lower_x10 - s2_upper_x10
  /-- Number of free parameters. -/
  free_parameters : Nat := 0
  deriving Repr
```
