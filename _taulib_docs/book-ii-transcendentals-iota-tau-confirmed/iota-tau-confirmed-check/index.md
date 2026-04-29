---
{
  "projection_kind": "taulib_declaration",
  "title": "iota_tau_confirmed_check",
  "permalink": "/verify/taulib/docs/book-ii-transcendentals-iota-tau-confirmed/iota-tau-confirmed-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Transcendentals.IotaTauConfirmed`.",
  "declaration_id": "TauLib.BookII.Transcendentals.IotaTauConfirmed::iota_tau_confirmed_check",
  "declaration_slug": "iota-tau-confirmed-check",
  "kind": "def",
  "name": "iota_tau_confirmed_check",
  "module_name": "TauLib.BookII.Transcendentals.IotaTauConfirmed",
  "module_url": "/verify/taulib/docs/book-ii-transcendentals-iota-tau-confirmed/",
  "source_line_start": 56,
  "source_line_end": 58,
  "registry_ids": [
    "II.T25"
  ],
  "related_registry_items": [
    {
      "id": "II.T25",
      "title": "Master Constant Confirmed",
      "url": "/registry/object/II.T25/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Transcendentals/IotaTauConfirmed.lean#L56-L58",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Transcendentals/IotaTauConfirmed.lean#L56-L58",
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
- Source path: [`TauLib/BookII/Transcendentals/IotaTauConfirmed.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Transcendentals/IotaTauConfirmed.lean#L56-L58)
- Source range: L56-L58
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.T25` — Master Constant Confirmed

## Immediate Comment / Docstring

```lean
/-- [II.T25] Master constant confirmed: iota_tau ~ 0.341304.
    iota_tau * 10^6 ~ 341304.
    With 2000 Leibniz terms and 12 factorial terms:
    pi ~ 3141092, e ~ 2718281, sum ~ 5859373
    iota ~ 2 * 10^12 / 5859373 ~ 341381 (within 1% of 341304). -/
```

## Source Excerpt

```lean
def iota_tau_confirmed_check : Bool :=
  let iota := iota_tau_computed 2000 12 1000000
  iota > 335000 && iota < 350000
```
