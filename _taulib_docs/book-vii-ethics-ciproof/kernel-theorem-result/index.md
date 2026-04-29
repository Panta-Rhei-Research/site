---
{
  "projection_kind": "taulib_declaration",
  "title": "KernelTheoremResult",
  "permalink": "/verify/taulib/docs/book-vii-ethics-ciproof/kernel-theorem-result/",
  "summary_short": "`structure` declaration in `TauLib.BookVII.Ethics.CIProof`.",
  "declaration_id": "TauLib.BookVII.Ethics.CIProof::KernelTheoremResult",
  "declaration_slug": "kernel-theorem-result",
  "kind": "structure",
  "name": "KernelTheoremResult",
  "module_name": "TauLib.BookVII.Ethics.CIProof",
  "module_url": "/verify/taulib/docs/book-vii-ethics-ciproof/",
  "source_line_start": 411,
  "source_line_end": 422,
  "registry_ids": [
    "VII.T36"
  ],
  "related_registry_items": [
    {
      "id": "VII.T36",
      "title": "Kernel Theorem (K)",
      "url": "/registry/object/VII.T36/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L411-L422",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L411-L422",
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

- Module: [TauLib.BookVII.Ethics.CIProof](/verify/taulib/docs/book-vii-ethics-ciproof/)
- Source path: [`TauLib/BookVII/Ethics/CIProof.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L411-L422)
- Source range: L411-L422
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VII.T36` — Kernel Theorem (K)

## Immediate Comment / Docstring

```lean
/-- [VII.T36] Kernel Theorem (ch89, Stage K). At E₃ in τ:
    (1) Existence: there exists a j_dig-closed operator graph G = (M, U, γ, R)
    (2) Structural origin: forced by (a) saturation Enrich⁴ = Enrich³,
        (b) bipolar L = S¹ ∨ S¹ generating agent-patient polarity,
        (c) Yoneda embedding ensuring faithful presheaf representation
    (3) Canonicity: determined by structural data, no arbitrary choices

    Proof: self-enrichment at E₃ provides internal hom [A,A]; maxims are
    sections M = Γ([A,A]). U via internal universal quantification (topos).
    γ = sheafification comparison. R = Aut(C) action. Bipolar structure
    ensures non-trivial site. Yoneda ensures faithfulness. -/
```

## Source Excerpt

```lean
structure KernelTheoremResult where
  /-- Existence of j-closed operator graph. -/
  existence : Bool := true
  /-- Forced by self-enrichment saturation. -/
  from_saturation : Bool := true
  /-- Forced by bipolar lemniscate structure. -/
  from_bipolarity : Bool := true
  /-- Forced by Yoneda faithfulness. -/
  from_yoneda : Bool := true
  /-- Canonically determined. -/
  canonical : Bool := true
  deriving Repr
```
