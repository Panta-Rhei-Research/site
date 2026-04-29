---
{
  "projection_kind": "taulib_declaration",
  "title": "NonDualisticPlatonism",
  "permalink": "/verify/taulib/docs/book-vii-meta-registers/non-dualistic-platonism/",
  "summary_short": "`structure` declaration in `TauLib.BookVII.Meta.Registers`.",
  "declaration_id": "TauLib.BookVII.Meta.Registers::NonDualisticPlatonism",
  "declaration_slug": "non-dualistic-platonism",
  "kind": "structure",
  "name": "NonDualisticPlatonism",
  "module_name": "TauLib.BookVII.Meta.Registers",
  "module_url": "/verify/taulib/docs/book-vii-meta-registers/",
  "source_line_start": 961,
  "source_line_end": 968,
  "registry_ids": [
    "VII.D40"
  ],
  "related_registry_items": [
    {
      "id": "VII.D40",
      "title": "Non-Dualistic Platonism",
      "url": "/registry/object/VII.D40/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L961-L968",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L961-L968",
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
- Source path: [`TauLib/BookVII/Meta/Registers.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L961-L968)
- Source range: L961-L968
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VII.D40` — Non-Dualistic Platonism

## Immediate Comment / Docstring

```lean
/-- [VII.D40] Non-Dualistic Platonism (ch32). Dissolves the
    Platonism-Nominalism debate: mathematical objects exist as
    structural positions (not in a separate Platonic realm) but
    are mind-independent (not nominalist conventions). The kernel
    K_τ is the locus of mathematical existence. -/
```

## Source Excerpt

```lean
structure NonDualisticPlatonism where
  /-- Not Platonic realm. -/
  no_separate_realm : Bool := true
  /-- Not nominalist convention. -/
  mind_independent : Bool := true
  /-- Structural positions in kernel. -/
  kernel_locus : Bool := true
  deriving Repr
```
