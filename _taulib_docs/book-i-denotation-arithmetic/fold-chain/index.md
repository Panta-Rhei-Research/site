---
{
  "projection_kind": "taulib_declaration",
  "title": "fold_chain",
  "permalink": "/verify/taulib/docs/book-i-denotation-arithmetic/fold-chain/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Denotation.Arithmetic`.",
  "declaration_id": "TauLib.BookI.Denotation.Arithmetic::fold_chain",
  "declaration_slug": "fold-chain",
  "kind": "theorem",
  "name": "fold_chain",
  "module_name": "TauLib.BookI.Denotation.Arithmetic",
  "module_url": "/verify/taulib/docs/book-i-denotation-arithmetic/",
  "source_line_start": 135,
  "source_line_end": 140,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/Arithmetic.lean#L135-L140",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Denotation.Arithmetic",
        "url": "/verify/taulib/docs/book-i-denotation-arithmetic/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/Arithmetic.lean#L135-L140",
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

- Module: [TauLib.BookI.Denotation.Arithmetic](/verify/taulib/docs/book-i-denotation-arithmetic/)
- Source path: [`TauLib/BookI/Denotation/Arithmetic.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/Arithmetic.lean#L135-L140)
- Source range: L135-L140
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The Fold Chain Principle: each arithmetic level is obtained by
    structural recursion on the previous level.
    Ground truth: chunk_0060 (UR-ITER), chunk_0057 (counting = time). -/
```

## Source Excerpt

```lean
theorem fold_chain :
    (∀ n m, idx_add n m = (iter_rho m (toAlphaOrbit n)).depth) ∧
    (∀ n m, idx_mul n (m + 1) = idx_add (idx_mul n m) n) ∧
    (∀ n m, idx_exp n (m + 1) = idx_mul (idx_exp n m) n) ∧
    (∀ n m, idx_tetration n (m + 1) = idx_exp n (idx_tetration n m)) :=
  ⟨fun _ _ => rfl, fun _ _ => rfl, fun _ _ => rfl, fun _ _ => rfl⟩
```
