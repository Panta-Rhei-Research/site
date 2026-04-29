---
{
  "projection_kind": "taulib_declaration",
  "title": "planck_uniqueness",
  "permalink": "/verify/taulib/docs/book-iv-quantum-mechanics-address-obstruction/planck-uniqueness/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.QuantumMechanics.AddressObstruction`.",
  "declaration_id": "TauLib.BookIV.QuantumMechanics.AddressObstruction::planck_uniqueness",
  "declaration_slug": "planck-uniqueness",
  "kind": "theorem",
  "name": "planck_uniqueness",
  "module_name": "TauLib.BookIV.QuantumMechanics.AddressObstruction",
  "module_url": "/verify/taulib/docs/book-iv-quantum-mechanics-address-obstruction/",
  "source_line_start": 216,
  "source_line_end": 221,
  "registry_ids": [
    "IV.T24"
  ],
  "related_registry_items": [
    {
      "id": "IV.T24",
      "title": "Planck Character Uniqueness",
      "url": "/registry/object/IV.T24/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/AddressObstruction.lean#L216-L221",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.QuantumMechanics.AddressObstruction",
        "url": "/verify/taulib/docs/book-iv-quantum-mechanics-address-obstruction/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/AddressObstruction.lean#L216-L221",
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

- Module: [TauLib.BookIV.QuantumMechanics.AddressObstruction](/verify/taulib/docs/book-iv-quantum-mechanics-address-obstruction/)
- Source path: [`TauLib/BookIV/QuantumMechanics/AddressObstruction.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/AddressObstruction.lean#L216-L221)
- Source range: L216-L221
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.T24` — Planck Character Uniqueness

## Immediate Comment / Docstring

```lean
/-- [IV.T24] hbar_tau is the UNIQUE sigma-equivariant crossing-point
    mediator. There is no other value that satisfies all three constraints:
    (1) sigma-fixed, (2) lives at crossing point, (3) mediates x-p resolution.
    Formalized: the mediator has the specific value 1/4. -/
```

## Source Excerpt

```lean
theorem planck_uniqueness :
    crossing_mediator.numer = 1 ∧
    crossing_mediator.denom = 4 ∧
    crossing_mediator.is_sigma_equivariant = true ∧
    crossing_mediator.is_unique = true :=
  ⟨rfl, rfl, rfl, rfl⟩
```
