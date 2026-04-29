---
{
  "projection_kind": "taulib_declaration",
  "title": "NormalHierarchyProof",
  "permalink": "/verify/taulib/docs/book-v-cosmology-neutrino-background/normal-hierarchy-proof/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.NeutrinoBackground`.",
  "declaration_id": "TauLib.BookV.Cosmology.NeutrinoBackground::NormalHierarchyProof",
  "declaration_slug": "normal-hierarchy-proof",
  "kind": "structure",
  "name": "NormalHierarchyProof",
  "module_name": "TauLib.BookV.Cosmology.NeutrinoBackground",
  "module_url": "/verify/taulib/docs/book-v-cosmology-neutrino-background/",
  "source_line_start": 156,
  "source_line_end": 171,
  "registry_ids": [
    "V.T268"
  ],
  "related_registry_items": [
    {
      "id": "V.T268",
      "title": "Normal Hierarchy from Winding Exponent Order",
      "url": "/registry/object/V.T268/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/NeutrinoBackground.lean#L156-L171",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.NeutrinoBackground",
        "url": "/verify/taulib/docs/book-v-cosmology-neutrino-background/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/NeutrinoBackground.lean#L156-L171",
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

- Module: [TauLib.BookV.Cosmology.NeutrinoBackground](/verify/taulib/docs/book-v-cosmology-neutrino-background/)
- Source path: [`TauLib/BookV/Cosmology/NeutrinoBackground.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/NeutrinoBackground.lean#L156-L171)
- Source range: L156-L171
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.T268` — Normal Hierarchy from Winding Exponent Order

## Immediate Comment / Docstring

```lean
/-- [V.T268] Normal Hierarchy from winding exponent order.
    Since Δpq = 203/175 > 0 and Δpr = 609/700 > 0,
    the ordering r < p < q gives m₃ > m₂ > m₁ (Normal Ordering).
    This is a theorem, not a parameter choice. -/
```

## Source Excerpt

```lean
structure NormalHierarchyProof where
  /-- Δpq numerator (positive). -/
  delta_pq_num : Nat := 203
  /-- Δpq denominator (positive). -/
  delta_pq_den : Nat := 175
  /-- Δpr numerator (positive). -/
  delta_pr_num : Nat := 609
  /-- Δpr denominator (positive). -/
  delta_pr_den : Nat := 700
  /-- Total Δqr numerator (positive). -/
  delta_qr_num : Nat := 1421
  /-- Total Δqr denominator (positive). -/
  delta_qr_den : Nat := 700
  /-- All numerators positive (Normal Ordering is forced). -/
  is_normal_ordering : Bool := true
  deriving Repr
```
