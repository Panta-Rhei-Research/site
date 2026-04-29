---
{
  "projection_kind": "taulib_declaration",
  "title": "QuarkMode",
  "permalink": "/verify/taulib/docs/book-iv-strong-quarks-gluons/quark-mode/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Strong.QuarksGluons`.",
  "declaration_id": "TauLib.BookIV.Strong.QuarksGluons::QuarkMode",
  "declaration_slug": "quark-mode",
  "kind": "structure",
  "name": "QuarkMode",
  "module_name": "TauLib.BookIV.Strong.QuarksGluons",
  "module_url": "/verify/taulib/docs/book-iv-strong-quarks-gluons/",
  "source_line_start": 56,
  "source_line_end": 67,
  "registry_ids": [
    "IV.D187"
  ],
  "related_registry_items": [
    {
      "id": "IV.D187",
      "title": "Quark mode",
      "url": "/registry/object/IV.D187/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/QuarksGluons.lean#L56-L67",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/QuarksGluons.lean#L56-L67",
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
- Source path: [`TauLib/BookIV/Strong/QuarksGluons.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/QuarksGluons.lean#L56-L67)
- Source range: L56-L67
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D187` — Quark mode

## Immediate Comment / Docstring

```lean
/-- [IV.D187] A quark mode: character mode chi_{m,n} on T^2 with
    n not equiv 0 mod 3, carrying color class c = n mod 3.
    Cannot exist as isolated state by the Confinement Theorem. -/
```

## Source Excerpt

```lean
structure QuarkMode where
  /-- Gamma-winding (EM component). -/
  gamma_winding : Int
  /-- Eta-winding (strong component, not divisible by 3). -/
  eta_winding : Int
  /-- Quark type derived from eta_winding mod 3. -/
  quark_type : QuarkType
  /-- Generation (1, 2, or 3). -/
  generation : Nat
  /-- Generation is valid. -/
  gen_valid : generation >= 1 ∧ generation <= 3
  deriving Repr
```
