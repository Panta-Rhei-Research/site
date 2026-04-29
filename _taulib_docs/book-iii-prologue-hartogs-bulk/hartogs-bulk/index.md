---
{
  "projection_kind": "taulib_declaration",
  "title": "HartogsBulk",
  "permalink": "/verify/taulib/docs/book-iii-prologue-hartogs-bulk/hartogs-bulk/",
  "summary_short": "`structure` declaration in `TauLib.BookIII.Prologue.HartogsBulk`.",
  "declaration_id": "TauLib.BookIII.Prologue.HartogsBulk::HartogsBulk",
  "declaration_slug": "hartogs-bulk",
  "kind": "structure",
  "name": "HartogsBulk",
  "module_name": "TauLib.BookIII.Prologue.HartogsBulk",
  "module_url": "/verify/taulib/docs/book-iii-prologue-hartogs-bulk/",
  "source_line_start": 48,
  "source_line_end": 52,
  "registry_ids": [
    "III.D01"
  ],
  "related_registry_items": [
    {
      "id": "III.D01",
      "title": "Hartogs Bulk Projection",
      "url": "/registry/object/III.D01/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Prologue/HartogsBulk.lean#L48-L52",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Prologue/HartogsBulk.lean#L48-L52",
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

- Module: [TauLib.BookIII.Prologue.HartogsBulk](/verify/taulib/docs/book-iii-prologue-hartogs-bulk/)
- Source path: [`TauLib/BookIII/Prologue/HartogsBulk.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Prologue/HartogsBulk.lean#L48-L52)
- Source range: L48-L52
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `III.D01` — Hartogs Bulk Projection

## Immediate Comment / Docstring

```lean
/-- [III.D01] Hartogs Bulk Projection: at each stage k, the bulk coordinate
    is the interior value obtained by Hartogs extension from boundary data.
    Concretely: given boundary values at stage k (the reduce-compatible map),
    the bulk value is the unique Hartogs extension = reduce(x, k).

    The "3D space" perceived at a point is the Hartogs-filled interior of
    the local T² fiber. We model this as: for each pair (boundary_val, stage),
    the bulk projection is the reduce of their sum (combining solenoidal
    coordinates into a single interior coordinate). -/
```

## Source Excerpt

```lean
structure HartogsBulk where
  boundary_b : TauIdx  -- B-channel boundary value
  boundary_c : TauIdx  -- C-channel boundary value
  stage : TauIdx       -- primorial stage
  deriving Repr, DecidableEq
```
