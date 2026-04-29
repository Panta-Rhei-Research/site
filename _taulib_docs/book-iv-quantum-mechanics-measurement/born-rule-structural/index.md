---
{
  "projection_kind": "taulib_declaration",
  "title": "born_rule_structural",
  "permalink": "/verify/taulib/docs/book-iv-quantum-mechanics-measurement/born-rule-structural/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.QuantumMechanics.Measurement`.",
  "declaration_id": "TauLib.BookIV.QuantumMechanics.Measurement::born_rule_structural",
  "declaration_slug": "born-rule-structural",
  "kind": "theorem",
  "name": "born_rule_structural",
  "module_name": "TauLib.BookIV.QuantumMechanics.Measurement",
  "module_url": "/verify/taulib/docs/book-iv-quantum-mechanics-measurement/",
  "source_line_start": 101,
  "source_line_end": 102,
  "registry_ids": [
    "IV.T27"
  ],
  "related_registry_items": [
    {
      "id": "IV.T27",
      "title": "Born Rule",
      "url": "/registry/object/IV.T27/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/Measurement.lean#L101-L102",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/Measurement.lean#L101-L102",
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
- Source path: [`TauLib/BookIV/QuantumMechanics/Measurement.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/Measurement.lean#L101-L102)
- Source range: L101-L102
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.T27` — Born Rule

## Immediate Comment / Docstring

```lean
/-- [IV.T27] Born rule as theorem: the probability of resolving to mode
    (m₀, n₀) equals |c_{m₀,n₀}|², the squared projection coefficient.

    This is a STRUCTURAL consequence of the Pythagorean theorem on the
    CR-Hilbert space, not a postulate. The resolution probability is
    determined by the geometry of the projection, not by an axiom. -/
```

## Source Excerpt

```lean
theorem born_rule_structural (a : AddressResolution) :
    a.probability_numer ≤ a.probability_denom := a.prob_le_one
```
