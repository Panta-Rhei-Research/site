---
{
  "projection_kind": "taulib_declaration",
  "title": "ci_minimality",
  "permalink": "/verify/taulib/docs/book-vii-ethics-ciproof/ci-minimality/",
  "summary_short": "`theorem` declaration in `TauLib.BookVII.Ethics.CIProof`.",
  "declaration_id": "TauLib.BookVII.Ethics.CIProof::ci_minimality",
  "declaration_slug": "ci-minimality",
  "kind": "theorem",
  "name": "ci_minimality",
  "module_name": "TauLib.BookVII.Ethics.CIProof",
  "module_url": "/verify/taulib/docs/book-vii-ethics-ciproof/",
  "source_line_start": 390,
  "source_line_end": 394,
  "registry_ids": [
    "VII.L12"
  ],
  "related_registry_items": [
    {
      "id": "VII.L12",
      "title": "CI Minimality Lemma",
      "url": "/registry/object/VII.L12/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L390-L394",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L390-L394",
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
- Source path: [`TauLib/BookVII/Ethics/CIProof.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L390-L394)
- Source range: L390-L394
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `VII.L12` — CI Minimality Lemma

## Immediate Comment / Docstring

```lean
/-- [VII.L12] CI Minimality (ch88). In the poset F of j_dig-closed operator
    graphs, ordered by inclusion:
    (1) Lower bound: CI is the minimum (CI-admissible ⊆ any G ∈ F)
    (2) Necessity: any G' strictly weaker is not j-closed
    (3) Redundancy: any G'' strictly stronger has CI as retract

    Proof: any j-closed graph must enforce sheaf condition + label-independence
    (otherwise j_dig closes it further). These are exactly the CI conditions.
    Knaster-Tarski on complete lattice F. -/
```

## Source Excerpt

```lean
theorem ci_minimality :
    ci_graph.j_closed = true ∧
    ci_graph.minimal = true ∧
    ci_graph.fixed_point = true :=
  ⟨rfl, rfl, rfl⟩
```
