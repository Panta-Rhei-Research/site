---
{
  "projection_kind": "taulib_declaration",
  "title": "emActiveStructural",
  "permalink": "/verify/taulib/docs/book-iv-sectors-boundary-filtration/em-active-structural/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Sectors.BoundaryFiltration`.",
  "declaration_id": "TauLib.BookIV.Sectors.BoundaryFiltration::emActiveStructural",
  "declaration_slug": "em-active-structural",
  "kind": "def",
  "name": "emActiveStructural",
  "module_name": "TauLib.BookIV.Sectors.BoundaryFiltration",
  "module_url": "/verify/taulib/docs/book-iv-sectors-boundary-filtration/",
  "source_line_start": 121,
  "source_line_end": 124,
  "registry_ids": [
    "IV.D330"
  ],
  "related_registry_items": [
    {
      "id": "IV.D330",
      "title": "Structural EM Activity",
      "url": "/registry/object/IV.D330/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/BoundaryFiltration.lean#L121-L124",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Sectors.BoundaryFiltration",
        "url": "/verify/taulib/docs/book-iv-sectors-boundary-filtration/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/BoundaryFiltration.lean#L121-L124",
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

- Module: [TauLib.BookIV.Sectors.BoundaryFiltration](/verify/taulib/docs/book-iv-sectors-boundary-filtration/)
- Source path: [`TauLib/BookIV/Sectors/BoundaryFiltration.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/BoundaryFiltration.lean#L121-L124)
- Source range: L121-L124
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `IV.D330` — Structural EM Activity

## Immediate Comment / Docstring

```lean
/-- [IV.D330] Structural EM-activity: derived from carrier type and polarity alone.

    **Rule 1 (Gravitational Orthogonality):**
    If carrier = Base AND polarity ≠ Balanced (i.e., D-sector/α),
    then EM-silent. Base τ¹ ⊥ fiber T² in τ³.

    **Rule 2 (Crossing Polarity Cancellation):**
    If polarity = Balanced AND config = Crossing, then EM-silent.
    Net EM charge = χ₊ − χ₋ = 0 at crossing for balanced generator.

    **Default:** All other modes are EM-active. -/
```

## Source Excerpt

```lean
def emActiveStructural : BoundaryMode → Bool
  | ⟨.alpha, _⟩          => false  -- Rule 1: D-sector on base, EM-orthogonal
  | ⟨.pi_, .crossing⟩    => false  -- Rule 2: balanced polarity at crossing
  | _                     => true   -- All other modes: active
```
