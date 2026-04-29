---
{
  "projection_kind": "taulib_declaration",
  "title": "pi_convergence_check",
  "permalink": "/verify/taulib/docs/book-ii-transcendentals-pi-earned/pi-convergence-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Transcendentals.PiEarned`.",
  "declaration_id": "TauLib.BookII.Transcendentals.PiEarned::pi_convergence_check",
  "declaration_slug": "pi-convergence-check",
  "kind": "def",
  "name": "pi_convergence_check",
  "module_name": "TauLib.BookII.Transcendentals.PiEarned",
  "module_url": "/verify/taulib/docs/book-ii-transcendentals-pi-earned/",
  "source_line_start": 74,
  "source_line_end": 76,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Transcendentals/PiEarned.lean#L74-L76",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Transcendentals/PiEarned.lean#L74-L76",
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
- Source path: [`TauLib/BookII/Transcendentals/PiEarned.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Transcendentals/PiEarned.lean#L74-L76)
- Source range: L74-L76
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [II.T22, perspective 1] Leibniz convergence: with enough terms,
    the scaled pi approximation falls within a reasonable range.

    pi * 10^6 = 3141592. With 1000 terms, Leibniz gives ~3140592
    (Leibniz converges slowly: error ~ 1/N).
    We check it lands in [3100000, 3200000]. -/
```

## Source Excerpt

```lean
def pi_convergence_check : Bool :=
  let pi_approx := pi_scaled 1000
  pi_approx > 3100000 && pi_approx < 3200000
```
