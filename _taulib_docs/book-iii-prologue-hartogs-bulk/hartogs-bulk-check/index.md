---
{
  "projection_kind": "taulib_declaration",
  "title": "hartogs_bulk_check",
  "permalink": "/verify/taulib/docs/book-iii-prologue-hartogs-bulk/hartogs-bulk-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Prologue.HartogsBulk`.",
  "declaration_id": "TauLib.BookIII.Prologue.HartogsBulk::hartogs_bulk_check",
  "declaration_slug": "hartogs-bulk-check",
  "kind": "def",
  "name": "hartogs_bulk_check",
  "module_name": "TauLib.BookIII.Prologue.HartogsBulk",
  "module_url": "/verify/taulib/docs/book-iii-prologue-hartogs-bulk/",
  "source_line_start": 73,
  "source_line_end": 84,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Prologue/HartogsBulk.lean#L73-L84",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Prologue/HartogsBulk.lean#L73-L84",
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
- Source path: [`TauLib/BookIII/Prologue/HartogsBulk.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Prologue/HartogsBulk.lean#L73-L84)
- Source range: L73-L84
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D01` — Hartogs Bulk Projection

## Immediate Comment / Docstring

```lean
/-- [III.D01] Full Hartogs bulk check: for all boundary pairs in range,
    verify tower coherence of the bulk projection. -/
```

## Source Excerpt

```lean
def hartogs_bulk_check (bound db : TauIdx) : Bool :=
  go 0 0 1 ((bound + 1) * (bound + 1) * (db + 1))
where
  go (b c k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if b > bound then true
    else if c > bound then go (b + 1) 0 1 (fuel - 1)
    else if k >= db then go b (c + 1) 1 (fuel - 1)
    else
      let hb : HartogsBulk := ⟨b, c, db⟩
      hartogs_bulk_coherent hb k && go b c (k + 1) (fuel - 1)
  termination_by fuel
```
