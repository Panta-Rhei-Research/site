---
{
  "projection_kind": "taulib_declaration",
  "title": "pi_improvement_check",
  "permalink": "/verify/taulib/docs/book-ii-transcendentals-pi-earned/pi-improvement-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Transcendentals.PiEarned`.",
  "declaration_id": "TauLib.BookII.Transcendentals.PiEarned::pi_improvement_check",
  "declaration_slug": "pi-improvement-check",
  "kind": "def",
  "name": "pi_improvement_check",
  "module_name": "TauLib.BookII.Transcendentals.PiEarned",
  "module_url": "/verify/taulib/docs/book-ii-transcendentals-pi-earned/",
  "source_line_start": 81,
  "source_line_end": 94,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Transcendentals/PiEarned.lean#L81-L94",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Transcendentals/PiEarned.lean#L81-L94",
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
- Source path: [`TauLib/BookII/Transcendentals/PiEarned.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Transcendentals/PiEarned.lean#L81-L94)
- Source range: L81-L94
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Monotone improvement: more terms should bring the approximation
    closer to the true value. Evidence: the difference between
    successive approximations decreases. -/
```

## Source Excerpt

```lean
def pi_improvement_check : Bool :=
  let p100 := pi_scaled 100
  let p500 := pi_scaled 500
  let p1000 := pi_scaled 1000
  -- All should be in a reasonable range
  p100 > 3000000 && p100 < 3300000 &&
  p500 > 3100000 && p500 < 3200000 &&
  p1000 > 3100000 && p1000 < 3200000 &&
  -- p1000 should be closer to 3141592 than p100
  -- i.e., |p1000 - 3141592| < |p100 - 3141592|
  let target : Nat := 3141592
  let err1000 := if p1000 >= target then p1000 - target else target - p1000
  let err100 := if p100 >= target then p100 - target else target - p100
  err1000 < err100
```
