---
{
  "projection_kind": "taulib_declaration",
  "title": "b_sector_multiplicative",
  "permalink": "/verify/taulib/docs/book-ii-mirror-wave-holomorphy/b-sector-multiplicative/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Mirror.WaveHolomorphy`.",
  "declaration_id": "TauLib.BookII.Mirror.WaveHolomorphy::b_sector_multiplicative",
  "declaration_slug": "b-sector-multiplicative",
  "kind": "theorem",
  "name": "b_sector_multiplicative",
  "module_name": "TauLib.BookII.Mirror.WaveHolomorphy",
  "module_url": "/verify/taulib/docs/book-ii-mirror-wave-holomorphy/",
  "source_line_start": 246,
  "source_line_end": 249,
  "registry_ids": [
    "II.D70"
  ],
  "related_registry_items": [
    {
      "id": "II.D70",
      "title": "PDE Type Classification",
      "url": "/registry/object/II.D70/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/WaveHolomorphy.lean#L246-L249",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Mirror.WaveHolomorphy",
        "url": "/verify/taulib/docs/book-ii-mirror-wave-holomorphy/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/WaveHolomorphy.lean#L246-L249",
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

- Module: [TauLib.BookII.Mirror.WaveHolomorphy](/verify/taulib/docs/book-ii-mirror-wave-holomorphy/)
- Source path: [`TauLib/BookII/Mirror/WaveHolomorphy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/WaveHolomorphy.lean#L246-L249)
- Source range: L246-L249
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `II.D70` — PDE Type Classification

## Immediate Comment / Docstring

```lean
/-- [II.D70] The sector components are multiplicative:
    (z * w)_b = z_b * w_b. This is the key ring-isomorphism property. -/
```

## Source Excerpt

```lean
theorem b_sector_multiplicative (z w : SplitComplex) :
    (SplitComplex.mul z w).re + (SplitComplex.mul z w).im =
    (z.re + z.im) * (w.re + w.im) := by
  simp [SplitComplex.mul]; ring
```
