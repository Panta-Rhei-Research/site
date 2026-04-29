---
{
  "projection_kind": "taulib_declaration",
  "title": "poly_eval",
  "permalink": "/verify/taulib/docs/book-iii-spectral-hensel-lifting/poly-eval/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Spectral.HenselLifting`.",
  "declaration_id": "TauLib.BookIII.Spectral.HenselLifting::poly_eval",
  "declaration_slug": "poly-eval",
  "kind": "def",
  "name": "poly_eval",
  "module_name": "TauLib.BookIII.Spectral.HenselLifting",
  "module_url": "/verify/taulib/docs/book-iii-spectral-hensel-lifting/",
  "source_line_start": 47,
  "source_line_end": 49,
  "registry_ids": [
    "III.T11"
  ],
  "related_registry_items": [
    {
      "id": "III.T11",
      "title": "Constructive Hensel Lifting",
      "url": "/registry/object/III.T11/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/HenselLifting.lean#L47-L49",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Spectral.HenselLifting",
        "url": "/verify/taulib/docs/book-iii-spectral-hensel-lifting/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/HenselLifting.lean#L47-L49",
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

- Module: [TauLib.BookIII.Spectral.HenselLifting](/verify/taulib/docs/book-iii-spectral-hensel-lifting/)
- Source path: [`TauLib/BookIII/Spectral/HenselLifting.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/HenselLifting.lean#L47-L49)
- Source range: L47-L49
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.T11` — Constructive Hensel Lifting

## Immediate Comment / Docstring

```lean
/-- [III.T11] Evaluate a polynomial f(x) = x² - a mod m.
    This is the canonical test case: lifting square roots. -/
```

## Source Excerpt

```lean
def poly_eval (a x m : TauIdx) : TauIdx :=
  if m == 0 then 0
  else (x * x + m - a % m) % m
```
