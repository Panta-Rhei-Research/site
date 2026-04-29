---
{
  "projection_kind": "taulib_declaration",
  "title": "archimedean_bridge_check",
  "permalink": "/verify/taulib/docs/book-ii-transcendentals-iota-tau-confirmed/archimedean-bridge-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Transcendentals.IotaTauConfirmed`.",
  "declaration_id": "TauLib.BookII.Transcendentals.IotaTauConfirmed::archimedean_bridge_check",
  "declaration_slug": "archimedean-bridge-check",
  "kind": "def",
  "name": "archimedean_bridge_check",
  "module_name": "TauLib.BookII.Transcendentals.IotaTauConfirmed",
  "module_url": "/verify/taulib/docs/book-ii-transcendentals-iota-tau-confirmed/",
  "source_line_start": 104,
  "source_line_end": 112,
  "registry_ids": [
    "II.D34"
  ],
  "related_registry_items": [
    {
      "id": "II.D34",
      "title": "Archimedean Bridge",
      "url": "/registry/object/II.D34/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Transcendentals/IotaTauConfirmed.lean#L104-L112",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Transcendentals/IotaTauConfirmed.lean#L104-L112",
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
- Source path: [`TauLib/BookII/Transcendentals/IotaTauConfirmed.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Transcendentals/IotaTauConfirmed.lean#L104-L112)
- Source range: L104-L112
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D34` — Archimedean Bridge

## Immediate Comment / Docstring

```lean
/-- [II.D34] Archimedean bridge: iota_tau mediates between
    the Archimedean world (pi, e from limits) and the profinite
    world (tau^3 from primorial inverse system).

    The resolution at stage k is 1/P_k. The scale where
    resolution crosses iota_tau happens between k=1 and k=2:
    1/P_1 = 1/2 = 0.5 > iota_tau ~ 0.341 > 1/P_2 = 1/6 ~ 0.167.

    In scaled integer arithmetic: scale/P_k vs iota_tau_scaled. -/
```

## Source Excerpt

```lean
def archimedean_bridge_check : Bool :=
  let scale : Nat := 1000000
  let iota := iota_tau_computed 2000 12 scale
  -- Resolution at k=1: scale/P_1 = 1000000/2 = 500000
  let res1 := scale / primorial 1
  -- Resolution at k=2: scale/P_2 = 1000000/6 = 166666
  let res2 := scale / primorial 2
  -- iota_tau sits between the two resolution levels
  res1 > iota && iota > res2
```
