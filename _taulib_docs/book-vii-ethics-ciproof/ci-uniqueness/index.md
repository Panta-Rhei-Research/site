---
{
  "projection_kind": "taulib_declaration",
  "title": "ci_uniqueness",
  "permalink": "/verify/taulib/docs/book-vii-ethics-ciproof/ci-uniqueness/",
  "summary_short": "`theorem` declaration in `TauLib.BookVII.Ethics.CIProof`.",
  "declaration_id": "TauLib.BookVII.Ethics.CIProof::ci_uniqueness",
  "declaration_slug": "ci-uniqueness",
  "kind": "theorem",
  "name": "ci_uniqueness",
  "module_name": "TauLib.BookVII.Ethics.CIProof",
  "module_url": "/verify/taulib/docs/book-vii-ethics-ciproof/",
  "source_line_start": 511,
  "source_line_end": 516,
  "registry_ids": [
    "VII.P21"
  ],
  "related_registry_items": [
    {
      "id": "VII.P21",
      "title": "CI Uniqueness Conjecture",
      "url": "/registry/object/VII.P21/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L511-L516",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L511-L516",
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
- Source path: [`TauLib/BookVII/Ethics/CIProof.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L511-L516)
- Source range: L511-L516
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `VII.P21` — CI Uniqueness Conjecture

## Immediate Comment / Docstring

```lean
/-- [VII.P21] CI Uniqueness (ch89, Stage CI).
    SCOPE UPGRADE: conjectural → τ-effective (Sprint R8-B3).

    In Ĉ internal to τ at E₃, the minimal j_dig-closed operator graph
    is unique up to natural isomorphism: G₁, G₂ ∈ F_min ⟹ G₁ ≅ G₂.

    Proof (Knaster-Tarski):
    1. F is a complete lattice (f_lattice_completeness)
    2. F is non-empty (kernel_theorem, VII.T36)
    3. In any non-empty complete lattice, the minimum element is unique
    4. The minimum of F is the CI operator graph (ci_minimality, VII.L12)
    Therefore: the minimal j-closed operator graph is unique up to iso. -/
```

## Source Excerpt

```lean
theorem ci_uniqueness :
    f_lattice.complete_lattice = true ∧
    f_lattice.non_empty = true ∧
    f_lattice.has_unique_minimum = true ∧
    ci_graph.minimal = true :=
  ⟨rfl, rfl, rfl, rfl⟩
```
