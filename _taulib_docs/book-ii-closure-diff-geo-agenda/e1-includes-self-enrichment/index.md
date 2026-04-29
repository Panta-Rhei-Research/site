---
{
  "projection_kind": "taulib_declaration",
  "title": "e1_includes_self_enrichment",
  "permalink": "/verify/taulib/docs/book-ii-closure-diff-geo-agenda/e1-includes-self-enrichment/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Closure.DiffGeoAgenda`.",
  "declaration_id": "TauLib.BookII.Closure.DiffGeoAgenda::e1_includes_self_enrichment",
  "declaration_slug": "e1-includes-self-enrichment",
  "kind": "theorem",
  "name": "e1_includes_self_enrichment",
  "module_name": "TauLib.BookII.Closure.DiffGeoAgenda",
  "module_url": "/verify/taulib/docs/book-ii-closure-diff-geo-agenda/",
  "source_line_start": 160,
  "source_line_end": 168,
  "registry_ids": [
    "II.R22"
  ],
  "related_registry_items": [
    {
      "id": "II.R22",
      "title": "Enrichment Ladder Forward Declaration",
      "url": "/registry/object/II.R22/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/DiffGeoAgenda.lean#L160-L168",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Closure.DiffGeoAgenda",
        "url": "/verify/taulib/docs/book-ii-closure-diff-geo-agenda/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/DiffGeoAgenda.lean#L160-L168",
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

- Module: [TauLib.BookII.Closure.DiffGeoAgenda](/verify/taulib/docs/book-ii-closure-diff-geo-agenda/)
- Source path: [`TauLib/BookII/Closure/DiffGeoAgenda.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/DiffGeoAgenda.lean#L160-L168)
- Source range: L160-L168
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `II.R22` — Enrichment Ladder Forward Declaration

## Immediate Comment / Docstring

```lean
/-- [II.R22] E1 completeness implies self-enrichment witness holds.
    This is structural: e1_layer_check includes self-enrichment.
    If the full layer check passes, then in particular the
    self-enrichment component is true. -/
```

## Source Excerpt

```lean
theorem e1_includes_self_enrichment (bound db k_max : TauIdx) :
    e1_layer_check bound db k_max = true ->
    e1_self_enrichment_witness bound db = true := by
  intro h
  simp only [e1_layer_check, compute_e1_layer] at h
  revert h
  cases e1_self_enrichment_witness bound db <;> simp

end Tau.BookII.Closure
```
