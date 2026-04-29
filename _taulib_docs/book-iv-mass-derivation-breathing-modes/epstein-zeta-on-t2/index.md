---
{
  "projection_kind": "taulib_declaration",
  "title": "EpsteinZetaOnT2",
  "permalink": "/verify/taulib/docs/book-iv-mass-derivation-breathing-modes/epstein-zeta-on-t2/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.MassDerivation.BreathingModes`.",
  "declaration_id": "TauLib.BookIV.MassDerivation.BreathingModes::EpsteinZetaOnT2",
  "declaration_slug": "epstein-zeta-on-t2",
  "kind": "structure",
  "name": "EpsteinZetaOnT2",
  "module_name": "TauLib.BookIV.MassDerivation.BreathingModes",
  "module_url": "/verify/taulib/docs/book-iv-mass-derivation-breathing-modes/",
  "source_line_start": 102,
  "source_line_end": 105,
  "registry_ids": [
    "IV.D310"
  ],
  "related_registry_items": [
    {
      "id": "IV.D310",
      "title": "Epstein zeta structure",
      "url": "/registry/object/IV.D310/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/MassDerivation/BreathingModes.lean#L102-L105",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.MassDerivation.BreathingModes",
        "url": "/verify/taulib/docs/book-iv-mass-derivation-breathing-modes/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/MassDerivation/BreathingModes.lean#L102-L105",
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

- Module: [TauLib.BookIV.MassDerivation.BreathingModes](/verify/taulib/docs/book-iv-mass-derivation-breathing-modes/)
- Source path: [`TauLib/BookIV/MassDerivation/BreathingModes.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/MassDerivation/BreathingModes.lean#L102-L105)
- Source range: L102-L105
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D310` — Epstein zeta structure

## Immediate Comment / Docstring

```lean
/-- [IV.D310] Epstein zeta Z(s; iι_τ) as spectral zeta of B on T². -/
```

## Source Excerpt

```lean
structure EpsteinZetaOnT2 where
  zeta : EpsteinZetaStructure
  interpretation : String := "spectral zeta of breathing operator on T²"
  deriving Repr
```
