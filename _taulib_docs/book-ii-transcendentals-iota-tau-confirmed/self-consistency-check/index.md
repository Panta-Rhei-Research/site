---
{
  "projection_kind": "taulib_declaration",
  "title": "self_consistency_check",
  "permalink": "/verify/taulib/docs/book-ii-transcendentals-iota-tau-confirmed/self-consistency-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Transcendentals.IotaTauConfirmed`.",
  "declaration_id": "TauLib.BookII.Transcendentals.IotaTauConfirmed::self_consistency_check",
  "declaration_slug": "self-consistency-check",
  "kind": "def",
  "name": "self_consistency_check",
  "module_name": "TauLib.BookII.Transcendentals.IotaTauConfirmed",
  "module_url": "/verify/taulib/docs/book-ii-transcendentals-iota-tau-confirmed/",
  "source_line_start": 76,
  "source_line_end": 89,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Transcendentals/IotaTauConfirmed.lean#L76-L89",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Transcendentals/IotaTauConfirmed.lean#L76-L89",
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
- Source path: [`TauLib/BookII/Transcendentals/IotaTauConfirmed.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Transcendentals/IotaTauConfirmed.lean#L76-L89)
- Source range: L76-L89
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Self-consistency: pi + e = 2 / iota_tau.
    In scaled arithmetic: (pi + e) * iota = 2 * scale.
    Check: pi_scaled + e_scaled ~ 2 * scale^2 / iota_scaled. -/
```

## Source Excerpt

```lean
def self_consistency_check : Bool :=
  let scale : Nat := 1000000
  let pi_approx := leibniz_pi_scaled 2000 scale
  let e_approx := e_factorial_scaled 12 scale
  let pe_sum := pi_approx + e_approx
  -- pe_sum should be close to 5859873 (= pi + e scaled by 10^6)
  -- 2 * 10^6 / pe_sum should give iota_tau
  -- Equivalently: pe_sum * iota ~ 2 * 10^6
  let iota := iota_tau_computed 2000 12 scale
  -- pe_sum * iota / scale ~ 2 * scale
  let product := pe_sum * iota / scale
  -- product should be close to 2 * scale = 2000000
  -- Allow 2% tolerance: within [1960000, 2040000]
  product > 1960000 && product < 2040000
```
