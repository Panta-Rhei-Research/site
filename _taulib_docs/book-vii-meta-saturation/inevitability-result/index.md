---
{
  "projection_kind": "taulib_declaration",
  "title": "InevitabilityResult",
  "permalink": "/verify/taulib/docs/book-vii-meta-saturation/inevitability-result/",
  "summary_short": "`structure` declaration in `TauLib.BookVII.Meta.Saturation`.",
  "declaration_id": "TauLib.BookVII.Meta.Saturation::InevitabilityResult",
  "declaration_slug": "inevitability-result",
  "kind": "structure",
  "name": "InevitabilityResult",
  "module_name": "TauLib.BookVII.Meta.Saturation",
  "module_url": "/verify/taulib/docs/book-vii-meta-saturation/",
  "source_line_start": 531,
  "source_line_end": 548,
  "registry_ids": [
    "VII.T14"
  ],
  "related_registry_items": [
    {
      "id": "VII.T14",
      "title": "Inevitability Convergence",
      "url": "/registry/object/VII.T14/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Saturation.lean#L531-L548",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVII.Meta.Saturation",
        "url": "/verify/taulib/docs/book-vii-meta-saturation/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Saturation.lean#L531-L548",
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

- Module: [TauLib.BookVII.Meta.Saturation](/verify/taulib/docs/book-vii-meta-saturation/)
- Source path: [`TauLib/BookVII/Meta/Saturation.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Saturation.lean#L531-L548)
- Source range: L531-L548
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VII.T14` — Inevitability Convergence

## Immediate Comment / Docstring

```lean
/-- [VII.T14] Inevitability Convergence (ch29).
    SCOPE UPGRADE: conjectural → τ-effective (Sprint R8-B4).

    The six ontic requirements collectively entail τ's axiom structure.
    Constraint-entailment proof (not global uniqueness):
    1. (OR1)+(OR2) → finitely generated + Yoneda → axiom candidates
    2. (OR3)+(OR4) → NF-address structure → K0–K4
    3. (OR5)+(OR6) → holomorphic-spectral bridge → K5–K6 + Central Theorem
    Composition: OR1–OR6 → K0–K6 ∧ 5 generators ∧ τ³ fibration

    Upgraded from global uniqueness (undecidable) to constraint-entailment:
    the requirements force the axiom structure, which determines τ. -/
```

## Source Excerpt

```lean
structure InevitabilityResult where
  /-- Six requirements all satisfied. -/
  all_requirements : SixOnticRequirements := six_requirements
  /-- Pairwise narrowing succeeds (3 pairs). -/
  pairwise_narrowing : Bool := true
  /-- Entails K0–K4 (combinatorial axioms). -/
  entails_k0_k4 : Bool := true
  /-- Entails K5–K6 (analytic axioms). -/
  entails_k5_k8 : Bool := true
  /-- Entails 5 generators. -/
  entails_generators : Bool := true
  /-- Entails τ³ fibration. -/
  entails_fibration : Bool := true
  /-- Axiom count: 7 (K0–K6). -/
  axiom_count : Nat := 9
  /-- Generator count: 5. -/
  generator_count : Nat := 5
  deriving Repr
```
