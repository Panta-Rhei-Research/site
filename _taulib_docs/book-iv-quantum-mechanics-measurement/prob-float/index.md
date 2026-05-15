---
{
  "projection_kind": "taulib_declaration",
  "title": "AddressResolution.probFloat",
  "permalink": "/corpus/taulib/docs/book-iv-quantum-mechanics-measurement/prob-float/",
  "summary_short": "`def` declaration in `TauLib.BookIV.QuantumMechanics.Measurement`.",
  "declaration_id": "TauLib.BookIV.QuantumMechanics.Measurement::AddressResolution.probFloat",
  "declaration_slug": "prob-float",
  "kind": "def",
  "name": "AddressResolution.probFloat",
  "module_name": "TauLib.BookIV.QuantumMechanics.Measurement",
  "module_url": "/corpus/taulib/docs/book-iv-quantum-mechanics-measurement/",
  "source_line_start": 88,
  "source_line_end": 89,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/Measurement.lean#L88-L89",
  "formal_status": "defined",
  "declaration_role": "data/computed value",
  "formal_status_label": "data/computed value",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.QuantumMechanics.Measurement",
        "url": "/corpus/taulib/docs/book-iv-quantum-mechanics-measurement/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/Measurement.lean#L88-L89",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "role": "data/computed value",
      "status": "data/computed value"
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

- Module: [TauLib.BookIV.QuantumMechanics.Measurement](/corpus/taulib/docs/book-iv-quantum-mechanics-measurement/)
- Source path: [`TauLib/BookIV/QuantumMechanics/Measurement.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/Measurement.lean#L88-L89)
- Source range: L88-L89
- Kind: `def`
- Public role: `data/computed value`
- Formal status hint: `data/computed value`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Probability as Float (for display). -/
```

## Source Excerpt

```lean
def AddressResolution.probFloat (a : AddressResolution) : Float :=
  Float.ofNat a.probability_numer / Float.ofNat a.probability_denom
```
