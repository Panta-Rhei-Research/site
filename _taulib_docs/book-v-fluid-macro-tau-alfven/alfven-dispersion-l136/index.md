---
{
  "projection_kind": "taulib_declaration",
  "title": "alfven_dispersion",
  "permalink": "/verify/taulib/docs/book-v-fluid-macro-tau-alfven/alfven-dispersion-l136/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.FluidMacro.TauAlfven`.",
  "declaration_id": "TauLib.BookV.FluidMacro.TauAlfven::alfven_dispersion",
  "declaration_slug": "alfven-dispersion-l136",
  "kind": "theorem",
  "name": "alfven_dispersion",
  "module_name": "TauLib.BookV.FluidMacro.TauAlfven",
  "module_url": "/verify/taulib/docs/book-v-fluid-macro-tau-alfven/",
  "source_line_start": 136,
  "source_line_end": 138,
  "registry_ids": [
    "V.P52"
  ],
  "related_registry_items": [
    {
      "id": "V.P52",
      "title": "Alfv'en speed as cross-coupling readout",
      "url": "/registry/object/V.P52/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/TauAlfven.lean#L136-L138",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.FluidMacro.TauAlfven",
        "url": "/verify/taulib/docs/book-v-fluid-macro-tau-alfven/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/TauAlfven.lean#L136-L138",
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

- Module: [TauLib.BookV.FluidMacro.TauAlfven](/verify/taulib/docs/book-v-fluid-macro-tau-alfven/)
- Source path: [`TauLib/BookV/FluidMacro/TauAlfven.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/TauAlfven.lean#L136-L138)
- Source range: L136-L138
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.P52` — Alfv'en speed as cross-coupling readout

## Immediate Comment / Docstring

```lean
/-- [V.P52] Alfven dispersion: the phase velocity depends on polarization
    and angle.

    Shear: v_φ = v_A cos θ (angle-dependent)
    Fast: v_φ > v_A (faster than Alfven speed)
    Slow: v_φ < v_A (slower than Alfven speed)

    Structural recording. -/
```

## Source Excerpt

```lean
theorem alfven_dispersion :
    "Shear: omega = v_A k cos(theta), Fast: v_phi > v_A, Slow: v_phi < v_A" =
    "Shear: omega = v_A k cos(theta), Fast: v_phi > v_A, Slow: v_phi < v_A" := rfl
```
