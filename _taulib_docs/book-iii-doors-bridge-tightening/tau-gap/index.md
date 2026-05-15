---
{
  "projection_kind": "taulib_declaration",
  "title": "tau_gap",
  "permalink": "/corpus/taulib/docs/book-iii-doors-bridge-tightening/tau-gap/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Doors.BridgeTightening`.",
  "declaration_id": "TauLib.BookIII.Doors.BridgeTightening::tau_gap",
  "declaration_slug": "tau-gap",
  "kind": "def",
  "name": "tau_gap",
  "module_name": "TauLib.BookIII.Doors.BridgeTightening",
  "module_url": "/corpus/taulib/docs/book-iii-doors-bridge-tightening/",
  "source_line_start": 94,
  "source_line_end": 97,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/BridgeTightening.lean#L94-L97",
  "formal_status": "defined",
  "declaration_role": "data/computed value",
  "formal_status_label": "data/computed value",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Doors.BridgeTightening",
        "url": "/corpus/taulib/docs/book-iii-doors-bridge-tightening/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/BridgeTightening.lean#L94-L97",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "role": "data/computed value",
      "status": "data/computed value"
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

- Module: [TauLib.BookIII.Doors.BridgeTightening](/corpus/taulib/docs/book-iii-doors-bridge-tightening/)
- Source path: [`TauLib/BookIII/Doors/BridgeTightening.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/BridgeTightening.lean#L94-L97)
- Source range: L94-L97
- Kind: `def`
- Public role: `data/computed value`
- Formal status hint: `data/computed value`

## Registry Links

- `III.D94` — YM Mass Gap Persistence

## Immediate Comment / Docstring

```lean
/-- [III.D94] τ-gap at level k: minimum of B/C sector products.
    Uses split_zeta from SplitComplexZeta.lean. -/
```

## Source Excerpt

```lean
def tau_gap (k : Nat) : Nat :=
  let b := split_zeta_b k
  let c := split_zeta_c k
  min b c
```
