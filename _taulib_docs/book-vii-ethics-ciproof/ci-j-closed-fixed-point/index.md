---
{
  "projection_kind": "taulib_declaration",
  "title": "ci_j_closed_fixed_point",
  "permalink": "/verify/taulib/docs/book-vii-ethics-ciproof/ci-j-closed-fixed-point/",
  "summary_short": "`theorem` declaration in `TauLib.BookVII.Ethics.CIProof`.",
  "declaration_id": "TauLib.BookVII.Ethics.CIProof::ci_j_closed_fixed_point",
  "declaration_slug": "ci-j-closed-fixed-point",
  "kind": "theorem",
  "name": "ci_j_closed_fixed_point",
  "module_name": "TauLib.BookVII.Ethics.CIProof",
  "module_url": "/verify/taulib/docs/book-vii-ethics-ciproof/",
  "source_line_start": 370,
  "source_line_end": 375,
  "registry_ids": [
    "VII.T35"
  ],
  "related_registry_items": [
    {
      "id": "VII.T35",
      "title": "CI as j-Closed Fixed Point",
      "url": "/registry/object/VII.T35/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L370-L375",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L370-L375",
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
- Source path: [`TauLib/BookVII/Ethics/CIProof.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L370-L375)
- Source range: L370-L375
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `VII.T35` — CI as j-Closed Fixed Point

## Immediate Comment / Docstring

```lean
/-- [VII.T35] CI as j-Closed Fixed Point (ch88). Three claims:
    (1) Stability: j_dig(CI) = CI
    (2) Component-wise: j_dig(M⁺) = M⁺, j_dig ∘ U = U ∘ j_dig,
        j_dig(γ) = γ, j_dig ∘ R = R ∘ j_dig
    (3) Interpretation: CI already lives in A_dig

    Proof: sheaf condition is label-independent → M⁺ j-closed.
    U commutes with L_dig (universal quantification preserves site).
    γ checks membership in j-closed M⁺. R checks invariance under
    exactly the group defining L_dig. -/
```

## Source Excerpt

```lean
theorem ci_j_closed_fixed_point :
    ci_graph.j_closed = true ∧
    ci_graph.fixed_point = true ∧
    ci_graph.minimal = true ∧
    dignity.lt_modality = true :=
  ⟨rfl, rfl, rfl, rfl⟩
```
