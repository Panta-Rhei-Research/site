---
{
  "projection_kind": "taulib_declaration",
  "title": "TruthMakerOntological",
  "permalink": "/verify/taulib/docs/book-vii-meta-registers/truth-maker-ontological/",
  "summary_short": "`structure` declaration in `TauLib.BookVII.Meta.Registers`.",
  "declaration_id": "TauLib.BookVII.Meta.Registers::TruthMakerOntological",
  "declaration_slug": "truth-maker-ontological",
  "kind": "structure",
  "name": "TruthMakerOntological",
  "module_name": "TauLib.BookVII.Meta.Registers",
  "module_url": "/verify/taulib/docs/book-vii-meta-registers/",
  "source_line_start": 643,
  "source_line_end": 654,
  "registry_ids": [
    "VII.D27"
  ],
  "related_registry_items": [
    {
      "id": "VII.D27",
      "title": "Truth-Maker in τ (Ontological)",
      "url": "/registry/object/VII.D27/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L643-L654",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVII.Meta.Registers",
        "url": "/verify/taulib/docs/book-vii-meta-registers/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L643-L654",
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

- Module: [TauLib.BookVII.Meta.Registers](/verify/taulib/docs/book-vii-meta-registers/)
- Source path: [`TauLib/BookVII/Meta/Registers.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L643-L654)
- Source range: L643-L654
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VII.D27` — Truth-Maker in τ (Ontological)

## Immediate Comment / Docstring

```lean
/-- [VII.D27] Truth-Maker in τ — Ontological (ch19). Four truth-makers:
    (1) Inclusion: subobject witness (monomorphism)
    (2) Section: global section of a sheaf
    (3) Diagram: commutative diagram as proof certificate
    (4) Invariant: property stable under all automorphisms -/
```

## Source Excerpt

```lean
structure TruthMakerOntological where
  /-- (1) Inclusion as truth-maker. -/
  tm_inclusion : Bool := true
  /-- (2) Section as truth-maker. -/
  tm_section : Bool := true
  /-- (3) Diagram as truth-maker. -/
  tm_diagram : Bool := true
  /-- (4) Invariant as truth-maker. -/
  tm_invariant : Bool := true
  /-- Four truth-maker types. -/
  tm_count : Nat := 4
  deriving Repr
```
