---
{
  "projection_kind": "taulib_declaration",
  "title": "spectral_scan",
  "permalink": "/verify/taulib/docs/book-i-polarity-spectral/spectral-scan/",
  "summary_short": "`def` declaration in `TauLib.BookI.Polarity.Spectral`.",
  "declaration_id": "TauLib.BookI.Polarity.Spectral::spectral_scan",
  "declaration_slug": "spectral-scan",
  "kind": "def",
  "name": "spectral_scan",
  "module_name": "TauLib.BookI.Polarity.Spectral",
  "module_url": "/verify/taulib/docs/book-i-polarity-spectral/",
  "source_line_start": 36,
  "source_line_end": 48,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/Spectral.lean#L36-L48",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Polarity.Spectral",
        "url": "/verify/taulib/docs/book-i-polarity-spectral/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/Spectral.lean#L36-L48",
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

- Module: [TauLib.BookI.Polarity.Spectral](/verify/taulib/docs/book-i-polarity-spectral/)
- Source path: [`TauLib/BookI/Polarity/Spectral.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/Spectral.lean#L36-L48)
- Source range: L36-L48
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Scan objects from i to N, tracking max B and C for objects with A = p. -/
```

## Source Excerpt

```lean
def spectral_scan (p i N bmax cmax : TauIdx) (fuel : Nat) : TauIdx × TauIdx :=
  if fuel = 0 then (bmax, cmax)
  else if i > N then (bmax, cmax)
  else
    if coord_A i == p then
      let b := coord_B i
      let c := coord_C i
      let bmax' := if b > bmax then b else bmax
      let cmax' := if c > cmax then c else cmax
      spectral_scan p (i + 1) N bmax' cmax' (fuel - 1)
    else
      spectral_scan p (i + 1) N bmax cmax (fuel - 1)
termination_by fuel
```
