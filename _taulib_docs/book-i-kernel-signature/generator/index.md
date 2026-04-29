---
{
  "projection_kind": "taulib_declaration",
  "title": "Generator",
  "permalink": "/verify/taulib/docs/book-i-kernel-signature/generator/",
  "summary_short": "`inductive` declaration in `TauLib.BookI.Kernel.Signature`.",
  "declaration_id": "TauLib.BookI.Kernel.Signature::Generator",
  "declaration_slug": "generator",
  "kind": "inductive",
  "name": "Generator",
  "module_name": "TauLib.BookI.Kernel.Signature",
  "module_url": "/verify/taulib/docs/book-i-kernel-signature/",
  "source_line_start": 67,
  "source_line_end": 75,
  "registry_ids": [
    "I.D01"
  ],
  "related_registry_items": [
    {
      "id": "I.D01",
      "title": "Five Generators",
      "url": "/registry/object/I.D01/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Kernel/Signature.lean#L67-L75",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Kernel.Signature",
        "url": "/verify/taulib/docs/book-i-kernel-signature/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Kernel/Signature.lean#L67-L75",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "inductive",
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

- Module: [TauLib.BookI.Kernel.Signature](/verify/taulib/docs/book-i-kernel-signature/)
- Source path: [`TauLib/BookI/Kernel/Signature.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Kernel/Signature.lean#L67-L75)
- Source range: L67-L75
- Kind: `inductive`
- Formal status hint: `defined`

## Registry Links

- `I.D01` — Five Generators

## Immediate Comment / Docstring

```lean
/-- [I.D01] The five generators of Category τ.
    These are the ONLY primitive objects. All other objects are orbit elements
    produced by applying ρ to these generators. -/
```

## Source Excerpt

```lean
inductive Generator : Type where
  | alpha : Generator  -- α: radial seed
  | pi    : Generator  -- π: prime base
  | gamma : Generator  -- γ: exponent channel (1st Ed: π')
  | eta   : Generator  -- η: tetration channel (1st Ed: π'')
  | omega : Generator  -- ω: fixed-point absorber
  deriving DecidableEq, Repr

open Generator
```
