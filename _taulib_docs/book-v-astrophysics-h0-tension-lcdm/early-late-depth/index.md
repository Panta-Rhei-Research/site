---
{
  "projection_kind": "taulib_declaration",
  "title": "early_late_depth",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/early-late-depth/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Astrophysics.H0TensionLCDM`.",
  "declaration_id": "TauLib.BookV.Astrophysics.H0TensionLCDM::early_late_depth",
  "declaration_slug": "early-late-depth",
  "kind": "theorem",
  "name": "early_late_depth",
  "module_name": "TauLib.BookV.Astrophysics.H0TensionLCDM",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/",
  "source_line_start": 178,
  "source_line_end": 180,
  "registry_ids": [
    "V.P88"
  ],
  "related_registry_items": [
    {
      "id": "V.P88",
      "title": "Depth-Hubble Monotonicity",
      "url": "/registry/object/V.P88/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L178-L180",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L178-L180",
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
- Source path: [`TauLib/BookV/Astrophysics/H0TensionLCDM.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L178-L180)
- Source range: L178-L180
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.P88` — Depth-Hubble Monotonicity

## Immediate Comment / Docstring

```lean
/-- [V.P88] Early vs late readout depth: the CMB probes the D-sector
    coupling at refinement depth n_CMB (deep, primordial), while
    Cepheids probe at depth n_local (shallow, recent).

    Since the boundary holonomy correction depends on the readout
    depth, the effective H₀ is scale-dependent:
    H₀(CMB) ≠ H₀(Cepheid) is EXPECTED, not anomalous. -/
```

## Source Excerpt

```lean
theorem early_late_depth :
    planck_h0.h0_scaled < shoes_h0.h0_scaled := by
  native_decide
```
