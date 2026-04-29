---
{
  "projection_kind": "taulib_declaration",
  "title": "three_perspectives_pi_check",
  "permalink": "/verify/taulib/docs/book-ii-transcendentals-pi-earned/three-perspectives-pi-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Transcendentals.PiEarned`.",
  "declaration_id": "TauLib.BookII.Transcendentals.PiEarned::three_perspectives_pi_check",
  "declaration_slug": "three-perspectives-pi-check",
  "kind": "def",
  "name": "three_perspectives_pi_check",
  "module_name": "TauLib.BookII.Transcendentals.PiEarned",
  "module_url": "/verify/taulib/docs/book-ii-transcendentals-pi-earned/",
  "source_line_start": 135,
  "source_line_end": 138,
  "registry_ids": [
    "II.T22"
  ],
  "related_registry_items": [
    {
      "id": "II.T22",
      "title": "Three Perspectives on Pi",
      "url": "/registry/object/II.T22/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Transcendentals/PiEarned.lean#L135-L138",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Transcendentals/PiEarned.lean#L135-L138",
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
- Source path: [`TauLib/BookII/Transcendentals/PiEarned.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Transcendentals/PiEarned.lean#L135-L138)
- Source range: L135-L138
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.T22` — Three Perspectives on Pi

## Immediate Comment / Docstring

```lean
/-- [II.T22] Full three-perspective check. -/
```

## Source Excerpt

```lean
def three_perspectives_pi_check (bound : TauIdx) : Bool :=
  pi_convergence_check &&
  spectral_pi_check bound &&
  topological_pi_check
```
