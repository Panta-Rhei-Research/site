---
{
  "projection_kind": "taulib_declaration",
  "title": "CIOperatorGraph",
  "permalink": "/corpus/taulib/docs/book-vii-ethics-ciproof/cioperator-graph/",
  "summary_short": "`structure` declaration in `TauLib.BookVII.Ethics.CIProof`.",
  "declaration_id": "TauLib.BookVII.Ethics.CIProof::CIOperatorGraph",
  "declaration_slug": "cioperator-graph",
  "kind": "structure",
  "name": "CIOperatorGraph",
  "module_name": "TauLib.BookVII.Ethics.CIProof",
  "module_url": "/corpus/taulib/docs/book-vii-ethics-ciproof/",
  "source_line_start": 324,
  "source_line_end": 341,
  "registry_ids": [
    "VII.D71"
  ],
  "related_registry_items": [
    {
      "id": "VII.D71",
      "title": "CI Operator Graph",
      "url": "/registry/object/VII.D71/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L324-L341",
  "formal_status": "defined",
  "declaration_role": "type/data schema",
  "formal_status_label": "type/data schema",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVII.Ethics.CIProof",
        "url": "/corpus/taulib/docs/book-vii-ethics-ciproof/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L324-L341",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
      "role": "type/data schema",
      "status": "type/data schema"
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

- Module: [TauLib.BookVII.Ethics.CIProof](/corpus/taulib/docs/book-vii-ethics-ciproof/)
- Source path: [`TauLib/BookVII/Ethics/CIProof.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L324-L341)
- Source range: L324-L341
- Kind: `structure`
- Public role: `type/data schema`
- Formal status hint: `type/data schema`

## Registry Links

- `VII.D71` — CI Operator Graph

## Immediate Comment / Docstring

```lean
/-- [VII.D71] CI Operator Graph (ch88). Quadruple CI = (M, U, γ, R):
    M: maxim presheaf (typed pairs (α, φ) of action-type + context predicate)
    U: universalization endofunctor (extends context to all perspectives)
    γ: coherence test (sheaf condition check)
    R: respect operator (naturality under address permutations)

    Four components capture Kant's four formulations:
    Universal Law (U), Law of Nature (γ), Humanity (R), Autonomy (M + site). -/
```

## Source Excerpt

```lean
structure CIOperatorGraph where
  /-- M: maxim presheaf in Ĉ. -/
  has_maxim_space : Bool := true
  /-- U: universalization endofunctor. -/
  has_universalization : Bool := true
  /-- γ: coherence test (sheaf condition). -/
  has_coherence_test : Bool := true
  /-- R: respect operator (label-invariance). -/
  has_respect_operator : Bool := true
  /-- Component count = 4 (matching four Kantian formulations). -/
  component_count : Nat := 4
  /-- j_dig-closed: j_dig(CI) = CI. -/
  j_closed : Bool := true
  /-- Fixed point: CI = j(CI). -/
  fixed_point : Bool := true
  /-- Minimal: no proper j-closed sub-principle. -/
  minimal : Bool := true
  deriving Repr
```
