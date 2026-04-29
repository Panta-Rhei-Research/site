---
{
  "projection_kind": "taulib_declaration",
  "title": "inOrbitRay",
  "permalink": "/verify/taulib/docs/book-i-kernel-axioms/in-orbit-ray/",
  "summary_short": "`def` declaration in `TauLib.BookI.Kernel.Axioms`.",
  "declaration_id": "TauLib.BookI.Kernel.Axioms::inOrbitRay",
  "declaration_slug": "in-orbit-ray",
  "kind": "def",
  "name": "inOrbitRay",
  "module_name": "TauLib.BookI.Kernel.Axioms",
  "module_url": "/verify/taulib/docs/book-i-kernel-axioms/",
  "source_line_start": 93,
  "source_line_end": 94,
  "registry_ids": [
    "I.K3"
  ],
  "related_registry_items": [
    {
      "id": "I.K3",
      "title": "Orbit-Seeded Generation (K3)",
      "url": "/registry/object/I.K3/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Kernel/Axioms.lean#L93-L94",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Kernel/Axioms.lean#L93-L94",
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
- Source path: [`TauLib/BookI/Kernel/Axioms.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Kernel/Axioms.lean#L93-L94)
- Source range: L93-L94
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `I.K3` — Orbit-Seeded Generation (K3)

## Immediate Comment / Docstring

```lean
/-- [I.K3] **Orbit-Seeded Generation**: Each non-omega generator g seeds
    its orbit ray O_g = {ρⁿ(g) : n ≥ 0}.

    We define the orbit ray predicate. -/
```

## Source Excerpt

```lean
def inOrbitRay (g : Generator) (x : TauObj) : Prop :=
  x.seed = g ∧ g ≠ omega
```
