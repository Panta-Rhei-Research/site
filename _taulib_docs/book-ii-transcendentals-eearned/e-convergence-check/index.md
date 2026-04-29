---
{
  "projection_kind": "taulib_declaration",
  "title": "e_convergence_check",
  "permalink": "/verify/taulib/docs/book-ii-transcendentals-eearned/e-convergence-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Transcendentals.EEarned`.",
  "declaration_id": "TauLib.BookII.Transcendentals.EEarned::e_convergence_check",
  "declaration_slug": "e-convergence-check",
  "kind": "def",
  "name": "e_convergence_check",
  "module_name": "TauLib.BookII.Transcendentals.EEarned",
  "module_url": "/verify/taulib/docs/book-ii-transcendentals-eearned/",
  "source_line_start": 62,
  "source_line_end": 64,
  "registry_ids": [
    "II.T23"
  ],
  "related_registry_items": [
    {
      "id": "II.T23",
      "title": "e from Index Arithmetic",
      "url": "/registry/object/II.T23/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Transcendentals/EEarned.lean#L62-L64",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Transcendentals.EEarned",
        "url": "/verify/taulib/docs/book-ii-transcendentals-eearned/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Transcendentals/EEarned.lean#L62-L64",
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

- Module: [TauLib.BookII.Transcendentals.EEarned](/verify/taulib/docs/book-ii-transcendentals-eearned/)
- Source path: [`TauLib/BookII/Transcendentals/EEarned.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Transcendentals/EEarned.lean#L62-L64)
- Source range: L62-L64
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.T23` — e from Index Arithmetic

## Immediate Comment / Docstring

```lean
/-- [II.T23] e from index arithmetic: e * 10^6 ~ 2718281.
    The factorial series converges MUCH faster than Leibniz:
    10 terms gives 6+ digits of accuracy.
    Check: result in [2700000, 2750000]. -/
```

## Source Excerpt

```lean
def e_convergence_check : Bool :=
  let e_approx := e_scaled 10
  e_approx > 2700000 && e_approx < 2750000
```
