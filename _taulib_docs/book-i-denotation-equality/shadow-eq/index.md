---
{
  "projection_kind": "taulib_declaration",
  "title": "shadow_eq",
  "permalink": "/verify/taulib/docs/book-i-denotation-equality/shadow-eq/",
  "summary_short": "`def` declaration in `TauLib.BookI.Denotation.Equality`.",
  "declaration_id": "TauLib.BookI.Denotation.Equality::shadow_eq",
  "declaration_slug": "shadow-eq",
  "kind": "def",
  "name": "shadow_eq",
  "module_name": "TauLib.BookI.Denotation.Equality",
  "module_url": "/verify/taulib/docs/book-i-denotation-equality/",
  "source_line_start": 42,
  "source_line_end": 50,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/Equality.lean#L42-L50",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Denotation.Equality",
        "url": "/verify/taulib/docs/book-i-denotation-equality/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/Equality.lean#L42-L50",
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

- Module: [TauLib.BookI.Denotation.Equality](/verify/taulib/docs/book-i-denotation-equality/)
- Source path: [`TauLib/BookI/Denotation/Equality.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/Equality.lean#L42-L50)
- Source range: L42-L50
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [I.D15, Level 3] Shadow equality: same coordinates.
    In Parts I-III, this collapses to ontic equality.
    (The full ABCD chart in Part IV may refine this.) -/
```

## Source Excerpt

```lean
def shadow_eq (x y : TauObj) : Prop := x = y

-- ============================================================
-- PROPERTIES
-- ============================================================

/-- Ontic equality is decidable. -/
instance ontic_eq_decidable (x y : TauObj) : Decidable (ontic_eq x y) :=
  inferInstanceAs (Decidable (x = y))
```
