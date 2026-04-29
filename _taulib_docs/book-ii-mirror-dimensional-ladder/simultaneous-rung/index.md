---
{
  "projection_kind": "taulib_declaration",
  "title": "simultaneous_rung",
  "permalink": "/verify/taulib/docs/book-ii-mirror-dimensional-ladder/simultaneous-rung/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Mirror.DimensionalLadder`.",
  "declaration_id": "TauLib.BookII.Mirror.DimensionalLadder::simultaneous_rung",
  "declaration_slug": "simultaneous-rung",
  "kind": "theorem",
  "name": "simultaneous_rung",
  "module_name": "TauLib.BookII.Mirror.DimensionalLadder",
  "module_url": "/verify/taulib/docs/book-ii-mirror-dimensional-ladder/",
  "source_line_start": 248,
  "source_line_end": 249,
  "registry_ids": [
    "II.T47"
  ],
  "related_registry_items": [
    {
      "id": "II.T47",
      "title": "Simultaneous Rung Theorem",
      "url": "/registry/object/II.T47/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/DimensionalLadder.lean#L248-L249",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Mirror.DimensionalLadder",
        "url": "/verify/taulib/docs/book-ii-mirror-dimensional-ladder/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/DimensionalLadder.lean#L248-L249",
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

- Module: [TauLib.BookII.Mirror.DimensionalLadder](/verify/taulib/docs/book-ii-mirror-dimensional-ladder/)
- Source path: [`TauLib/BookII/Mirror/DimensionalLadder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/DimensionalLadder.lean#L248-L249)
- Source range: L248-L249
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `II.T47` — Simultaneous Rung Theorem

## Immediate Comment / Docstring

```lean
/-- [II.T47] Simultaneous Rung Theorem: τ³ exhibits features from at least
    three classical SCV dimension rungs simultaneously.
    Specifically: C1 (CauchyIntegral), C2 (DistinguishedBoundary, HartogsExtension),
    and C3 (FullHartogs). -/
```

## Source Excerpt

```lean
theorem simultaneous_rung :
    tau_distinct_rungs.length ≥ 3 := by native_decide
```
