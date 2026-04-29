---
{
  "projection_kind": "taulib_declaration",
  "title": "refinement_resolution_check",
  "permalink": "/verify/taulib/docs/book-ii-transcendentals-iota-tau-confirmed/refinement-resolution-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Transcendentals.IotaTauConfirmed`.",
  "declaration_id": "TauLib.BookII.Transcendentals.IotaTauConfirmed::refinement_resolution_check",
  "declaration_slug": "refinement-resolution-check",
  "kind": "def",
  "name": "refinement_resolution_check",
  "module_name": "TauLib.BookII.Transcendentals.IotaTauConfirmed",
  "module_url": "/verify/taulib/docs/book-ii-transcendentals-iota-tau-confirmed/",
  "source_line_start": 134,
  "source_line_end": 141,
  "registry_ids": [
    "II.P07"
  ],
  "related_registry_items": [
    {
      "id": "II.P07",
      "title": "Bipolar Channel Independence",
      "url": "/registry/object/II.P07/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Transcendentals/IotaTauConfirmed.lean#L134-L141",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Transcendentals/IotaTauConfirmed.lean#L134-L141",
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
- Source path: [`TauLib/BookII/Transcendentals/IotaTauConfirmed.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Transcendentals/IotaTauConfirmed.lean#L134-L141)
- Source range: L134-L141
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.P07` — Bipolar Channel Independence

## Immediate Comment / Docstring

```lean
/-- [II.P07] Refinement resolution bound: at stage k, the
    resolution 1/P_k decreases monotonically.
    P_{k+1} > P_k for all k >= 0. -/
```

## Source Excerpt

```lean
def refinement_resolution_check (stages : TauIdx) : Bool :=
  go 1 (stages + 1)
where
  go (k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k > stages then true
    else primorial (k + 1) > primorial k && go (k + 1) (fuel - 1)
  termination_by fuel
```
