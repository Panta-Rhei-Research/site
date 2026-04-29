---
{
  "projection_kind": "taulib_declaration",
  "title": "rho",
  "permalink": "/verify/taulib/docs/book-i-kernel-axioms/rho/",
  "summary_short": "`def` declaration in `TauLib.BookI.Kernel.Axioms`.",
  "declaration_id": "TauLib.BookI.Kernel.Axioms::rho",
  "declaration_slug": "rho",
  "kind": "def",
  "name": "rho",
  "module_name": "TauLib.BookI.Kernel.Axioms",
  "module_url": "/verify/taulib/docs/book-i-kernel-axioms/",
  "source_line_start": 61,
  "source_line_end": 64,
  "registry_ids": [
    "I.D02"
  ],
  "related_registry_items": [
    {
      "id": "I.D02",
      "title": "Progression Operator rho",
      "url": "/registry/object/I.D02/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Kernel/Axioms.lean#L61-L64",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Kernel.Axioms",
        "url": "/verify/taulib/docs/book-i-kernel-axioms/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Kernel/Axioms.lean#L61-L64",
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

- Module: [TauLib.BookI.Kernel.Axioms](/verify/taulib/docs/book-i-kernel-axioms/)
- Source path: [`TauLib/BookI/Kernel/Axioms.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Kernel/Axioms.lean#L61-L64)
- Source range: L61-L64
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `I.D02` — Progression Operator rho

## Immediate Comment / Docstring

```lean
/-- [I.D02] The progression operator ρ: sole primitive iterator.
    ρ(ω) = ω (K2 omega fixed point); otherwise increments depth. -/
```

## Source Excerpt

```lean
def rho (x : TauObj) : TauObj :=
  match x.seed with
  | omega => x  -- K2: ω is a fixed point
  | _ => ⟨x.seed, x.depth + 1⟩
```
