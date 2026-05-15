---
{
  "projection_kind": "taulib_declaration",
  "title": "genCarrier",
  "permalink": "/corpus/taulib/docs/book-iv-sectors-boundary-filtration/gen-carrier-l82/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Sectors.BoundaryFiltration`.",
  "declaration_id": "TauLib.BookIV.Sectors.BoundaryFiltration::genCarrier",
  "declaration_slug": "gen-carrier-l82",
  "kind": "def",
  "name": "genCarrier",
  "module_name": "TauLib.BookIV.Sectors.BoundaryFiltration",
  "module_url": "/corpus/taulib/docs/book-iv-sectors-boundary-filtration/",
  "source_line_start": 82,
  "source_line_end": 87,
  "registry_ids": [
    "IV.D328"
  ],
  "related_registry_items": [
    {
      "id": "IV.D328",
      "title": "Generator Carrier Assignment",
      "url": "/registry/object/IV.D328/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/BoundaryFiltration.lean#L82-L87",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/BoundaryFiltration.lean#L82-L87",
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
- Source path: [`TauLib/BookIV/Sectors/BoundaryFiltration.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/BoundaryFiltration.lean#L82-L87)
- Source range: L82-L87
- Kind: `def`
- Public role: `definition`
- Formal status hint: `definition`

## Registry Links

- `IV.D328` — Generator Carrier Assignment

## Immediate Comment / Docstring

```lean
/-- [IV.D328] Carrier assignment for each generator.

    The 5 generators split into base (temporal) and fiber (spatial):
    - Base τ¹: α (gravity, D-sector), π (weak, A-sector)
    - Fiber T²: γ (EM, B-sector), η (strong, C-sector), ω (Higgs, B∩C)

    This is a τ-structural fact from the fibered product, not SM input. -/
```

## Source Excerpt

```lean
def genCarrier : Gen5 → GenCarrier
  | .alpha => .Base     -- D-sector: base τ¹ (gravity = temporal)
  | .pi_   => .Base     -- A-sector: base τ¹ (weak = temporal)
  | .gamma => .Fiber    -- B-sector: fiber T² (EM = spatial)
  | .eta   => .Fiber    -- C-sector: fiber T² (strong = spatial)
  | .omega => .Fiber    -- B∩C: fiber T² (Higgs = crossing on fiber)
```
