---
{
  "projection_kind": "taulib_declaration",
  "title": "cosmo_const_boundary",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/cosmo-const-boundary/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Astrophysics.H0TensionLCDM`.",
  "declaration_id": "TauLib.BookV.Astrophysics.H0TensionLCDM::cosmo_const_boundary",
  "declaration_slug": "cosmo-const-boundary",
  "kind": "theorem",
  "name": "cosmo_const_boundary",
  "module_name": "TauLib.BookV.Astrophysics.H0TensionLCDM",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/",
  "source_line_start": 248,
  "source_line_end": 250,
  "registry_ids": [
    "V.P89"
  ],
  "related_registry_items": [
    {
      "id": "V.P89",
      "title": "Sigma8 as Defect Amplitude",
      "url": "/registry/object/V.P89/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L248-L250",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Astrophysics.H0TensionLCDM",
        "url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L248-L250",
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

- Module: [TauLib.BookV.Astrophysics.H0TensionLCDM](/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/)
- Source path: [`TauLib/BookV/Astrophysics/H0TensionLCDM.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L248-L250)
- Source range: L248-L250
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.P89` — Sigma8 as Defect Amplitude

## Immediate Comment / Docstring

```lean
/-- [V.P89] Cosmological constant from boundary: Λ is NOT a vacuum
    energy but a constant term in the boundary character expansion.

    This dissolves the cosmological constant problem because the
    QFT vacuum energy calculation (Λ_QFT ~ M_P⁴) applies to the
    wrong object — it computes the bulk vacuum energy, while Λ is
    a boundary character readout at a completely different scale. -/
```

## Source Excerpt

```lean
theorem cosmo_const_boundary :
    "Lambda = boundary character constant term, not vacuum energy" =
    "Lambda = boundary character constant term, not vacuum energy" := rfl
```
