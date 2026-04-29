---
{
  "projection_kind": "taulib_declaration",
  "title": "cr_admissible",
  "permalink": "/verify/taulib/docs/book-iv-quantum-mechanics-craddress-space/cr-admissible/",
  "summary_short": "`def` declaration in `TauLib.BookIV.QuantumMechanics.CRAddressSpace`.",
  "declaration_id": "TauLib.BookIV.QuantumMechanics.CRAddressSpace::cr_admissible",
  "declaration_slug": "cr-admissible",
  "kind": "def",
  "name": "cr_admissible",
  "module_name": "TauLib.BookIV.QuantumMechanics.CRAddressSpace",
  "module_url": "/verify/taulib/docs/book-iv-quantum-mechanics-craddress-space/",
  "source_line_start": 180,
  "source_line_end": 185,
  "registry_ids": [
    "IV.T16"
  ],
  "related_registry_items": [
    {
      "id": "IV.T16",
      "title": "CR Parity Constraint",
      "url": "/registry/object/IV.T16/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/CRAddressSpace.lean#L180-L185",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.QuantumMechanics.CRAddressSpace",
        "url": "/verify/taulib/docs/book-iv-quantum-mechanics-craddress-space/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/CRAddressSpace.lean#L180-L185",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
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

- Module: [TauLib.BookIV.QuantumMechanics.CRAddressSpace](/verify/taulib/docs/book-iv-quantum-mechanics-craddress-space/)
- Source path: [`TauLib/BookIV/QuantumMechanics/CRAddressSpace.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/CRAddressSpace.lean#L180-L185)
- Source range: L180-L185
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `IV.T16` — CR Parity Constraint

## Immediate Comment / Docstring

```lean
/-- [IV.T16] CR parity constraint: chi_{m,n} is CR-admissible iff
    m + n is even (m + n = 0 mod 2). This is the condition for the
    character to be compatible with the CR-structure on tau^3. -/
```

## Source Excerpt

```lean
def cr_admissible (addr : CRAddress) : Prop :=
  (addr.m + addr.n) % 2 = 0

/-- Decidability of CR-admissibility. -/
instance (addr : CRAddress) : Decidable (cr_admissible addr) :=
  inferInstanceAs (Decidable ((addr.m + addr.n) % 2 = 0))
```
