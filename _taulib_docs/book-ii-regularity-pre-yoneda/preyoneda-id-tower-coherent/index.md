---
{
  "projection_kind": "taulib_declaration",
  "title": "preyoneda_id_tower_coherent",
  "permalink": "/verify/taulib/docs/book-ii-regularity-pre-yoneda/preyoneda-id-tower-coherent/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Regularity.PreYoneda`.",
  "declaration_id": "TauLib.BookII.Regularity.PreYoneda::preyoneda_id_tower_coherent",
  "declaration_slug": "preyoneda-id-tower-coherent",
  "kind": "theorem",
  "name": "preyoneda_id_tower_coherent",
  "module_name": "TauLib.BookII.Regularity.PreYoneda",
  "module_url": "/verify/taulib/docs/book-ii-regularity-pre-yoneda/",
  "source_line_start": 356,
  "source_line_end": 360,
  "registry_ids": [
    "II.D50"
  ],
  "related_registry_items": [
    {
      "id": "II.D50",
      "title": "Pre-Yoneda Embedding",
      "url": "/registry/object/II.D50/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/PreYoneda.lean#L356-L360",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Regularity.PreYoneda",
        "url": "/verify/taulib/docs/book-ii-regularity-pre-yoneda/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/PreYoneda.lean#L356-L360",
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

- Module: [TauLib.BookII.Regularity.PreYoneda](/verify/taulib/docs/book-ii-regularity-pre-yoneda/)
- Source path: [`TauLib/BookII/Regularity/PreYoneda.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/PreYoneda.lean#L356-L360)
- Source range: L356-L360
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `II.D50` — Pre-Yoneda Embedding

## Immediate Comment / Docstring

```lean
/-- [II.D50] Formal proof: the pre-Yoneda embedding of the identity
    function is tower-coherent.

    preyoneda(id, x, k) = reduce(x, k), so tower coherence reduces to
    reduce(reduce(x, k+1), k) = reduce(x, k), which is reduction_compat. -/
```

## Source Excerpt

```lean
theorem preyoneda_id_tower_coherent (x : TauIdx) {k l : TauIdx} (h : k ≤ l) :
    reduce (preyoneda_embed_nat (fun n => n) x l) k =
    preyoneda_embed_nat (fun n => n) x k := by
  simp only [preyoneda_embed_nat]
  exact reduction_compat x h
```
