---
{
  "projection_kind": "taulib_declaration",
  "title": "genPolarity",
  "permalink": "/corpus/taulib/docs/book-iv-sectors-boundary-filtration/gen-polarity/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Sectors.BoundaryFiltration`.",
  "declaration_id": "TauLib.BookIV.Sectors.BoundaryFiltration::genPolarity",
  "declaration_slug": "gen-polarity",
  "kind": "def",
  "name": "genPolarity",
  "module_name": "TauLib.BookIV.Sectors.BoundaryFiltration",
  "module_url": "/corpus/taulib/docs/book-iv-sectors-boundary-filtration/",
  "source_line_start": 99,
  "source_line_end": 104,
  "registry_ids": [
    "IV.D329"
  ],
  "related_registry_items": [
    {
      "id": "IV.D329",
      "title": "Generator Polarity Assignment",
      "url": "/registry/object/IV.D329/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/BoundaryFiltration.lean#L99-L104",
  "formal_status": "defined",
  "declaration_role": "definition",
  "formal_status_label": "definition",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Sectors.BoundaryFiltration",
        "url": "/corpus/taulib/docs/book-iv-sectors-boundary-filtration/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/BoundaryFiltration.lean#L99-L104",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "role": "definition",
      "status": "definition"
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

- Module: [TauLib.BookIV.Sectors.BoundaryFiltration](/corpus/taulib/docs/book-iv-sectors-boundary-filtration/)
- Source path: [`TauLib/BookIV/Sectors/BoundaryFiltration.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/BoundaryFiltration.lean#L99-L104)
- Source range: L99-L104
- Kind: `def`
- Public role: `definition`
- Formal status hint: `definition`

## Registry Links

- `IV.D329` — Generator Polarity Assignment

## Immediate Comment / Docstring

```lean
/-- [IV.D329] Polarity assignment for each generator, from SectorParameters.

    - ChiPlus: χ₊-dominant (α, γ)
    - Balanced: equal χ₊ and χ₋ (π — unique!)
    - ChiMinus: χ₋-dominant (η)
    - Crossing: both lobes active (ω) -/
```

## Source Excerpt

```lean
def genPolarity : Gen5 → PolaritySign
  | .alpha => .ChiPlus   -- D-sector: χ₊-dominant
  | .pi_   => .Balanced  -- A-sector: balanced (unique)
  | .gamma => .ChiPlus   -- B-sector: χ₊-dominant
  | .eta   => .ChiMinus  -- C-sector: χ₋-dominant
  | .omega => .Crossing  -- B∩C: crossing
```
