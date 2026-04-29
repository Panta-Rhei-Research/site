---
{
  "projection_kind": "taulib_declaration",
  "title": "ElectronQuantumNumbers",
  "permalink": "/verify/taulib/docs/book-iv-particles-periodic-table/electron-quantum-numbers/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.PeriodicTable`.",
  "declaration_id": "TauLib.BookIV.Particles.PeriodicTable::ElectronQuantumNumbers",
  "declaration_slug": "electron-quantum-numbers",
  "kind": "structure",
  "name": "ElectronQuantumNumbers",
  "module_name": "TauLib.BookIV.Particles.PeriodicTable",
  "module_url": "/verify/taulib/docs/book-iv-particles-periodic-table/",
  "source_line_start": 100,
  "source_line_end": 113,
  "registry_ids": [
    "IV.D204"
  ],
  "related_registry_items": [
    {
      "id": "IV.D204",
      "title": "Electron quantum numbers",
      "url": "/registry/object/IV.D204/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/PeriodicTable.lean#L100-L113",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Particles.PeriodicTable",
        "url": "/verify/taulib/docs/book-iv-particles-periodic-table/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/PeriodicTable.lean#L100-L113",
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

- Module: [TauLib.BookIV.Particles.PeriodicTable](/verify/taulib/docs/book-iv-particles-periodic-table/)
- Source path: [`TauLib/BookIV/Particles/PeriodicTable.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/PeriodicTable.lean#L100-L113)
- Source range: L100-L113
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D204` — Electron quantum numbers

## Immediate Comment / Docstring

```lean
/-- [IV.D204] An electron mode on T² bound to nuclear charge Z
    carries four quantum numbers:
    - n: principal (total winding depth)
    - l: angular (0 ≤ l ≤ n-1, lobe structure on L)
    - m_l: magnetic (-l ≤ m_l ≤ l, orientation on L)
    - m_s: spin (±1/2, chirality on T²)

    Shell capacity: 2n² = 2 × sum_{l=0}^{n-1} (2l+1). -/
```

## Source Excerpt

```lean
structure ElectronQuantumNumbers where
  /-- Principal quantum number (n ≥ 1). -/
  n_principal : Nat
  /-- Angular quantum number (0 ≤ l ≤ n-1). -/
  l_angular : Nat
  /-- Magnetic quantum number (|m_l| ≤ l). -/
  m_l_magnetic : Int
  /-- Spin (true = +1/2, false = -1/2). -/
  spin_up : Bool
  /-- n ≥ 1. -/
  n_pos : n_principal ≥ 1
  /-- l < n. -/
  l_bound : l_angular < n_principal
  deriving Repr
```
