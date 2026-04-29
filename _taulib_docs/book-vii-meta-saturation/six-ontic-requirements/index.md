---
{
  "projection_kind": "taulib_declaration",
  "title": "SixOnticRequirements",
  "permalink": "/verify/taulib/docs/book-vii-meta-saturation/six-ontic-requirements/",
  "summary_short": "`structure` declaration in `TauLib.BookVII.Meta.Saturation`.",
  "declaration_id": "TauLib.BookVII.Meta.Saturation::SixOnticRequirements",
  "declaration_slug": "six-ontic-requirements",
  "kind": "structure",
  "name": "SixOnticRequirements",
  "module_name": "TauLib.BookVII.Meta.Saturation",
  "module_url": "/verify/taulib/docs/book-vii-meta-saturation/",
  "source_line_start": 465,
  "source_line_end": 482,
  "registry_ids": [
    "VII.D37"
  ],
  "related_registry_items": [
    {
      "id": "VII.D37",
      "title": "Six Ontic Requirements",
      "url": "/registry/object/VII.D37/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Saturation.lean#L465-L482",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Saturation.lean#L465-L482",
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
- Source path: [`TauLib/BookVII/Meta/Saturation.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Saturation.lean#L465-L482)
- Source range: L465-L482
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VII.D37` — Six Ontic Requirements

## Immediate Comment / Docstring

```lean
/-- [VII.D37] Six Ontic Requirements (ch29). A candidate foundation F must satisfy:
    (OR1) Yoneda: identity-faithful representation (eliminates haecceity)
    (OR2) Finite signature: finitely generated (surveyable by finite being)
    (OR3) Diagonal-free: self-description without diagonal paradoxes (NF-addresses)
    (OR4) NF-addressable: unique normal-form addresses (findability, decidable identity)
    (OR5) Holomorphic: local data determine global structure (Central Theorem)
    (OR6) Spectral completeness: internal spectral decomposition (eight forces)

    SCOPE UPGRADE: conjectural → τ-effective (Sprint R8-B4).
    Upgraded via constraint-entailment: six constraints collectively force
    τ's axiom structure (K0–K6 + 5 generators), verified by pairwise narrowing. -/
```

## Source Excerpt

```lean
structure SixOnticRequirements where
  /-- (OR1) Yoneda: identity-faithful representation. -/
  or1_yoneda : Bool := true
  /-- (OR2) Finite signature: finitely generated. -/
  or2_finite : Bool := true
  /-- (OR3) Diagonal-free: NF-addresses, no paradoxes. -/
  or3_diagonal_free : Bool := true
  /-- (OR4) NF-addressable: unique normal-form addresses. -/
  or4_nf_addressable : Bool := true
  /-- (OR5) Holomorphic: local ⟹ global (Central Theorem). -/
  or5_holomorphic : Bool := true
  /-- (OR6) Spectral: internal spectral decomposition. -/
  or6_spectral : Bool := true
  /-- All six requirements satisfied by τ. -/
  requirement_count : Nat := 6
  /-- τ satisfies all six. -/
  tau_satisfies_all : Bool := true
  deriving Repr
```
