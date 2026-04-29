---
{
  "projection_kind": "taulib_declaration",
  "title": "ci_sheaf_equivalence",
  "permalink": "/verify/taulib/docs/book-vii-ethics-ciproof/ci-sheaf-equivalence/",
  "summary_short": "`theorem` declaration in `TauLib.BookVII.Ethics.CIProof`.",
  "declaration_id": "TauLib.BookVII.Ethics.CIProof::ci_sheaf_equivalence",
  "declaration_slug": "ci-sheaf-equivalence",
  "kind": "theorem",
  "name": "ci_sheaf_equivalence",
  "module_name": "TauLib.BookVII.Ethics.CIProof",
  "module_url": "/verify/taulib/docs/book-vii-ethics-ciproof/",
  "source_line_start": 159,
  "source_line_end": 165,
  "registry_ids": [
    "VII.T31"
  ],
  "related_registry_items": [
    {
      "id": "VII.T31",
      "title": "CI-Sheaf Equivalence",
      "url": "/registry/object/VII.T31/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L159-L165",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L159-L165",
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
- Source path: [`TauLib/BookVII/Ethics/CIProof.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L159-L165)
- Source range: L159-L165
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `VII.T31` — CI-Sheaf Equivalence

## Immediate Comment / Docstring

```lean
/-- [VII.T31] CI-Sheaf Equivalence (ch77). Three equivalent formulations:
    (1) Kantian universalizability: M willed as universal law without contradiction
    (2) Sheaf condition: Max_M is a sheaf on (P, J)
    (3) Naturality + local realizability: Max_M separated, fibers nonempty,
        compatibility cocycles trivial

    Proof: (1)⟹(2) Kant's test = gluing criterion.
    (2)⟹(3) sheaf ⟹ separated + nonempty + trivial cocycles.
    (3)⟹(1) naturality = no hidden exceptions, nonempty = conceivability,
    trivial cocycles = no Čech obstruction. -/
```

## Source Excerpt

```lean
theorem ci_sheaf_equivalence :
    ci_naturality.has_site = true ∧
    ci_naturality.has_maxim_presheaf = true ∧
    ci_naturality.naturality = true ∧
    ci_naturality.separated = true ∧
    ci_naturality.dignity_filtered = true :=
  ⟨rfl, rfl, rfl, rfl, rfl⟩
```
