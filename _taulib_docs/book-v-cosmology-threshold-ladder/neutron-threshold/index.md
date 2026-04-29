---
{
  "projection_kind": "taulib_declaration",
  "title": "NeutronThreshold",
  "permalink": "/verify/taulib/docs/book-v-cosmology-threshold-ladder/neutron-threshold/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.ThresholdLadder`.",
  "declaration_id": "TauLib.BookV.Cosmology.ThresholdLadder::NeutronThreshold",
  "declaration_slug": "neutron-threshold",
  "kind": "structure",
  "name": "NeutronThreshold",
  "module_name": "TauLib.BookV.Cosmology.ThresholdLadder",
  "module_url": "/verify/taulib/docs/book-v-cosmology-threshold-ladder/",
  "source_line_start": 166,
  "source_line_end": 173,
  "registry_ids": [
    "V.D160"
  ],
  "related_registry_items": [
    {
      "id": "V.D160",
      "title": "Neutron Threshold L_N",
      "url": "/registry/object/V.D160/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/ThresholdLadder.lean#L166-L173",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/ThresholdLadder.lean#L166-L173",
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
- Source path: [`TauLib/BookV/Cosmology/ThresholdLadder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/ThresholdLadder.lean#L166-L173)
- Source range: L166-L173
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D160` — Neutron Threshold L_N

## Immediate Comment / Docstring

```lean
/-- [V.D160] Neutron threshold L_N: the refinement depth at which
    the strong-sector (η) character drops below the confinement
    coupling κ(C;3) = ι_τ³/(1−ι_τ).

    At L_N, the mass hierarchy is established:
      m_n > m_p > m_e
      m_p = m_n − δ_A
      m_e = m_n / R -/
```

## Source Excerpt

```lean
structure NeutronThreshold where
  /-- Threshold data. -/
  threshold : ThresholdRegimeBoundary
  /-- The threshold is for neutrons. -/
  is_neutron : threshold.kind = .Neutron
  /-- Mass hierarchy holds below this threshold. -/
  mass_hierarchy_established : Bool := true
  deriving Repr
```
