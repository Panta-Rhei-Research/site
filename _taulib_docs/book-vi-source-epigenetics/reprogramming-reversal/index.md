---
{
  "projection_kind": "taulib_declaration",
  "title": "ReprogrammingReversal",
  "permalink": "/verify/taulib/docs/book-vi-source-epigenetics/reprogramming-reversal/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Source.Epigenetics`.",
  "declaration_id": "TauLib.BookVI.Source.Epigenetics::ReprogrammingReversal",
  "declaration_slug": "reprogramming-reversal",
  "kind": "structure",
  "name": "ReprogrammingReversal",
  "module_name": "TauLib.BookVI.Source.Epigenetics",
  "module_url": "/verify/taulib/docs/book-vi-source-epigenetics/",
  "source_line_start": 276,
  "source_line_end": 285,
  "registry_ids": [
    "VI.T48"
  ],
  "related_registry_items": [
    {
      "id": "VI.T48",
      "title": "Reprogramming as Refinement Reversal",
      "url": "/registry/object/VI.T48/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Source/Epigenetics.lean#L276-L285",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.Source.Epigenetics",
        "url": "/verify/taulib/docs/book-vi-source-epigenetics/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Source/Epigenetics.lean#L276-L285",
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

- Module: [TauLib.BookVI.Source.Epigenetics](/verify/taulib/docs/book-vi-source-epigenetics/)
- Source path: [`TauLib/BookVI/Source/Epigenetics.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Source/Epigenetics.lean#L276-L285)
- Source range: L276-L285
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.T48` — Reprogramming as Refinement Reversal

## Immediate Comment / Docstring

```lean
/-- [VI.T48] Reprogramming as Refinement Reversal.
    The ω-germ code is unchanged throughout differentiation (VI.P18, item iv),
    so chromatin restriction is reversible in principle.
    Yamanaka factors (Oct4, Sox2, Klf4, c-Myc) demonstrate constructive
    reversal: C_k → C_{k-1} → ··· → C_1.
    Scope: τ-effective. -/
```

## Source Excerpt

```lean
structure ReprogrammingReversal where
  /-- Code is invariant (ω-germ unchanged). -/
  code_invariant : Bool := true
  /-- Reversal demonstrated by Yamanaka factors (2006). -/
  yamanaka_demonstrated : Bool := true
  /-- Number of Yamanaka factors. -/
  factor_count : Nat := 4
  /-- Scope: τ-effective. -/
  scope : String := "tau-effective"
  deriving Repr
```
