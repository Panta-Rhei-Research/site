---
{
  "projection_kind": "taulib_declaration",
  "title": "bridge_interpolation_check",
  "permalink": "/verify/taulib/docs/book-ii-transcendentals-iota-tau-confirmed/bridge-interpolation-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Transcendentals.IotaTauConfirmed`.",
  "declaration_id": "TauLib.BookII.Transcendentals.IotaTauConfirmed::bridge_interpolation_check",
  "declaration_slug": "bridge-interpolation-check",
  "kind": "def",
  "name": "bridge_interpolation_check",
  "module_name": "TauLib.BookII.Transcendentals.IotaTauConfirmed",
  "module_url": "/verify/taulib/docs/book-ii-transcendentals-iota-tau-confirmed/",
  "source_line_start": 118,
  "source_line_end": 125,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Transcendentals/IotaTauConfirmed.lean#L118-L125",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Transcendentals.IotaTauConfirmed",
        "url": "/verify/taulib/docs/book-ii-transcendentals-iota-tau-confirmed/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Transcendentals/IotaTauConfirmed.lean#L118-L125",
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

- Module: [TauLib.BookII.Transcendentals.IotaTauConfirmed](/verify/taulib/docs/book-ii-transcendentals-iota-tau-confirmed/)
- Source path: [`TauLib/BookII/Transcendentals/IotaTauConfirmed.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Transcendentals/IotaTauConfirmed.lean#L118-L125)
- Source range: L118-L125
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Bridge characterization: iota_tau as the stage-1/stage-2
    interpolation constant. The fact that iota_tau falls between
    1/P_1 and 1/P_2 means it governs the first refinement step
    where the primorial ladder becomes finer than the master constant. -/
```

## Source Excerpt

```lean
def bridge_interpolation_check : Bool :=
  let scale : Nat := 1000000
  let iota := iota_tau_computed 2000 12 scale
  -- P_1 = 2, P_2 = 6, P_3 = 30, P_4 = 210
  -- iota * P_1 = ~682918 < scale (iota < 1/P_1 * P_1 = 1, trivially)
  -- iota * P_2 = ~2048286 > scale (iota > 1/P_2, i.e. iota*P_2 > 1)
  iota * primorial 1 < scale * 2 &&  -- iota < 1
  iota * primorial 2 > scale         -- iota > 1/6
```
