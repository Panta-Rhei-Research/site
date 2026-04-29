---
{
  "projection_kind": "taulib_declaration",
  "title": "VMQuantumState",
  "permalink": "/verify/taulib/docs/book-v-orthodox-measurement-unification/vmquantum-state/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Orthodox.MeasurementUnification`.",
  "declaration_id": "TauLib.BookV.Orthodox.MeasurementUnification::VMQuantumState",
  "declaration_slug": "vmquantum-state",
  "kind": "structure",
  "name": "VMQuantumState",
  "module_name": "TauLib.BookV.Orthodox.MeasurementUnification",
  "module_url": "/verify/taulib/docs/book-v-orthodox-measurement-unification/",
  "source_line_start": 81,
  "source_line_end": 92,
  "registry_ids": [
    "V.D189"
  ],
  "related_registry_items": [
    {
      "id": "V.D189",
      "title": "VM representation of a quantum state",
      "url": "/registry/object/V.D189/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/MeasurementUnification.lean#L81-L92",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Orthodox.MeasurementUnification",
        "url": "/verify/taulib/docs/book-v-orthodox-measurement-unification/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/MeasurementUnification.lean#L81-L92",
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

- Module: [TauLib.BookV.Orthodox.MeasurementUnification](/verify/taulib/docs/book-v-orthodox-measurement-unification/)
- Source path: [`TauLib/BookV/Orthodox/MeasurementUnification.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/MeasurementUnification.lean#L81-L92)
- Source range: L81-L92
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D189` — VM representation of a quantum state

## Immediate Comment / Docstring

```lean
/-- [V.D189] VM representation of a quantum state.

    A VM quantum state is a vector |psi> obtained from a boundary
    character chi by the readout map Read : chi -> |psi_chi>.

    The wave function is NOT a physical object. It is a VM (virtual
    machine) representation of boundary data. "Collapse" is the VM
    updating when address resolution occurs at the ontic level. -/
```

## Source Excerpt

```lean
structure VMQuantumState where
  /-- Number of boundary characters in the superposition. -/
  character_count : Nat
  /-- At least one character (non-empty state). -/
  nonempty : character_count > 0
  /-- Current readout status. -/
  status : ReadoutStatus
  /-- Sector(s) involved (up to 5). -/
  sector_count : Nat
  /-- Sector count bounded by 5. -/
  sector_bound : sector_count ≤ 5
  deriving Repr
```
