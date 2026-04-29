---
{
  "projection_kind": "taulib_declaration",
  "title": "no_conflict",
  "permalink": "/verify/taulib/docs/book-vii-ethics-ciproof/no-conflict/",
  "summary_short": "`theorem` declaration in `TauLib.BookVII.Ethics.CIProof`.",
  "declaration_id": "TauLib.BookVII.Ethics.CIProof::no_conflict",
  "declaration_slug": "no-conflict",
  "kind": "theorem",
  "name": "no_conflict",
  "module_name": "TauLib.BookVII.Ethics.CIProof",
  "module_url": "/verify/taulib/docs/book-vii-ethics-ciproof/",
  "source_line_start": 220,
  "source_line_end": 224,
  "registry_ids": [
    "VII.T32"
  ],
  "related_registry_items": [
    {
      "id": "VII.T32",
      "title": "No-Conflict Theorem",
      "url": "/registry/object/VII.T32/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L220-L224",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVII.Ethics.CIProof",
        "url": "/verify/taulib/docs/book-vii-ethics-ciproof/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L220-L224",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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

- Module: [TauLib.BookVII.Ethics.CIProof](/verify/taulib/docs/book-vii-ethics-ciproof/)
- Source path: [`TauLib/BookVII/Ethics/CIProof.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L220-L224)
- Source range: L220-L224
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `VII.T32` — No-Conflict Theorem

## Immediate Comment / Docstring

```lean
/-- [VII.T32] No-Conflict Theorem (ch78). For properly typed D₁, D₂:
    (1) Joint realizability: D₁(U) ∩ D₂(U) ≠ ∅ for every U
    (2) Global compatibility: joint fibers glue to global section
    (3) No dignity sacrifice: global section factors through L_dig

    Proof: intersection of subsheaves pointwise. Proper typing (VII.L11)
    gives nonempty fibers + dignity preservation. Sheaf axiom gives gluing.
    τ-holomorphy extends local joint enactments globally. -/
```

## Source Excerpt

```lean
theorem no_conflict :
    canonical_duty.is_subsheaf = true ∧
    canonical_duty.dignity_preserving = true ∧
    ci_naturality.separated = true :=
  ⟨rfl, rfl, rfl⟩
```
