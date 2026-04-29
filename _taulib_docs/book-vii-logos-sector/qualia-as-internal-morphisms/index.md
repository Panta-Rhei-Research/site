---
{
  "projection_kind": "taulib_declaration",
  "title": "QualiaAsInternalMorphisms",
  "permalink": "/verify/taulib/docs/book-vii-logos-sector/qualia-as-internal-morphisms/",
  "summary_short": "`structure` declaration in `TauLib.BookVII.Logos.Sector`.",
  "declaration_id": "TauLib.BookVII.Logos.Sector::QualiaAsInternalMorphisms",
  "declaration_slug": "qualia-as-internal-morphisms",
  "kind": "structure",
  "name": "QualiaAsInternalMorphisms",
  "module_name": "TauLib.BookVII.Logos.Sector",
  "module_url": "/verify/taulib/docs/book-vii-logos-sector/",
  "source_line_start": 204,
  "source_line_end": 211,
  "registry_ids": [
    "VII.D85"
  ],
  "related_registry_items": [
    {
      "id": "VII.D85",
      "title": "Qualia as Internal Morphisms",
      "url": "/registry/object/VII.D85/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Logos/Sector.lean#L204-L211",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Logos/Sector.lean#L204-L211",
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
- Source path: [`TauLib/BookVII/Logos/Sector.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Logos/Sector.lean#L204-L211)
- Source range: L204-L211
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VII.D85` — Qualia as Internal Morphisms

## Immediate Comment / Docstring

```lean
/-- [VII.D85] Qualia as Internal Morphisms (ch110). **CONJECTURAL.**
    Qualia (subjective experience quality) modelled as internal
    morphisms in the mind-topos: endomorphisms capturing the
    "what it is like" aspect. Conjectural because the hard problem
    of consciousness remains an epistemic gap — the structural
    account is offered as framework, not as proof that qualia
    are "nothing but" morphisms. -/
```

## Source Excerpt

```lean
structure QualiaAsInternalMorphisms where
  /-- Internal morphisms in mind-topos. -/
  internal_morphisms : Bool := true
  /-- Capture qualitative character. -/
  qualitative_character : Bool := true
  /-- Epistemic gap acknowledged. -/
  epistemic_gap : Bool := true
  deriving Repr
```
