---
{
  "projection_kind": "taulib_declaration",
  "title": "AccessibilityMorphism",
  "permalink": "/corpus/taulib/docs/book-vii-ethics-ciproof/accessibility-morphism/",
  "summary_short": "`structure` declaration in `TauLib.BookVII.Ethics.CIProof`.",
  "declaration_id": "TauLib.BookVII.Ethics.CIProof::AccessibilityMorphism",
  "declaration_slug": "accessibility-morphism",
  "kind": "structure",
  "name": "AccessibilityMorphism",
  "module_name": "TauLib.BookVII.Ethics.CIProof",
  "module_url": "/corpus/taulib/docs/book-vii-ethics-ciproof/",
  "source_line_start": 815,
  "source_line_end": 822,
  "registry_ids": [
    "VII.D63"
  ],
  "related_registry_items": [
    {
      "id": "VII.D63",
      "title": "Accessibility Morphism",
      "url": "/registry/object/VII.D63/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L815-L822",
  "formal_status": "defined",
  "declaration_role": "type/data schema",
  "formal_status_label": "type/data schema",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVII.Ethics.CIProof",
        "url": "/corpus/taulib/docs/book-vii-ethics-ciproof/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L815-L822",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
      "role": "type/data schema",
      "status": "type/data schema"
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

- Module: [TauLib.BookVII.Ethics.CIProof](/corpus/taulib/docs/book-vii-ethics-ciproof/)
- Source path: [`TauLib/BookVII/Ethics/CIProof.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L815-L822)
- Source range: L815-L822
- Kind: `structure`
- Public role: `type/data schema`
- Formal status hint: `type/data schema`

## Registry Links

- `VII.D63` — Accessibility Morphism

## Immediate Comment / Docstring

```lean
/-- [VII.D63] Accessibility Morphism (ch43). The accessibility
    relation is a morphism in the kernel: f : w₁ → w₂ iff w₂ is
    accessible from w₁ via an admissible transformation. Reflexive
    and transitive (S4). -/
```

## Source Excerpt

```lean
structure AccessibilityMorphism where
  /-- Reflexive: every world accesses itself. -/
  reflexive : Bool := true
  /-- Transitive: accessibility composes. -/
  transitive : Bool := true
  /-- Morphism in kernel. -/
  kernel_morphism : Bool := true
  deriving Repr
```
