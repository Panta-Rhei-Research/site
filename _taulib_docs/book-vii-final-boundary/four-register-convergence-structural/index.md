---
{
  "projection_kind": "taulib_declaration",
  "title": "four_register_convergence_structural",
  "permalink": "/verify/taulib/docs/book-vii-final-boundary/four-register-convergence-structural/",
  "summary_short": "`theorem` declaration in `TauLib.BookVII.Final.Boundary`.",
  "declaration_id": "TauLib.BookVII.Final.Boundary::four_register_convergence_structural",
  "declaration_slug": "four-register-convergence-structural",
  "kind": "theorem",
  "name": "four_register_convergence_structural",
  "module_name": "TauLib.BookVII.Final.Boundary",
  "module_url": "/verify/taulib/docs/book-vii-final-boundary/",
  "source_line_start": 104,
  "source_line_end": 108,
  "registry_ids": [
    "VII.P29"
  ],
  "related_registry_items": [
    {
      "id": "VII.P29",
      "title": "Four-Register Convergence at S_L",
      "url": "/registry/object/VII.P29/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Final/Boundary.lean#L104-L108",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVII.Final.Boundary",
        "url": "/verify/taulib/docs/book-vii-final-boundary/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Final/Boundary.lean#L104-L108",
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

- Module: [TauLib.BookVII.Final.Boundary](/verify/taulib/docs/book-vii-final-boundary/)
- Source path: [`TauLib/BookVII/Final/Boundary.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Final/Boundary.lean#L104-L108)
- Source range: L104-L108
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `VII.P29` — Four-Register Convergence at S_L

## Immediate Comment / Docstring

```lean
/-- [VII.P29] Four-Register Convergence at S_L (ch121). Structural parts:
    D-C coincidence verified; the convergence of all four registers
    (E, P, D, C) at S_L requires ω-content.

    **sorry**: methodological boundary — full four-register convergence
    involves Reg_C stance-stability and Reg_E empirical adequacy claims
    that transcend formal verification. D-C coincidence is the
    diagrammatic core. -/
```

## Source Excerpt

```lean
theorem four_register_convergence_structural :
    sector_logos.dc_coincidence = true ∧
    sector_logos.unique_mediator = true ∧
    canonical_sector_decomp.pure_sector_count = 4 :=
  ⟨rfl, rfl, rfl⟩
```
