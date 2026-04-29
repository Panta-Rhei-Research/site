---
{
  "projection_kind": "taulib_declaration",
  "title": "no_knobs_check",
  "permalink": "/verify/taulib/docs/book-iii-sectors-parity-bridge/no-knobs-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Sectors.ParityBridge`.",
  "declaration_id": "TauLib.BookIII.Sectors.ParityBridge::no_knobs_check",
  "declaration_slug": "no-knobs-check",
  "kind": "def",
  "name": "no_knobs_check",
  "module_name": "TauLib.BookIII.Sectors.ParityBridge",
  "module_url": "/verify/taulib/docs/book-iii-sectors-parity-bridge/",
  "source_line_start": 122,
  "source_line_end": 126,
  "registry_ids": [
    "III.T08"
  ],
  "related_registry_items": [
    {
      "id": "III.T08",
      "title": "No Knobs Principle",
      "url": "/registry/object/III.T08/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Sectors/ParityBridge.lean#L122-L126",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Sectors.ParityBridge",
        "url": "/verify/taulib/docs/book-iii-sectors-parity-bridge/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Sectors/ParityBridge.lean#L122-L126",
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

- Module: [TauLib.BookIII.Sectors.ParityBridge](/verify/taulib/docs/book-iii-sectors-parity-bridge/)
- Source path: [`TauLib/BookIII/Sectors/ParityBridge.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Sectors/ParityBridge.lean#L122-L126)
- Source range: L122-L126
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.T08` — No Knobs Principle

## Immediate Comment / Docstring

```lean
/-- [III.T08] No Knobs check: all couplings are canonically determined.
    1. Complete ledger (10 entries)
    2. Sector preservation (structure determines couplings)
    3. Template invariance (structure is rigid)
    4. Langlands reflection (sector structure preserved under enrichment) -/
```

## Source Excerpt

```lean
def no_knobs_check (bound db : TauIdx) : Bool :=
  coupling_ledger_check bound &&
  sector_preservation_check bound db &&
  template_invariance_check bound db &&
  langlands_reflection_check bound db
```
