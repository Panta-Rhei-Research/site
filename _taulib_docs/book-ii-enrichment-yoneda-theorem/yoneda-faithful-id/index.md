---
{
  "projection_kind": "taulib_declaration",
  "title": "yoneda_faithful_id",
  "permalink": "/verify/taulib/docs/book-ii-enrichment-yoneda-theorem/yoneda-faithful-id/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Enrichment.YonedaTheorem`.",
  "declaration_id": "TauLib.BookII.Enrichment.YonedaTheorem::yoneda_faithful_id",
  "declaration_slug": "yoneda-faithful-id",
  "kind": "theorem",
  "name": "yoneda_faithful_id",
  "module_name": "TauLib.BookII.Enrichment.YonedaTheorem",
  "module_url": "/verify/taulib/docs/book-ii-enrichment-yoneda-theorem/",
  "source_line_start": 316,
  "source_line_end": 324,
  "registry_ids": [
    "II.T36"
  ],
  "related_registry_items": [
    {
      "id": "II.T36",
      "title": "Tau-Yoneda Embedding",
      "url": "/registry/object/II.T36/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/YonedaTheorem.lean#L316-L324",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Enrichment.YonedaTheorem",
        "url": "/verify/taulib/docs/book-ii-enrichment-yoneda-theorem/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/YonedaTheorem.lean#L316-L324",
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

- Module: [TauLib.BookII.Enrichment.YonedaTheorem](/verify/taulib/docs/book-ii-enrichment-yoneda-theorem/)
- Source path: [`TauLib/BookII/Enrichment/YonedaTheorem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/YonedaTheorem.lean#L316-L324)
- Source range: L316-L324
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `II.T36` — Tau-Yoneda Embedding

## Immediate Comment / Docstring

```lean
/-- [II.T36] Formal proof: the pre-Yoneda embedding of the identity
    is faithful — Code extraction recovers the function.
    code_extract(fun a => preyoneda(id, a, k), k, x) = (reduce(x, k) : Int).

    Unfolding: code_extract f k x = f(reduce(x, k))
    where f(a) = preyoneda(reduce(·, k), a, k) = reduce(reduce(a, k), k).
    So the full expression is reduce(reduce(reduce(x, k), k), k) which
    collapses to reduce(x, k) by triple application of mod idempotence. -/
```

## Source Excerpt

```lean
theorem yoneda_faithful_id (x k : TauIdx) :
    code_extract (fun a => (preyoneda_embed_nat (fun n => reduce n k) a k : Int)) k x =
    (reduce x k : Int) := by
  simp only [code_extract, preyoneda_embed_nat, reduce]
  congr 1
  -- Goal: x % P_k % P_k % P_k = x % P_k
  have h1 := Nat.mod_mod_of_dvd x (dvd_refl (primorial k))
  -- h1 : x % P_k % P_k = x % P_k
  rw [h1, h1]
```
