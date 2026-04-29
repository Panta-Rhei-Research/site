---
{
  "projection_kind": "taulib_declaration",
  "title": "ym_gap_persistence_check",
  "permalink": "/verify/taulib/docs/book-iii-doors-bridge-tightening/ym-gap-persistence-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Doors.BridgeTightening`.",
  "declaration_id": "TauLib.BookIII.Doors.BridgeTightening::ym_gap_persistence_check",
  "declaration_slug": "ym-gap-persistence-check",
  "kind": "def",
  "name": "ym_gap_persistence_check",
  "module_name": "TauLib.BookIII.Doors.BridgeTightening",
  "module_url": "/verify/taulib/docs/book-iii-doors-bridge-tightening/",
  "source_line_start": 101,
  "source_line_end": 114,
  "registry_ids": [
    "III.D94"
  ],
  "related_registry_items": [
    {
      "id": "III.D94",
      "title": "YM Mass Gap Persistence",
      "url": "/registry/object/III.D94/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/BridgeTightening.lean#L101-L114",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Doors.BridgeTightening",
        "url": "/verify/taulib/docs/book-iii-doors-bridge-tightening/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/BridgeTightening.lean#L101-L114",
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

- Module: [TauLib.BookIII.Doors.BridgeTightening](/verify/taulib/docs/book-iii-doors-bridge-tightening/)
- Source path: [`TauLib/BookIII/Doors/BridgeTightening.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/BridgeTightening.lean#L101-L114)
- Source range: L101-L114
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D94` — YM Mass Gap Persistence

## Immediate Comment / Docstring

```lean
/-- [III.D94] Gap persistence: τ-gap is positive and non-decreasing
    for k ≥ 3. -/
```

## Source Excerpt

```lean
def ym_gap_persistence_check (db : Nat) : Bool :=
  go 3 (db + 1)
where
  go (k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k > db then true
    else
      let gap_k := tau_gap k
      -- Positive gap
      let positive := gap_k > 0
      -- Non-decreasing (gap at k+1 ≥ gap at k)
      let monotone := if k < db then tau_gap (k + 1) >= gap_k else true
      positive && monotone && go (k + 1) (fuel - 1)
  termination_by fuel
```
