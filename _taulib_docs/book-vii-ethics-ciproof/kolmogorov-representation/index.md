---
{
  "projection_kind": "taulib_declaration",
  "title": "kolmogorov_representation",
  "permalink": "/verify/taulib/docs/book-vii-ethics-ciproof/kolmogorov-representation/",
  "summary_short": "`theorem` declaration in `TauLib.BookVII.Ethics.CIProof`.",
  "declaration_id": "TauLib.BookVII.Ethics.CIProof::kolmogorov_representation",
  "declaration_slug": "kolmogorov-representation",
  "kind": "theorem",
  "name": "kolmogorov_representation",
  "module_name": "TauLib.BookVII.Ethics.CIProof",
  "module_url": "/verify/taulib/docs/book-vii-ethics-ciproof/",
  "source_line_start": 698,
  "source_line_end": 701,
  "registry_ids": [
    "VII.T25"
  ],
  "related_registry_items": [
    {
      "id": "VII.T25",
      "title": "Kolmogorov Representation",
      "url": "/registry/object/VII.T25/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L698-L701",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L698-L701",
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
- Source path: [`TauLib/BookVII/Ethics/CIProof.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L698-L701)
- Source range: L698-L701
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `VII.T25` — Kolmogorov Representation

## Immediate Comment / Docstring

```lean
/-- [VII.T25] Kolmogorov Representation (ch40). Internal probability
    measures satisfy Kolmogorov axioms: they arise as normalized
    counting measures on NF-address subsets. No additional structure
    needed beyond NF-addresses + morphism counts. -/
```

## Source Excerpt

```lean
theorem kolmogorov_representation :
    internal_randomness.complexity_as_randomness = true ∧
    internal_randomness.deterministic_kernel = true :=
  ⟨rfl, rfl⟩
```
