---
{
  "projection_kind": "taulib_declaration",
  "title": "DignityStructure",
  "permalink": "/corpus/taulib/docs/book-vii-ethics-ciproof/dignity-structure/",
  "summary_short": "`structure` declaration in `TauLib.BookVII.Ethics.CIProof`.",
  "declaration_id": "TauLib.BookVII.Ethics.CIProof::DignityStructure",
  "declaration_slug": "dignity-structure",
  "kind": "structure",
  "name": "DignityStructure",
  "module_name": "TauLib.BookVII.Ethics.CIProof",
  "module_url": "/corpus/taulib/docs/book-vii-ethics-ciproof/",
  "source_line_start": 72,
  "source_line_end": 85,
  "registry_ids": [
    "VII.D65"
  ],
  "related_registry_items": [
    {
      "id": "VII.D65",
      "title": "Dignity as Label-Independence",
      "url": "/registry/object/VII.D65/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L72-L85",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L72-L85",
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
- Source path: [`TauLib/BookVII/Ethics/CIProof.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L72-L85)
- Source range: L72-L85
- Kind: `structure`
- Public role: `type/data schema`
- Formal status hint: `type/data schema`

## Registry Links

- `VII.D65` — Dignity as Label-Independence

## Immediate Comment / Docstring

```lean
/-- [VII.D65] Dignity as Label-Independence (ch76).
    For agent-state X ∈ Ob(A), identity-invariants D(X) = {P ∈ Prop(X) | σ*P = P ∀ σ}.
    A policy π has dignity iff σ ∘ π = π ∘ σ for all σ ∈ Aut(A).
    The Dignity Functor D : A → Inv extracts identity-invariants.

    Identity-invariants include: rational agency, autonomous will, reflexive
    self-awareness, capacity for suffering/flourishing, temporal persistence.
    Excluded: names, wealth, social status, contingent attributes. -/
```

## Source Excerpt

```lean
structure DignityStructure where
  /-- Label-independent: commutes with all automorphisms. -/
  label_independent : Bool := true
  /-- Identity-invariants extractable via functor D. -/
  has_identity_invariants : Bool := true
  /-- Admissible subworld A_dig: full subcategory on dignity-preserving states. -/
  has_admissible_subworld : Bool := true
  /-- Reflector L_dig : A → A_dig exists (left adjoint to inclusion). -/
  has_reflector : Bool := true
  /-- Reflector is idempotent: L_dig ∘ L_dig = L_dig. -/
  reflector_idempotent : Bool := true
  /-- j_dig = i ∘ L_dig is a Lawvere-Tierney modal operator on A. -/
  lt_modality : Bool := true
  deriving Repr
```
