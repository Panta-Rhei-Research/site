---
{
  "projection_kind": "taulib_declaration",
  "title": "GenerativeSwitch",
  "permalink": "/verify/taulib/docs/book-vii-logos-sector/generative-switch/",
  "summary_short": "`structure` declaration in `TauLib.BookVII.Logos.Sector`.",
  "declaration_id": "TauLib.BookVII.Logos.Sector::GenerativeSwitch",
  "declaration_slug": "generative-switch",
  "kind": "structure",
  "name": "GenerativeSwitch",
  "module_name": "TauLib.BookVII.Logos.Sector",
  "module_url": "/verify/taulib/docs/book-vii-logos-sector/",
  "source_line_start": 317,
  "source_line_end": 324,
  "registry_ids": [
    "VII.D90"
  ],
  "related_registry_items": [
    {
      "id": "VII.D90",
      "title": "Generative Switch",
      "url": "/registry/object/VII.D90/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Logos/Sector.lean#L317-L324",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVII.Logos.Sector",
        "url": "/verify/taulib/docs/book-vii-logos-sector/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Logos/Sector.lean#L317-L324",
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

- Module: [TauLib.BookVII.Logos.Sector](/verify/taulib/docs/book-vii-logos-sector/)
- Source path: [`TauLib/BookVII/Logos/Sector.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Logos/Sector.lean#L317-L324)
- Source range: L317-L324
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VII.D90` — Generative Switch

## Immediate Comment / Docstring

```lean
/-- [VII.D90] Generative Switch (ch126). The transition mechanism
    between enrichment layers: a structural switch that activates
    when sufficient complexity is reached at the current layer.
    E_n → E_{n+1} when Enrich(E_n) ≠ E_n. -/
```

## Source Excerpt

```lean
structure GenerativeSwitch where
  /-- Transition mechanism between layers. -/
  layer_transition : Bool := true
  /-- Activated by complexity threshold. -/
  complexity_threshold : Bool := true
  /-- Structural, not temporal. -/
  structural : Bool := true
  deriving Repr
```
