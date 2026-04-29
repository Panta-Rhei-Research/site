---
{
  "projection_kind": "taulib_declaration",
  "title": "MagnetoacousticSynthesis",
  "permalink": "/verify/taulib/docs/book-v-fluid-macro-tau-alfven/magnetoacoustic-synthesis/",
  "summary_short": "`structure` declaration in `TauLib.BookV.FluidMacro.TauAlfven`.",
  "declaration_id": "TauLib.BookV.FluidMacro.TauAlfven::MagnetoacousticSynthesis",
  "declaration_slug": "magnetoacoustic-synthesis",
  "kind": "structure",
  "name": "MagnetoacousticSynthesis",
  "module_name": "TauLib.BookV.FluidMacro.TauAlfven",
  "module_url": "/verify/taulib/docs/book-v-fluid-macro-tau-alfven/",
  "source_line_start": 224,
  "source_line_end": 233,
  "registry_ids": [
    "V.P53"
  ],
  "related_registry_items": [
    {
      "id": "V.P53",
      "title": "ISM Alfv'en cascade",
      "url": "/registry/object/V.P53/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/TauAlfven.lean#L224-L233",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/TauAlfven.lean#L224-L233",
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

- Module: [TauLib.BookV.FluidMacro.TauAlfven](/verify/taulib/docs/book-v-fluid-macro-tau-alfven/)
- Source path: [`TauLib/BookV/FluidMacro/TauAlfven.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/TauAlfven.lean#L224-L233)
- Source range: L224-L233
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.P53` — ISM Alfv'en cascade

## Immediate Comment / Docstring

```lean
/-- [V.P53] Magnetoacoustic synthesis: the three MHD wave modes
    (shear, fast, slow) form a complete basis for small-amplitude
    perturbations of a uniform magnetized plasma.

    Any MHD perturbation decomposes uniquely into these three modes.
    This is the MHD analogue of the Fourier decomposition. -/
```

## Source Excerpt

```lean
structure MagnetoacousticSynthesis where
  /-- Shear mode amplitude. -/
  shear_amplitude : Nat
  /-- Fast mode amplitude. -/
  fast_amplitude : Nat
  /-- Slow mode amplitude. -/
  slow_amplitude : Nat
  /-- Decomposition is complete (all modes present). -/
  is_complete : Bool := true
  deriving Repr
```
