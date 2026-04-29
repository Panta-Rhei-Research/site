---
{
  "projection_kind": "taulib_declaration",
  "title": "AFFromNcNf",
  "permalink": "/verify/taulib/docs/book-iv-strong-quarks-gluons/affrom-nc-nf/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Strong.QuarksGluons`.",
  "declaration_id": "TauLib.BookIV.Strong.QuarksGluons::AFFromNcNf",
  "declaration_slug": "affrom-nc-nf",
  "kind": "structure",
  "name": "AFFromNcNf",
  "module_name": "TauLib.BookIV.Strong.QuarksGluons",
  "module_url": "/verify/taulib/docs/book-iv-strong-quarks-gluons/",
  "source_line_start": 278,
  "source_line_end": 287,
  "registry_ids": [
    "IV.P118"
  ],
  "related_registry_items": [
    {
      "id": "IV.P118",
      "title": "Asymptotic freedom from N_c and N_f",
      "url": "/registry/object/IV.P118/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/QuarksGluons.lean#L278-L287",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Strong.QuarksGluons",
        "url": "/verify/taulib/docs/book-iv-strong-quarks-gluons/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/QuarksGluons.lean#L278-L287",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
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

- Module: [TauLib.BookIV.Strong.QuarksGluons](/verify/taulib/docs/book-iv-strong-quarks-gluons/)
- Source path: [`TauLib/BookIV/Strong/QuarksGluons.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/QuarksGluons.lean#L278-L287)
- Source range: L278-L287
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P118` — Asymptotic freedom from N_c and N_f

## Immediate Comment / Docstring

```lean
/-- [IV.P118] N_c = 3 and N_f = 6 satisfy the asymptotic freedom
    condition: N_f < 11*N_c/2 = 16.5.
    6 < 16.5: true. (Or equivalently, 2*N_f < 11*N_c: 12 < 33.) -/
```

## Source Excerpt

```lean
structure AFFromNcNf where
  /-- N_c = 3. -/
  nc : Nat := 3
  /-- N_f = 6 (u,d,c,s,t,b). -/
  nf : Nat := 6
  /-- 2*N_f < 11*N_c. -/
  condition_holds : Bool := true
  /-- Both tau and orthodox agree. -/
  agreement : String := "tau spectral tightening and orthodox beta function agree"
  deriving Repr
```
