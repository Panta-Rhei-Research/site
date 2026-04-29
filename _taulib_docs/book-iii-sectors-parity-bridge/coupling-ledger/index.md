---
{
  "projection_kind": "taulib_declaration",
  "title": "coupling_ledger",
  "permalink": "/verify/taulib/docs/book-iii-sectors-parity-bridge/coupling-ledger/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Sectors.ParityBridge`.",
  "declaration_id": "TauLib.BookIII.Sectors.ParityBridge::coupling_ledger",
  "declaration_slug": "coupling-ledger",
  "kind": "def",
  "name": "coupling_ledger",
  "module_name": "TauLib.BookIII.Sectors.ParityBridge",
  "module_url": "/verify/taulib/docs/book-iii-sectors-parity-bridge/",
  "source_line_start": 88,
  "source_line_end": 107,
  "registry_ids": [
    "III.D18"
  ],
  "related_registry_items": [
    {
      "id": "III.D18",
      "title": "Coupling Ledger",
      "url": "/registry/object/III.D18/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Sectors/ParityBridge.lean#L88-L107",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Sectors.ParityBridge",
        "url": "/verify/taulib/docs/book-iii-sectors-parity-bridge/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Sectors/ParityBridge.lean#L88-L107",
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

- Module: [TauLib.BookIII.Sectors.ParityBridge](/verify/taulib/docs/book-iii-sectors-parity-bridge/)
- Source path: [`TauLib/BookIII/Sectors/ParityBridge.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Sectors/ParityBridge.lean#L88-L107)
- Source range: L88-L107
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D18` — Coupling Ledger

## Immediate Comment / Docstring

```lean
/-- [III.D18] Build the 10-entry coupling ledger:
    upper triangle of 4×4 primitive sector matrix. -/
```

## Source Excerpt

```lean
def coupling_ledger (bound : TauIdx) : List CouplingEntry :=
  let secs := [Sector.D, Sector.A, Sector.B, Sector.C]
  go_i secs secs bound []
where
  go_i (si_list sj_full : List Sector) (bound : TauIdx) (acc : List CouplingEntry) :
      List CouplingEntry :=
    match si_list with
    | [] => acc
    | si :: rest =>
      let new_entries := go_j si sj_full bound []
      go_i rest sj_full bound (acc ++ new_entries)
  go_j (si : Sector) (sj_list : List Sector) (bound : TauIdx) (acc : List CouplingEntry) :
      List CouplingEntry :=
    match sj_list with
    | [] => acc
    | sj :: rest =>
      let acc' := if si.toNat <= sj.toNat then
        acc ++ [⟨si, sj, sector_coupling si sj bound⟩]
      else acc
      go_j si rest bound acc'
```
