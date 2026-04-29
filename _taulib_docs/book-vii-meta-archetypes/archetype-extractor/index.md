---
{
  "projection_kind": "taulib_declaration",
  "title": "ArchetypeExtractor",
  "permalink": "/verify/taulib/docs/book-vii-meta-archetypes/archetype-extractor/",
  "summary_short": "`structure` declaration in `TauLib.BookVII.Meta.Archetypes`.",
  "declaration_id": "TauLib.BookVII.Meta.Archetypes::ArchetypeExtractor",
  "declaration_slug": "archetype-extractor",
  "kind": "structure",
  "name": "ArchetypeExtractor",
  "module_name": "TauLib.BookVII.Meta.Archetypes",
  "module_url": "/verify/taulib/docs/book-vii-meta-archetypes/",
  "source_line_start": 111,
  "source_line_end": 123,
  "registry_ids": [
    "VII.D17"
  ],
  "related_registry_items": [
    {
      "id": "VII.D17",
      "title": "Archetype Extractor Protocol",
      "url": "/registry/object/VII.D17/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Archetypes.lean#L111-L123",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVII.Meta.Archetypes",
        "url": "/verify/taulib/docs/book-vii-meta-archetypes/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Archetypes.lean#L111-L123",
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

- Module: [TauLib.BookVII.Meta.Archetypes](/verify/taulib/docs/book-vii-meta-archetypes/)
- Source path: [`TauLib/BookVII/Meta/Archetypes.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Archetypes.lean#L111-L123)
- Source range: L111-L123
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VII.D17` — Archetype Extractor Protocol

## Immediate Comment / Docstring

```lean
/-- [VII.D17] Archetype Extractor: 5-step methodological procedure.
    (1) Identify invariant I
    (2) Enumerate j-closed candidates exhibiting I
    (3) Intersect to minimality (via VII.L08)
    (4) Verify non-triviality
    (5) Read out via register functor (Reg_E, Reg_P, Reg_D, Reg_C) -/
```

## Source Excerpt

```lean
structure ArchetypeExtractor where
  /-- Step 1: invariant identified. -/
  step1_identify : Bool := true
  /-- Step 2: candidates enumerated. -/
  step2_enumerate : Bool := true
  /-- Step 3: intersection computed. -/
  step3_intersect : Bool := true
  /-- Step 4: non-triviality verified. -/
  step4_verify : Bool := true
  /-- Step 5: readout applied. -/
  step5_readout : Bool := true
  step_count : Nat := 5
  deriving Repr
```
