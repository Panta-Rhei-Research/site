---
{
  "projection_kind": "taulib_declaration",
  "title": "topological_pi_check",
  "permalink": "/verify/taulib/docs/book-ii-transcendentals-pi-earned/topological-pi-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Transcendentals.PiEarned`.",
  "declaration_id": "TauLib.BookII.Transcendentals.PiEarned::topological_pi_check",
  "declaration_slug": "topological-pi-check",
  "kind": "def",
  "name": "topological_pi_check",
  "module_name": "TauLib.BookII.Transcendentals.PiEarned",
  "module_url": "/verify/taulib/docs/book-ii-transcendentals-pi-earned/",
  "source_line_start": 126,
  "source_line_end": 132,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Transcendentals/PiEarned.lean#L126-L132",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Transcendentals.PiEarned",
        "url": "/verify/taulib/docs/book-ii-transcendentals-pi-earned/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Transcendentals/PiEarned.lean#L126-L132",
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

- Module: [TauLib.BookII.Transcendentals.PiEarned](/verify/taulib/docs/book-ii-transcendentals-pi-earned/)
- Source path: [`TauLib/BookII/Transcendentals/PiEarned.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Transcendentals/PiEarned.lean#L126-L132)
- Source range: L126-L132
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [II.T22, perspective 3] Topological evidence: the lemniscate
    half-period is pi * iota_tau. In scaled arithmetic:
    half_period * 10^6 = pi * iota_tau * 10^6
                       ~ 3141592 * 341304 / 10^6
                       ~ 1072793

    We verify the numerical relationship:
    pi_scaled * iota_tau_numer / iota_tau_denom should give a
    consistent half-period value. -/
```

## Source Excerpt

```lean
def topological_pi_check : Bool :=
  let pi_approx := pi_scaled 1000
  -- half-period = pi * iota_tau, scaled by 10^6
  -- = pi_scaled * 341304 / 1000000
  let half_period := pi_approx * 341304 / 1000000
  -- Should be approximately 1072793 (within 5%)
  half_period > 1000000 && half_period < 1150000
```
