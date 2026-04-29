---
{
  "projection_kind": "taulib_declaration",
  "title": "prototime_to_nat",
  "permalink": "/verify/taulib/docs/book-iv-arena-refinement-tower/prototime-to-nat/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Arena.RefinementTower`.",
  "declaration_id": "TauLib.BookIV.Arena.RefinementTower::prototime_to_nat",
  "declaration_slug": "prototime-to-nat",
  "kind": "def",
  "name": "prototime_to_nat",
  "module_name": "TauLib.BookIV.Arena.RefinementTower",
  "module_url": "/verify/taulib/docs/book-iv-arena-refinement-tower/",
  "source_line_start": 116,
  "source_line_end": 116,
  "registry_ids": [
    "IV.P148"
  ],
  "related_registry_items": [
    {
      "id": "IV.P148",
      "title": "NNO from the alpha-Orbit",
      "url": "/registry/object/IV.P148/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/RefinementTower.lean#L116-L116",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Arena.RefinementTower",
        "url": "/verify/taulib/docs/book-iv-arena-refinement-tower/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/RefinementTower.lean#L116-L116",
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

- Module: [TauLib.BookIV.Arena.RefinementTower](/verify/taulib/docs/book-iv-arena-refinement-tower/)
- Source path: [`TauLib/BookIV/Arena/RefinementTower.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/RefinementTower.lean#L116-L116)
- Source range: L116-L116
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `IV.P148` — NNO from the alpha-Orbit

## Immediate Comment / Docstring

```lean
/-- [IV.P148] The natural numbers object ℕ is recovered from α-orbit
    depth indexing: depth 1 ↦ 0, depth 2 ↦ 1, ... -/
```

## Source Excerpt

```lean
def prototime_to_nat (t : ProtoTime) : Nat := t.tick - 1
```
