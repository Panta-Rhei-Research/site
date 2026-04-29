---
{
  "projection_kind": "taulib_declaration",
  "title": "yoneda_full_id",
  "permalink": "/verify/taulib/docs/book-ii-enrichment-yoneda-theorem/yoneda-full-id/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Enrichment.YonedaTheorem`.",
  "declaration_id": "TauLib.BookII.Enrichment.YonedaTheorem::yoneda_full_id",
  "declaration_slug": "yoneda-full-id",
  "kind": "theorem",
  "name": "yoneda_full_id",
  "module_name": "TauLib.BookII.Enrichment.YonedaTheorem",
  "module_url": "/verify/taulib/docs/book-ii-enrichment-yoneda-theorem/",
  "source_line_start": 331,
  "source_line_end": 334,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/YonedaTheorem.lean#L331-L334",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/YonedaTheorem.lean#L331-L334",
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
- Source path: [`TauLib/BookII/Enrichment/YonedaTheorem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/YonedaTheorem.lean#L331-L334)
- Source range: L331-L334
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `II.T36` — Tau-Yoneda Embedding

## Immediate Comment / Docstring

```lean
/-- [II.T36] Formal proof: fullness of the Yoneda embedding.
    For any tower-coherent g given by g(x, k) = reduce(x, k),
    preyoneda(g_k, x, k) = g(x, k).

    preyoneda(reduce(·, k), x, k) = reduce(reduce(x, k), k) = reduce(x, k). -/
```

## Source Excerpt

```lean
theorem yoneda_full_id (x k : TauIdx) :
    preyoneda_embed_nat (fun n => reduce n k) x k = reduce x k := by
  simp only [preyoneda_embed_nat, reduce]
  exact Nat.mod_mod_of_dvd x (dvd_refl (primorial k))
```
