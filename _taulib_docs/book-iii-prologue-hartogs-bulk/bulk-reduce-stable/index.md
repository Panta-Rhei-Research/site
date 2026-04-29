---
{
  "projection_kind": "taulib_declaration",
  "title": "bulk_reduce_stable",
  "permalink": "/verify/taulib/docs/book-iii-prologue-hartogs-bulk/bulk-reduce-stable/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Prologue.HartogsBulk`.",
  "declaration_id": "TauLib.BookIII.Prologue.HartogsBulk::bulk_reduce_stable",
  "declaration_slug": "bulk-reduce-stable",
  "kind": "theorem",
  "name": "bulk_reduce_stable",
  "module_name": "TauLib.BookIII.Prologue.HartogsBulk",
  "module_url": "/verify/taulib/docs/book-iii-prologue-hartogs-bulk/",
  "source_line_start": 155,
  "source_line_end": 160,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Prologue/HartogsBulk.lean#L155-L160",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Prologue/HartogsBulk.lean#L155-L160",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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
- Source path: [`TauLib/BookIII/Prologue/HartogsBulk.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Prologue/HartogsBulk.lean#L155-L160)
- Source range: L155-L160
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.D01` — Hartogs Bulk Projection

## Immediate Comment / Docstring

```lean
/-- [III.D01] Bulk projection is reduce-stable:
    reduce(bulk_coordinate(hb), hb.stage) = bulk_coordinate(hb). -/
```

## Source Excerpt

```lean
theorem bulk_reduce_stable (hb : HartogsBulk) :
    reduce (bulk_coordinate hb) hb.stage = bulk_coordinate hb := by
  simp only [bulk_coordinate, reduce]
  exact Nat.mod_mod_of_dvd _ (dvd_refl (primorial hb.stage))

end Tau.BookIII.Prologue
```
