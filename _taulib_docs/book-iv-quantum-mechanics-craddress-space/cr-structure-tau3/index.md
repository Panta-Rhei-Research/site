---
{
  "projection_kind": "taulib_declaration",
  "title": "cr_structure_tau3",
  "permalink": "/verify/taulib/docs/book-iv-quantum-mechanics-craddress-space/cr-structure-tau3/",
  "summary_short": "`def` declaration in `TauLib.BookIV.QuantumMechanics.CRAddressSpace`.",
  "declaration_id": "TauLib.BookIV.QuantumMechanics.CRAddressSpace::cr_structure_tau3",
  "declaration_slug": "cr-structure-tau3",
  "kind": "def",
  "name": "cr_structure_tau3",
  "module_name": "TauLib.BookIV.QuantumMechanics.CRAddressSpace",
  "module_url": "/verify/taulib/docs/book-iv-quantum-mechanics-craddress-space/",
  "source_line_start": 88,
  "source_line_end": 94,
  "registry_ids": [
    "IV.D50"
  ],
  "related_registry_items": [
    {
      "id": "IV.D50",
      "title": "CR-Structure on τ³",
      "url": "/registry/object/IV.D50/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/CRAddressSpace.lean#L88-L94",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/CRAddressSpace.lean#L88-L94",
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
- Source path: [`TauLib/BookIV/QuantumMechanics/CRAddressSpace.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/CRAddressSpace.lean#L88-L94)
- Source range: L88-L94
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `IV.D50` — CR-Structure on τ³

## Immediate Comment / Docstring

```lean
/-- [IV.D50] The CR-structure on tau^3 = tau^1 x_f T^2:
    H = fiber tangent T^2 (2 real dims), J = rotation on H,
    nu = contact form (1 real dim along tau^1).
    Type: (k=1, l=1) giving dim = 2*1 + 1 = 3. -/
```

## Source Excerpt

```lean
def cr_structure_tau3 : IntegrableCR where
  k := 1
  l := 1
  real_dim := 3
  dim_eq := rfl
  nijenhuis_vanishes := true
  nij_true := rfl
```
