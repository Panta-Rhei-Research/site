---
{
  "projection_kind": "taulib_declaration",
  "title": "restriction",
  "permalink": "/verify/taulib/docs/book-i-holomorphy-spectral-coefficients/restriction/",
  "summary_short": "`def` declaration in `TauLib.BookI.Holomorphy.SpectralCoefficients`.",
  "declaration_id": "TauLib.BookI.Holomorphy.SpectralCoefficients::restriction",
  "declaration_slug": "restriction",
  "kind": "def",
  "name": "restriction",
  "module_name": "TauLib.BookI.Holomorphy.SpectralCoefficients",
  "module_url": "/verify/taulib/docs/book-i-holomorphy-spectral-coefficients/",
  "source_line_start": 64,
  "source_line_end": 66,
  "registry_ids": [
    "I.D66"
  ],
  "related_registry_items": [
    {
      "id": "I.D66",
      "title": "Restriction Map",
      "url": "/registry/object/I.D66/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/SpectralCoefficients.lean#L64-L66",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Holomorphy.SpectralCoefficients",
        "url": "/verify/taulib/docs/book-i-holomorphy-spectral-coefficients/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/SpectralCoefficients.lean#L64-L66",
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

- Module: [TauLib.BookI.Holomorphy.SpectralCoefficients](/verify/taulib/docs/book-i-holomorphy-spectral-coefficients/)
- Source path: [`TauLib/BookI/Holomorphy/SpectralCoefficients.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/SpectralCoefficients.lean#L64-L66)
- Source range: L64-L66
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `I.D66` — Restriction Map

## Immediate Comment / Docstring

```lean
/-- [I.D66] The restriction map: restrict a StageFun to inputs
    NOT in a given subset K (modeled as a predicate).
    Returns 0 for inputs in K (the "deleted" set). -/
```

## Source Excerpt

```lean
def restriction (f : StageFun) (inK : TauIdx → Bool) : StageFun :=
  { b_fun := fun n k => if inK n then 0 else f.b_fun n k
    c_fun := fun n k => if inK n then 0 else f.c_fun n k }
```
