---
{
  "projection_kind": "taulib_declaration",
  "title": "DecoherenceShadow",
  "permalink": "/verify/taulib/docs/book-v-orthodox-measurement-unification/decoherence-shadow/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Orthodox.MeasurementUnification`.",
  "declaration_id": "TauLib.BookV.Orthodox.MeasurementUnification::DecoherenceShadow",
  "declaration_slug": "decoherence-shadow",
  "kind": "structure",
  "name": "DecoherenceShadow",
  "module_name": "TauLib.BookV.Orthodox.MeasurementUnification",
  "module_url": "/verify/taulib/docs/book-v-orthodox-measurement-unification/",
  "source_line_start": 210,
  "source_line_end": 221,
  "registry_ids": [
    "V.P107"
  ],
  "related_registry_items": [
    {
      "id": "V.P107",
      "title": "Decoherence as address-resolution shadow",
      "url": "/registry/object/V.P107/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/MeasurementUnification.lean#L210-L221",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Orthodox.MeasurementUnification",
        "url": "/verify/taulib/docs/book-v-orthodox-measurement-unification/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/MeasurementUnification.lean#L210-L221",
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

- Module: [TauLib.BookV.Orthodox.MeasurementUnification](/verify/taulib/docs/book-v-orthodox-measurement-unification/)
- Source path: [`TauLib/BookV/Orthodox/MeasurementUnification.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/MeasurementUnification.lean#L210-L221)
- Source range: L210-L221
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.P107` — Decoherence as address-resolution shadow

## Immediate Comment / Docstring

```lean
/-- [V.P107] Decoherence as address-resolution shadow.

    Decoherence is the VM description of address resolution in the
    boundary algebra. The "environment" is the collection of boundary
    characters not in the system's address range.

    Decoherence rate is determined by:
    1. The number of environment characters
    2. The cross-coupling between system and environment sectors
    3. The refinement depth of the address resolution

    Decoherence is NOT fundamental: it is the readout-layer description
    of the ontic address-resolution process. -/
```

## Source Excerpt

```lean
structure DecoherenceShadow where
  /-- Number of system characters. -/
  system_chars : Nat
  /-- Number of environment characters. -/
  env_chars : Nat
  /-- Total characters = system + environment. -/
  total : Nat
  /-- Total is sum. -/
  total_eq : total = system_chars + env_chars
  /-- Decoherence is NOT fundamental. -/
  is_fundamental : Bool := false
  deriving Repr
```
