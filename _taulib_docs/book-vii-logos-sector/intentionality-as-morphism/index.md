---
{
  "projection_kind": "taulib_declaration",
  "title": "IntentionalityAsMorphism",
  "permalink": "/verify/taulib/docs/book-vii-logos-sector/intentionality-as-morphism/",
  "summary_short": "`structure` declaration in `TauLib.BookVII.Logos.Sector`.",
  "declaration_id": "TauLib.BookVII.Logos.Sector::IntentionalityAsMorphism",
  "declaration_slug": "intentionality-as-morphism",
  "kind": "structure",
  "name": "IntentionalityAsMorphism",
  "module_name": "TauLib.BookVII.Logos.Sector",
  "module_url": "/verify/taulib/docs/book-vii-logos-sector/",
  "source_line_start": 184,
  "source_line_end": 189,
  "registry_ids": [
    "VII.D84"
  ],
  "related_registry_items": [
    {
      "id": "VII.D84",
      "title": "Intentionality as Morphism",
      "url": "/registry/object/VII.D84/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Logos/Sector.lean#L184-L189",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Logos/Sector.lean#L184-L189",
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
- Source path: [`TauLib/BookVII/Logos/Sector.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Logos/Sector.lean#L184-L189)
- Source range: L184-L189
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VII.D84` — Intentionality as Morphism

## Immediate Comment / Docstring

```lean
/-- [VII.D84] Intentionality as Morphism (ch109). Intentionality
    (aboutness) modelled as a morphism f : Mind → World in the
    ambient category. Mental state M is "about" world-state W iff
    there exists a morphism f : M → W. -/
```

## Source Excerpt

```lean
structure IntentionalityAsMorphism where
  /-- Aboutness = morphism. -/
  aboutness_as_morphism : Bool := true
  /-- From mind to world. -/
  mind_to_world : Bool := true
  deriving Repr
```
