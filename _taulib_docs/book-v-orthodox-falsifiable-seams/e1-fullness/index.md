---
{
  "projection_kind": "taulib_declaration",
  "title": "E1Fullness",
  "permalink": "/verify/taulib/docs/book-v-orthodox-falsifiable-seams/e1-fullness/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Orthodox.FalsifiableSeams`.",
  "declaration_id": "TauLib.BookV.Orthodox.FalsifiableSeams::E1Fullness",
  "declaration_slug": "e1-fullness",
  "kind": "structure",
  "name": "E1Fullness",
  "module_name": "TauLib.BookV.Orthodox.FalsifiableSeams",
  "module_url": "/verify/taulib/docs/book-v-orthodox-falsifiable-seams/",
  "source_line_start": 214,
  "source_line_end": 225,
  "registry_ids": [
    "V.T140"
  ],
  "related_registry_items": [
    {
      "id": "V.T140",
      "title": "Elayer1",
      "url": "/registry/object/V.T140/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/FalsifiableSeams.lean#L214-L225",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Orthodox.FalsifiableSeams",
        "url": "/verify/taulib/docs/book-v-orthodox-falsifiable-seams/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/FalsifiableSeams.lean#L214-L225",
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

- Module: [TauLib.BookV.Orthodox.FalsifiableSeams](/verify/taulib/docs/book-v-orthodox-falsifiable-seams/)
- Source path: [`TauLib/BookV/Orthodox/FalsifiableSeams.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/FalsifiableSeams.lean#L214-L225)
- Source range: L214-L225
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.T140` — Elayer1

## Immediate Comment / Docstring

```lean
/-- [V.T140] E-layer 1 is structurally full.

    At E1, the tau-framework provides:
    - 5 forces with sector assignments
    - All fundamental constants from iota_tau
    - All quantum phenomena from boundary characters
    - No unaccounted-for phenomena

    "Full" means: every known E1 (physics) phenomenon has a
    tau-description. It does NOT mean: every tau-computation
    has been carried out. Some entries (QCD, CKM, etc.) have
    structure but not yet completed computations. -/
```

## Source Excerpt

```lean
structure E1Fullness where
  /-- Number of forces with sector assignments. -/
  force_count : Nat
  /-- All 5. -/
  force_eq : force_count = 5
  /-- Number of constants from iota_tau. -/
  constants_from_iota : Bool := true
  /-- Quantum phenomena from boundary characters. -/
  quantum_from_characters : Bool := true
  /-- Some computations still in progress. -/
  computations_ongoing : Bool := true
  deriving Repr
```
