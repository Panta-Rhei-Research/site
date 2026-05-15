---
{
  "projection_kind": "taulib_declaration",
  "title": "functorial_12_4",
  "permalink": "/corpus/taulib/docs/book-ii-regularity-idempotent-decomposition/functorial-12-4/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Regularity.IdempotentDecomposition`.",
  "declaration_id": "TauLib.BookII.Regularity.IdempotentDecomposition::functorial_12_4",
  "declaration_slug": "functorial-12-4",
  "kind": "theorem",
  "name": "functorial_12_4",
  "module_name": "TauLib.BookII.Regularity.IdempotentDecomposition",
  "module_url": "/corpus/taulib/docs/book-ii-regularity-idempotent-decomposition/",
  "source_line_start": 317,
  "source_line_end": 318,
  "registry_ids": [
    "II.P10"
  ],
  "related_registry_items": [
    {
      "id": "II.P10",
      "title": "Functions as Tau-Objects",
      "url": "/registry/object/II.P10/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/IdempotentDecomposition.lean#L317-L318",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Regularity.IdempotentDecomposition",
        "url": "/corpus/taulib/docs/book-ii-regularity-idempotent-decomposition/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/IdempotentDecomposition.lean#L317-L318",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "role": "proof obligation",
      "status": "formal proof obligation checked"
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

- Module: [TauLib.BookII.Regularity.IdempotentDecomposition](/corpus/taulib/docs/book-ii-regularity-idempotent-decomposition/)
- Source path: [`TauLib/BookII/Regularity/IdempotentDecomposition.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/IdempotentDecomposition.lean#L317-L318)
- Source range: L317-L318
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- `II.P10` — Functions as Tau-Objects

## Immediate Comment / Docstring

```lean
-- Functoriality [II.P10]
```

## Source Excerpt

```lean
theorem functorial_12_4 :
    decompose_functorial_check 12 4 = true := by native_decide
```
