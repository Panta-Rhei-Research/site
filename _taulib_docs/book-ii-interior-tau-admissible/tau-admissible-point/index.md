---
{
  "projection_kind": "taulib_declaration",
  "title": "TauAdmissiblePoint",
  "permalink": "/verify/taulib/docs/book-ii-interior-tau-admissible/tau-admissible-point/",
  "summary_short": "`structure` declaration in `TauLib.BookII.Interior.TauAdmissible`.",
  "declaration_id": "TauLib.BookII.Interior.TauAdmissible::TauAdmissiblePoint",
  "declaration_slug": "tau-admissible-point",
  "kind": "structure",
  "name": "TauAdmissiblePoint",
  "module_name": "TauLib.BookII.Interior.TauAdmissible",
  "module_url": "/verify/taulib/docs/book-ii-interior-tau-admissible/",
  "source_line_start": 86,
  "source_line_end": 91,
  "registry_ids": [
    "II.D02"
  ],
  "related_registry_items": [
    {
      "id": "II.D02",
      "title": "Tau-Admissible Point",
      "url": "/registry/object/II.D02/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Interior/TauAdmissible.lean#L86-L91",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Interior.TauAdmissible",
        "url": "/verify/taulib/docs/book-ii-interior-tau-admissible/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Interior/TauAdmissible.lean#L86-L91",
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

- Module: [TauLib.BookII.Interior.TauAdmissible](/verify/taulib/docs/book-ii-interior-tau-admissible/)
- Source path: [`TauLib/BookII/Interior/TauAdmissible.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Interior/TauAdmissible.lean#L86-L91)
- Source range: L86-L91
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `II.D02` — Tau-Admissible Point

## Immediate Comment / Docstring

```lean
/-- [II.D02] A τ-admissible point: ABCD quadruple from the greedy peel
    decomposition. Every object X ∈ Obj(τ) has a unique such representation
    via the Hyperfactorization Theorem (I.T04). -/
```

## Source Excerpt

```lean
structure TauAdmissiblePoint where
  a : TauIdx  -- A: prime direction (π-channel)
  b : TauIdx  -- B: exponent (γ-channel)
  c : TauIdx  -- C: tetration height (η-channel)
  d : TauIdx  -- D: remainder (α-channel)
  deriving Repr, DecidableEq
```
