---
{
  "projection_kind": "taulib_declaration",
  "title": "hartogs_bulk_coherent",
  "permalink": "/verify/taulib/docs/book-iii-prologue-hartogs-bulk/hartogs-bulk-coherent/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Prologue.HartogsBulk`.",
  "declaration_id": "TauLib.BookIII.Prologue.HartogsBulk::hartogs_bulk_coherent",
  "declaration_slug": "hartogs-bulk-coherent",
  "kind": "def",
  "name": "hartogs_bulk_coherent",
  "module_name": "TauLib.BookIII.Prologue.HartogsBulk",
  "module_url": "/verify/taulib/docs/book-iii-prologue-hartogs-bulk/",
  "source_line_start": 63,
  "source_line_end": 69,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Prologue/HartogsBulk.lean#L63-L69",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Prologue/HartogsBulk.lean#L63-L69",
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
- Source path: [`TauLib/BookIII/Prologue/HartogsBulk.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Prologue/HartogsBulk.lean#L63-L69)
- Source range: L63-L69
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D01` — Hartogs Bulk Projection

## Immediate Comment / Docstring

```lean
/-- [III.D01] Hartogs bulk coherence: the bulk coordinate at stage k+1
    projects correctly to stage k. This is the local version of tower
    coherence applied to the spatial (Hartogs-filled) interior. -/
```

## Source Excerpt

```lean
def hartogs_bulk_coherent (hb : HartogsBulk) (k : TauIdx) : Bool :=
  if k >= hb.stage then true
  else
    let bulk_at_stage := reduce (hb.boundary_b + hb.boundary_c) hb.stage
    let projected := reduce bulk_at_stage k
    let direct := reduce (hb.boundary_b + hb.boundary_c) k
    projected == direct
```
