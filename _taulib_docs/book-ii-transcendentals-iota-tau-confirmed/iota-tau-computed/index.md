---
{
  "projection_kind": "taulib_declaration",
  "title": "iota_tau_computed",
  "permalink": "/verify/taulib/docs/book-ii-transcendentals-iota-tau-confirmed/iota-tau-computed/",
  "summary_short": "`def` declaration in `TauLib.BookII.Transcendentals.IotaTauConfirmed`.",
  "declaration_id": "TauLib.BookII.Transcendentals.IotaTauConfirmed::iota_tau_computed",
  "declaration_slug": "iota-tau-computed",
  "kind": "def",
  "name": "iota_tau_computed",
  "module_name": "TauLib.BookII.Transcendentals.IotaTauConfirmed",
  "module_url": "/verify/taulib/docs/book-ii-transcendentals-iota-tau-confirmed/",
  "source_line_start": 44,
  "source_line_end": 49,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Transcendentals/IotaTauConfirmed.lean#L44-L49",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Transcendentals/IotaTauConfirmed.lean#L44-L49",
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
- Source path: [`TauLib/BookII/Transcendentals/IotaTauConfirmed.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Transcendentals/IotaTauConfirmed.lean#L44-L49)
- Source range: L44-L49
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Compute iota_tau * scale using earned pi and e approximations.
    iota_tau = 2 / (pi + e).
    In scaled arithmetic: iota_tau * scale = 2 * scale^2 / (pi_scaled + e_scaled).

    pi_scaled and e_scaled are both in units of 10^6. -/
```

## Source Excerpt

```lean
def iota_tau_computed (pi_terms e_terms scale : Nat) : Nat :=
  let pi_approx := leibniz_pi_scaled pi_terms scale
  let e_approx := e_factorial_scaled e_terms scale
  let denom := pi_approx + e_approx
  if denom == 0 then 0
  else 2 * scale * scale / denom
```
