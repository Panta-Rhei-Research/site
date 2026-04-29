---
{
  "projection_kind": "taulib_declaration",
  "title": "TauReal.iota_tau",
  "permalink": "/verify/taulib/docs/book-i-boundary-tau-real-iota-tau/iota-tau/",
  "summary_short": "`def` declaration in `TauLib.BookI.Boundary.TauRealIotaTau`.",
  "declaration_id": "TauLib.BookI.Boundary.TauRealIotaTau::TauReal.iota_tau",
  "declaration_slug": "iota-tau",
  "kind": "def",
  "name": "TauReal.iota_tau",
  "module_name": "TauLib.BookI.Boundary.TauRealIotaTau",
  "module_url": "/verify/taulib/docs/book-i-boundary-tau-real-iota-tau/",
  "source_line_start": 98,
  "source_line_end": 99,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealIotaTau.lean#L98-L99",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.TauRealIotaTau",
        "url": "/verify/taulib/docs/book-i-boundary-tau-real-iota-tau/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealIotaTau.lean#L98-L99",
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

- Module: [TauLib.BookI.Boundary.TauRealIotaTau](/verify/taulib/docs/book-i-boundary-tau-real-iota-tau/)
- Source path: [`TauLib/BookI/Boundary/TauRealIotaTau.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealIotaTau.lean#L98-L99)
- Source range: L98-L99
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The master constant `iota_tau`, structurally defined as `2 / (π + e)`
    in the Cauchy completion of TauRat.

    This replaces the previous `Iota.lean` fiat-rational approach
    (`iota_tau_numer := 341304`, `iota_tau_denom := 1000000`) with an
    element that is **genuinely** the Cauchy class of `2/(π + e)`,
    rather than a decimal truncation of its numerical value. -/
```

## Source Excerpt

```lean
def TauReal.iota_tau : TauReal :=
  TauReal.div TauReal.two (TauReal.pi.add TauReal.e)
```
