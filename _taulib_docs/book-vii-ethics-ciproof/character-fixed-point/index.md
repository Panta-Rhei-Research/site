---
{
  "projection_kind": "taulib_declaration",
  "title": "CharacterFixedPoint",
  "permalink": "/verify/taulib/docs/book-vii-ethics-ciproof/character-fixed-point/",
  "summary_short": "`structure` declaration in `TauLib.BookVII.Ethics.CIProof`.",
  "declaration_id": "TauLib.BookVII.Ethics.CIProof::CharacterFixedPoint",
  "declaration_slug": "character-fixed-point",
  "kind": "structure",
  "name": "CharacterFixedPoint",
  "module_name": "TauLib.BookVII.Ethics.CIProof",
  "module_url": "/verify/taulib/docs/book-vii-ethics-ciproof/",
  "source_line_start": 286,
  "source_line_end": 293,
  "registry_ids": [
    "VII.D70"
  ],
  "related_registry_items": [
    {
      "id": "VII.D70",
      "title": "Character as Ethical Fixed Point",
      "url": "/registry/object/VII.D70/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L286-L293",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L286-L293",
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
- Source path: [`TauLib/BookVII/Ethics/CIProof.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L286-L293)
- Source range: L286-L293
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VII.D70` — Character as Ethical Fixed Point

## Immediate Comment / Docstring

```lean
/-- [VII.D70] Character as Ethical Fixed Point (ch86).
    Habituation functor H : Disp → Disp.
    Virtue V: stable fixed point H(V) = V.
    Vice W: unstable fixed point or H^n(W) diverges. -/
```

## Source Excerpt

```lean
structure CharacterFixedPoint where
  /-- Habituation functor well-defined. -/
  has_habituation : Bool := true
  /-- Virtue = stable fixed point. -/
  virtue_is_fixed : Bool := true
  /-- Vice = unstable fixed point or divergent. -/
  vice_is_unstable : Bool := true
  deriving Repr
```
