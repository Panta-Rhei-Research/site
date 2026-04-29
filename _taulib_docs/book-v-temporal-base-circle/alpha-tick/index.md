---
{
  "projection_kind": "taulib_declaration",
  "title": "AlphaTick",
  "permalink": "/verify/taulib/docs/book-v-temporal-base-circle/alpha-tick/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Temporal.BaseCircle`.",
  "declaration_id": "TauLib.BookV.Temporal.BaseCircle::AlphaTick",
  "declaration_slug": "alpha-tick",
  "kind": "structure",
  "name": "AlphaTick",
  "module_name": "TauLib.BookV.Temporal.BaseCircle",
  "module_url": "/verify/taulib/docs/book-v-temporal-base-circle/",
  "source_line_start": 102,
  "source_line_end": 109,
  "registry_ids": [
    "V.D16"
  ],
  "related_registry_items": [
    {
      "id": "V.D16",
      "title": "Alpha-Tick",
      "url": "/registry/object/V.D16/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/BaseCircle.lean#L102-L109",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Temporal.BaseCircle",
        "url": "/verify/taulib/docs/book-v-temporal-base-circle/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/BaseCircle.lean#L102-L109",
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

- Module: [TauLib.BookV.Temporal.BaseCircle](/verify/taulib/docs/book-v-temporal-base-circle/)
- Source path: [`TauLib/BookV/Temporal/BaseCircle.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/BaseCircle.lean#L102-L109)
- Source range: L102-L109
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D16` — Alpha-Tick

## Immediate Comment / Docstring

```lean
/-- [V.D16] Alpha-tick: the minimal temporal passage from depth n to
    depth n+1 in the refinement tower.

    Δ_n := (α_n → α_{n+1})

    Each tick is a single irreversible refinement step. The source
    depth must be strictly less than the target depth. -/
```

## Source Excerpt

```lean
structure AlphaTick where
  /-- Source proto-time (earlier). -/
  source : ProtoTime
  /-- Target proto-time (later). -/
  target : ProtoTime
  /-- Target is exactly one step after source. -/
  consecutive : target.tick = source.tick + 1
  deriving Repr
```
