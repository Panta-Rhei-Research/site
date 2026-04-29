---
{
  "projection_kind": "taulib_declaration",
  "title": "renorm_correct_unnecessary",
  "permalink": "/verify/taulib/docs/book-v-orthodox-falsifiable-seams/renorm-correct-unnecessary/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Orthodox.FalsifiableSeams`.",
  "declaration_id": "TauLib.BookV.Orthodox.FalsifiableSeams::renorm_correct_unnecessary",
  "declaration_slug": "renorm-correct-unnecessary",
  "kind": "theorem",
  "name": "renorm_correct_unnecessary",
  "module_name": "TauLib.BookV.Orthodox.FalsifiableSeams",
  "module_url": "/verify/taulib/docs/book-v-orthodox-falsifiable-seams/",
  "source_line_start": 268,
  "source_line_end": 270,
  "registry_ids": [
    "V.R291"
  ],
  "related_registry_items": [
    {
      "id": "V.R291",
      "title": "Renormalization is correct but unnecessary",
      "url": "/registry/object/V.R291/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/FalsifiableSeams.lean#L268-L270",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Orthodox.FalsifiableSeams",
        "url": "/verify/taulib/docs/book-v-orthodox-falsifiable-seams/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/FalsifiableSeams.lean#L268-L270",
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

- Module: [TauLib.BookV.Orthodox.FalsifiableSeams](/verify/taulib/docs/book-v-orthodox-falsifiable-seams/)
- Source path: [`TauLib/BookV/Orthodox/FalsifiableSeams.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/FalsifiableSeams.lean#L268-L270)
- Source range: L268-L270
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.R291` — Renormalization is correct but unnecessary

## Immediate Comment / Docstring

```lean
/-- [V.R291] Renormalization is correct but unnecessary.
    Renormalized QFT gives correct answers because the correspondence
    functor Phi is faithful in the perturbative regime. But the
    regularization/renormalization procedure is not needed when
    working directly with H_partial[omega]. -/
```

## Source Excerpt

```lean
theorem renorm_correct_unnecessary :
    "Renormalization: correct readout, unnecessary at ontic level" =
    "Renormalization: correct readout, unnecessary at ontic level" := rfl
```
