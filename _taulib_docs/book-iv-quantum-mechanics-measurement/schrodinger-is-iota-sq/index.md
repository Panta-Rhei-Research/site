---
{
  "projection_kind": "taulib_declaration",
  "title": "schrodinger_is_iota_sq",
  "permalink": "/verify/taulib/docs/book-iv-quantum-mechanics-measurement/schrodinger-is-iota-sq/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.QuantumMechanics.Measurement`.",
  "declaration_id": "TauLib.BookIV.QuantumMechanics.Measurement::schrodinger_is_iota_sq",
  "declaration_slug": "schrodinger-is-iota-sq",
  "kind": "theorem",
  "name": "schrodinger_is_iota_sq",
  "module_name": "TauLib.BookIV.QuantumMechanics.Measurement",
  "module_url": "/verify/taulib/docs/book-iv-quantum-mechanics-measurement/",
  "source_line_start": 262,
  "source_line_end": 265,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/Measurement.lean#L262-L265",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.QuantumMechanics.Measurement",
        "url": "/verify/taulib/docs/book-iv-quantum-mechanics-measurement/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/Measurement.lean#L262-L265",
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

- Module: [TauLib.BookIV.QuantumMechanics.Measurement](/verify/taulib/docs/book-iv-quantum-mechanics-measurement/)
- Source path: [`TauLib/BookIV/QuantumMechanics/Measurement.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/Measurement.lean#L262-L265)
- Source range: L262-L265
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The Schrodinger Hamiltonian coefficient matches ι_τ². -/
```

## Source Excerpt

```lean
theorem schrodinger_is_iota_sq :
    schrodinger_canonical.hamiltonian_coeff_numer = iota_sq_numer ∧
    schrodinger_canonical.hamiltonian_coeff_denom = iota_sq_denom :=
  ⟨rfl, rfl⟩
```
