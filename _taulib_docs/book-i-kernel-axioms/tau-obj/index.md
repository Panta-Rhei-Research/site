---
{
  "projection_kind": "taulib_declaration",
  "title": "TauObj",
  "permalink": "/verify/taulib/docs/book-i-kernel-axioms/tau-obj/",
  "summary_short": "`structure` declaration in `TauLib.BookI.Kernel.Axioms`.",
  "declaration_id": "TauLib.BookI.Kernel.Axioms::TauObj",
  "declaration_slug": "tau-obj",
  "kind": "structure",
  "name": "TauObj",
  "module_name": "TauLib.BookI.Kernel.Axioms",
  "module_url": "/verify/taulib/docs/book-i-kernel-axioms/",
  "source_line_start": 49,
  "source_line_end": 54,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Kernel/Axioms.lean#L49-L54",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Kernel/Axioms.lean#L49-L54",
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

- Module: [TauLib.BookI.Kernel.Axioms](/verify/taulib/docs/book-i-kernel-axioms/)
- Source path: [`TauLib/BookI/Kernel/Axioms.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Kernel/Axioms.lean#L49-L54)
- Source range: L49-L54
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Objects of Category τ: either a generator or an orbit element ρⁿ(g).
    This is the type AFTER the generative act (Part II).

    An object is represented by its seed generator and the number of ρ-applications.
    The generator ω with n=0 is the beacon; ω with n>0 collapses to ω (K2).

    **Depth convention**: depth 0 = the generator itself (no ρ applied).
    Orbit elements start at depth 1: α_1 = ⟨α, 1⟩ = ρ(α).
    The generator α = ⟨α, 0⟩ is the seed, NOT an orbit element "α_0".

    NOTE: This representation makes K6 (object closure) definitional rather than axiomatic:
    every TauObj is by construction in some orbit ray or is ω. -/
```

## Source Excerpt

```lean
structure TauObj where
  /-- The seed generator of this object's orbit ray -/
  seed : Generator
  /-- Number of ρ-applications (0 = the generator itself, ≥1 = orbit element) -/
  depth : Nat
  deriving DecidableEq, Repr
```
