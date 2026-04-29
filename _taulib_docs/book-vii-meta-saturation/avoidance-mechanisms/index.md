---
{
  "projection_kind": "taulib_declaration",
  "title": "AvoidanceMechanisms",
  "permalink": "/verify/taulib/docs/book-vii-meta-saturation/avoidance-mechanisms/",
  "summary_short": "`structure` declaration in `TauLib.BookVII.Meta.Saturation`.",
  "declaration_id": "TauLib.BookVII.Meta.Saturation::AvoidanceMechanisms",
  "declaration_slug": "avoidance-mechanisms",
  "kind": "structure",
  "name": "AvoidanceMechanisms",
  "module_name": "TauLib.BookVII.Meta.Saturation",
  "module_url": "/verify/taulib/docs/book-vii-meta-saturation/",
  "source_line_start": 403,
  "source_line_end": 410,
  "registry_ids": [
    "VII.P04"
  ],
  "related_registry_items": [
    {
      "id": "VII.P04",
      "title": "No-Diagonal Principle",
      "url": "/registry/object/VII.P04/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Saturation.lean#L403-L410",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Saturation.lean#L403-L410",
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
- Source path: [`TauLib/BookVII/Meta/Saturation.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Saturation.lean#L403-L410)
- Source range: L403-L410
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VII.P04` — No-Diagonal Principle

## Immediate Comment / Docstring

```lean
/-- [VII.P04] No-Diagonal: no surjection d : Ob(τ³) → Sub_j([τ^op, τ]).
    Anti-diagonal A = {x | x ∉ d(x)} is not j-closed due to monodromy
    constraint at crossing point p₀.

    Five avoidance mechanisms:
    1. No-Contraction: SelfDesc³ = SelfDesc² prevents unbounded nesting
    2. No-Diagonal: lemniscate crossing prevents surjective diagonal
    3. BWF: excludes unbounded quantification
    4. NF-Linearity: prevents circular reference chains
    5. Generation vs. Presentation: coherence is functorial, not syntactic -/
```

## Source Excerpt

```lean
structure AvoidanceMechanisms where
  no_contraction : Bool := true
  no_diagonal : Bool := true
  bounded_witness : Bool := true
  nf_linearity : Bool := true
  generation_not_presentation : Bool := true
  mechanism_count : Nat := 5
  deriving Repr
```
