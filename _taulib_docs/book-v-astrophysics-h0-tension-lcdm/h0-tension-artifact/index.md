---
{
  "projection_kind": "taulib_declaration",
  "title": "h0_tension_artifact",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/h0-tension-artifact/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Astrophysics.H0TensionLCDM`.",
  "declaration_id": "TauLib.BookV.Astrophysics.H0TensionLCDM::h0_tension_artifact",
  "declaration_slug": "h0-tension-artifact",
  "kind": "theorem",
  "name": "h0_tension_artifact",
  "module_name": "TauLib.BookV.Astrophysics.H0TensionLCDM",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/",
  "source_line_start": 163,
  "source_line_end": 165,
  "registry_ids": [
    "V.T101"
  ],
  "related_registry_items": [
    {
      "id": "V.T101",
      "title": "H0 Tension Resolution",
      "url": "/registry/object/V.T101/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L163-L165",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L163-L165",
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
- Source path: [`TauLib/BookV/Astrophysics/H0TensionLCDM.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L163-L165)
- Source range: L163-L165
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T101` — H0 Tension Resolution

## Immediate Comment / Docstring

```lean
/-- [V.T101] H₀ tension as readout artifact: the early-time and
    late-time H₀ values differ because they probe the D-sector
    coupling at different scales.

    CMB (z ~ 1100) sees the D-sector coupling at the primordial
    boundary surface. Cepheids (z < 0.01) see it at the local
    scale where boundary corrections are different.

    The ~8% discrepancy is the expected magnitude of the
    boundary holonomy correction between these two scales. -/
```

## Source Excerpt

```lean
theorem h0_tension_artifact :
    "H0 tension = different readout depths probe different boundary corrections" =
    "H0 tension = different readout depths probe different boundary corrections" := rfl
```
