---
{
  "projection_kind": "taulib_declaration",
  "title": "e2_strict_3",
  "permalink": "/verify/taulib/docs/book-iii-computation-e2-witness/e2-strict-3/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Computation.E2Witness`.",
  "declaration_id": "TauLib.BookIII.Computation.E2Witness::e2_strict_3",
  "declaration_slug": "e2-strict-3",
  "kind": "theorem",
  "name": "e2_strict_3",
  "module_name": "TauLib.BookIII.Computation.E2Witness",
  "module_url": "/verify/taulib/docs/book-iii-computation-e2-witness/",
  "source_line_start": 226,
  "source_line_end": 227,
  "registry_ids": [
    "III.P34"
  ],
  "related_registry_items": [
    {
      "id": "III.P34",
      "title": "E₂ ⊋ E₁ Strict Witness",
      "url": "/registry/object/III.P34/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/E2Witness.lean#L226-L227",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Computation.E2Witness",
        "url": "/verify/taulib/docs/book-iii-computation-e2-witness/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/E2Witness.lean#L226-L227",
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

- Module: [TauLib.BookIII.Computation.E2Witness](/verify/taulib/docs/book-iii-computation-e2-witness/)
- Source path: [`TauLib/BookIII/Computation/E2Witness.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/E2Witness.lean#L226-L227)
- Source range: L226-L227
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.P34` — E₂ ⊋ E₁ Strict Witness

## Immediate Comment / Docstring

```lean
/-- [III.P34] E₂ strict witness at depth 3. -/
```

## Source Excerpt

```lean
theorem e2_strict_3 :
    e2_strict_witness_check 3 = true := by native_decide
```
