---
{
  "projection_kind": "taulib_declaration",
  "title": "pvsnp_forbidden_damage",
  "permalink": "/verify/taulib/docs/book-iii-doors-bridge-tightening/pvsnp-forbidden-damage/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Doors.BridgeTightening`.",
  "declaration_id": "TauLib.BookIII.Doors.BridgeTightening::pvsnp_forbidden_damage",
  "declaration_slug": "pvsnp-forbidden-damage",
  "kind": "def",
  "name": "pvsnp_forbidden_damage",
  "module_name": "TauLib.BookIII.Doors.BridgeTightening",
  "module_url": "/verify/taulib/docs/book-iii-doors-bridge-tightening/",
  "source_line_start": 181,
  "source_line_end": 183,
  "registry_ids": [
    "III.T63"
  ],
  "related_registry_items": [
    {
      "id": "III.T63",
      "title": "P vs NP Forbidden Triple",
      "url": "/registry/object/III.T63/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/BridgeTightening.lean#L181-L183",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/BridgeTightening.lean#L181-L183",
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
- Source path: [`TauLib/BookIII/Doors/BridgeTightening.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/BridgeTightening.lean#L181-L183)
- Source range: L181-L183
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.T63` — P vs NP Forbidden Triple

## Immediate Comment / Docstring

```lean
/-- [III.T63] The three forbidden moves that collectively break the
    bridge for P vs NP:
    1. succinct_circuits (damage 3)
    2. exponential_quantification (damage 3)
    3. unbounded_fanout (damage 2)
    Total damage ≥ 3 → bridge breaks. -/
```

## Source Excerpt

```lean
def pvsnp_forbidden_damage : Nat :=
  -- Max of the three damages
  max (max 3 3) 2  -- succinct = 3, exponential = 3, fanout = 2
```
