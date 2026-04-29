---
{
  "projection_kind": "taulib_declaration",
  "title": "rh_gap_char",
  "permalink": "/verify/taulib/docs/book-iii-doors-bridge-tightening/rh-gap-char/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Doors.BridgeTightening`.",
  "declaration_id": "TauLib.BookIII.Doors.BridgeTightening::rh_gap_char",
  "declaration_slug": "rh-gap-char",
  "kind": "def",
  "name": "rh_gap_char",
  "module_name": "TauLib.BookIII.Doors.BridgeTightening",
  "module_url": "/verify/taulib/docs/book-iii-doors-bridge-tightening/",
  "source_line_start": 73,
  "source_line_end": 86,
  "registry_ids": [
    "III.D93"
  ],
  "related_registry_items": [
    {
      "id": "III.D93",
      "title": "RH Spectral Gap Characterization",
      "url": "/registry/object/III.D93/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/BridgeTightening.lean#L73-L86",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/BridgeTightening.lean#L73-L86",
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
- Source path: [`TauLib/BookIII/Doors/BridgeTightening.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/BridgeTightening.lean#L73-L86)
- Source range: L73-L86
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D93` — RH Spectral Gap Characterization

## Immediate Comment / Docstring

```lean
/-- [III.D93] RH gap characterization: the finite checks pass, but the
    infinite-limit assertion (O₃) is the gap. Characterize precisely. -/
```

## Source Excerpt

```lean
def rh_gap_char (db : Nat) : Bool :=
  go 1 (db + 1)
where
  go (k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k > db then true
    else
      -- Finite check passes at every stage
      let finite_ok := rh_internal_check k
      -- Gap measure: number of eigenvalues checked (finite)
      -- vs total eigenvalues needed (infinite)
      let gap_finite := k > 0  -- gap exists whenever k is finite
      finite_ok && gap_finite && go (k + 1) (fuel - 1)
  termination_by fuel
```
