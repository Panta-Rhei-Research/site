---
{
  "projection_kind": "taulib_declaration",
  "title": "MassHierarchyAtLN",
  "permalink": "/verify/taulib/docs/book-v-cosmology-threshold-ladder/mass-hierarchy-at-ln/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.ThresholdLadder`.",
  "declaration_id": "TauLib.BookV.Cosmology.ThresholdLadder::MassHierarchyAtLN",
  "declaration_slug": "mass-hierarchy-at-ln",
  "kind": "structure",
  "name": "MassHierarchyAtLN",
  "module_name": "TauLib.BookV.Cosmology.ThresholdLadder",
  "module_url": "/verify/taulib/docs/book-v-cosmology-threshold-ladder/",
  "source_line_start": 283,
  "source_line_end": 288,
  "registry_ids": [
    "V.R218"
  ],
  "related_registry_items": [
    {
      "id": "V.R218",
      "title": "The mass hierarchy at L_N",
      "url": "/registry/object/V.R218/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/ThresholdLadder.lean#L283-L288",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.ThresholdLadder",
        "url": "/verify/taulib/docs/book-v-cosmology-threshold-ladder/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/ThresholdLadder.lean#L283-L288",
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

- Module: [TauLib.BookV.Cosmology.ThresholdLadder](/verify/taulib/docs/book-v-cosmology-threshold-ladder/)
- Source path: [`TauLib/BookV/Cosmology/ThresholdLadder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/ThresholdLadder.lean#L283-L288)
- Source range: L283-L288
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.R218` — The mass hierarchy at L_N

## Immediate Comment / Docstring

```lean
/-- [V.R218] Mass hierarchy at L_N: once the strong-sector character
    drops below confinement coupling, the mass hierarchy locks in:
      m_n > m_p > m_e
    with m_p = m_n − δ_A and m_e = m_n/R (R ≈ 1838.68). -/
```

## Source Excerpt

```lean
structure MassHierarchyAtLN where
  /-- R ≈ 1838.68 (neutron-to-electron mass ratio, × 100). -/
  r_times_100 : Nat
  /-- R in range. -/
  r_range : r_times_100 > 183800 ∧ r_times_100 < 183900
  deriving Repr
```
