---
{
  "projection_kind": "taulib_declaration",
  "title": "QuantizationObstruction",
  "permalink": "/verify/taulib/docs/book-v-orthodox-emergent-geometry/quantization-obstruction/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Orthodox.EmergentGeometry`.",
  "declaration_id": "TauLib.BookV.Orthodox.EmergentGeometry::QuantizationObstruction",
  "declaration_slug": "quantization-obstruction",
  "kind": "structure",
  "name": "QuantizationObstruction",
  "module_name": "TauLib.BookV.Orthodox.EmergentGeometry",
  "module_url": "/verify/taulib/docs/book-v-orthodox-emergent-geometry/",
  "source_line_start": 120,
  "source_line_end": 129,
  "registry_ids": [
    "V.T126"
  ],
  "related_registry_items": [
    {
      "id": "V.T126",
      "title": "The readout quantization obstruction",
      "url": "/registry/object/V.T126/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/EmergentGeometry.lean#L120-L129",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Orthodox.EmergentGeometry",
        "url": "/verify/taulib/docs/book-v-orthodox-emergent-geometry/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/EmergentGeometry.lean#L120-L129",
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

- Module: [TauLib.BookV.Orthodox.EmergentGeometry](/verify/taulib/docs/book-v-orthodox-emergent-geometry/)
- Source path: [`TauLib/BookV/Orthodox/EmergentGeometry.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/EmergentGeometry.lean#L120-L129)
- Source range: L120-L129
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.T126` — The readout quantization obstruction

## Immediate Comment / Docstring

```lean
/-- [V.T126] The readout quantization obstruction.

    Quantizing GR = applying the quantum readout functor to a classical
    readout. This produces a double readout (boundary -> classical ->
    "quantum"), which explains UV divergences in quantum gravity.

    The correct approach: work directly with H_partial[omega]
    (which is already "quantum" in the sense of being a non-commutative
    profinite algebra). -/
```

## Source Excerpt

```lean
structure QuantizationObstruction where
  /-- Number of readout layers in the double readout. -/
  readout_depth : Nat
  /-- Double readout = 2 layers. -/
  depth_eq : readout_depth = 2
  /-- Double readout produces UV problems. -/
  produces_uv : Bool := true
  /-- Direct boundary approach avoids obstruction. -/
  boundary_avoids : Bool := true
  deriving Repr
```
