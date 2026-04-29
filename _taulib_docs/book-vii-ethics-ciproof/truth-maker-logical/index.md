---
{
  "projection_kind": "taulib_declaration",
  "title": "TruthMakerLogical",
  "permalink": "/verify/taulib/docs/book-vii-ethics-ciproof/truth-maker-logical/",
  "summary_short": "`structure` declaration in `TauLib.BookVII.Ethics.CIProof`.",
  "declaration_id": "TauLib.BookVII.Ethics.CIProof::TruthMakerLogical",
  "declaration_slug": "truth-maker-logical",
  "kind": "structure",
  "name": "TruthMakerLogical",
  "module_name": "TauLib.BookVII.Ethics.CIProof",
  "module_url": "/verify/taulib/docs/book-vii-ethics-ciproof/",
  "source_line_start": 727,
  "source_line_end": 738,
  "registry_ids": [
    "VII.D60"
  ],
  "related_registry_items": [
    {
      "id": "VII.D60",
      "title": "Truth-Maker in τ (Logical)",
      "url": "/registry/object/VII.D60/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L727-L738",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVII.Ethics.CIProof",
        "url": "/verify/taulib/docs/book-vii-ethics-ciproof/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L727-L738",
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

- Module: [TauLib.BookVII.Ethics.CIProof](/verify/taulib/docs/book-vii-ethics-ciproof/)
- Source path: [`TauLib/BookVII/Ethics/CIProof.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L727-L738)
- Source range: L727-L738
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VII.D60` — Truth-Maker in τ (Logical)

## Immediate Comment / Docstring

```lean
/-- [VII.D60] Truth-Maker — Logical (ch42). Four-level alethic
    hierarchy (matching VII.D27 ontological truth-makers):
    Level 1: Inclusion (subobject witness, monomorphism)
    Level 2: Section (global section of a sheaf)
    Level 3: Diagram (commutative diagram as proof certificate)
    Level 4: Invariant (property stable under all automorphisms) -/
```

## Source Excerpt

```lean
structure TruthMakerLogical where
  /-- Level 1: inclusion truth-maker. -/
  level_inclusion : Bool := true
  /-- Level 2: section truth-maker. -/
  level_section : Bool := true
  /-- Level 3: diagram truth-maker. -/
  level_diagram : Bool := true
  /-- Level 4: invariant truth-maker. -/
  level_invariant : Bool := true
  /-- Four levels. -/
  level_count : Nat := 4
  deriving Repr
```
