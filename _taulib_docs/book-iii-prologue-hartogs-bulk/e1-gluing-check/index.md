---
{
  "projection_kind": "taulib_declaration",
  "title": "e1_gluing_check",
  "permalink": "/verify/taulib/docs/book-iii-prologue-hartogs-bulk/e1-gluing-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Prologue.HartogsBulk`.",
  "declaration_id": "TauLib.BookIII.Prologue.HartogsBulk::e1_gluing_check",
  "declaration_slug": "e1-gluing-check",
  "kind": "def",
  "name": "e1_gluing_check",
  "module_name": "TauLib.BookIII.Prologue.HartogsBulk",
  "module_url": "/verify/taulib/docs/book-iii-prologue-hartogs-bulk/",
  "source_line_start": 95,
  "source_line_end": 97,
  "registry_ids": [
    "III.D03"
  ],
  "related_registry_items": [
    {
      "id": "III.D03",
      "title": "E₁ as Gluing Principle",
      "url": "/registry/object/III.D03/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Prologue/HartogsBulk.lean#L95-L97",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Prologue.HartogsBulk",
        "url": "/verify/taulib/docs/book-iii-prologue-hartogs-bulk/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Prologue/HartogsBulk.lean#L95-L97",
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

- Module: [TauLib.BookIII.Prologue.HartogsBulk](/verify/taulib/docs/book-iii-prologue-hartogs-bulk/)
- Source path: [`TauLib/BookIII/Prologue/HartogsBulk.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Prologue/HartogsBulk.lean#L95-L97)
- Source range: L95-L97
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D03` — E₁ as Gluing Principle

## Immediate Comment / Docstring

```lean
/-- [III.D03] E₁ gluing check: verify that Book II is complete (all 6
    export components verified) and that the Hartogs bulk projection
    is tower-coherent. E₁ = "local patches glue" = "physics exists".

    This combines the ForwardBook3 export with local Hartogs coherence. -/
```

## Source Excerpt

```lean
def e1_gluing_check (bound db k_max : TauIdx) : Bool :=
  full_export_check db bound k_max &&
  hartogs_bulk_check bound db
```
