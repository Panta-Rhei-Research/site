---
{
  "projection_kind": "taulib_declaration",
  "title": "YukawaReadout",
  "permalink": "/verify/taulib/docs/book-iv-particles-sector-atlas/yukawa-readout/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.SectorAtlas`.",
  "declaration_id": "TauLib.BookIV.Particles.SectorAtlas::YukawaReadout",
  "declaration_slug": "yukawa-readout",
  "kind": "structure",
  "name": "YukawaReadout",
  "module_name": "TauLib.BookIV.Particles.SectorAtlas",
  "module_url": "/verify/taulib/docs/book-iv-particles-sector-atlas/",
  "source_line_start": 216,
  "source_line_end": 225,
  "registry_ids": [
    "IV.R108"
  ],
  "related_registry_items": [
    {
      "id": "IV.R108",
      "title": "Yukawa as readout not parameter",
      "url": "/registry/object/IV.R108/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/SectorAtlas.lean#L216-L225",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Particles.SectorAtlas",
        "url": "/verify/taulib/docs/book-iv-particles-sector-atlas/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/SectorAtlas.lean#L216-L225",
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

- Module: [TauLib.BookIV.Particles.SectorAtlas](/verify/taulib/docs/book-iv-particles-sector-atlas/)
- Source path: [`TauLib/BookIV/Particles/SectorAtlas.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/SectorAtlas.lean#L216-L225)
- Source range: L216-L225
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.R108` — Yukawa as readout not parameter

## Immediate Comment / Docstring

```lean
/-- [IV.R108] The Yukawa hierarchy spanning six orders of magnitude
    (y_e ≈ 3×10⁻⁶ to y_t ≈ 1) is a readout of winding-mode geometry
    on T², not a set of independent parameters. It arises from compounding
    three geometric factors, each determined by ι_τ alone. -/
```

## Source Excerpt

```lean
structure YukawaReadout where
  /-- Orders of magnitude span. -/
  span_orders : Nat := 6
  /-- Number of geometric factors. -/
  num_factors : Nat := 3
  /-- All determined by ι_τ. -/
  iota_determined : Bool := true
  /-- Not free parameters. -/
  not_free : Bool := true
  deriving Repr
```
