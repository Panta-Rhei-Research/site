---
{
  "projection_kind": "taulib_declaration",
  "title": "probe_naturality_structural",
  "permalink": "/verify/taulib/docs/book-ii-enrichment-yoneda-theorem/probe-naturality-structural/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Enrichment.YonedaTheorem`.",
  "declaration_id": "TauLib.BookII.Enrichment.YonedaTheorem::probe_naturality_structural",
  "declaration_slug": "probe-naturality-structural",
  "kind": "theorem",
  "name": "probe_naturality_structural",
  "module_name": "TauLib.BookII.Enrichment.YonedaTheorem",
  "module_url": "/verify/taulib/docs/book-ii-enrichment-yoneda-theorem/",
  "source_line_start": 339,
  "source_line_end": 343,
  "registry_ids": [
    "II.L11"
  ],
  "related_registry_items": [
    {
      "id": "II.L11",
      "title": "Probe Naturality iff Yoneda",
      "url": "/registry/object/II.L11/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/YonedaTheorem.lean#L339-L343",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/YonedaTheorem.lean#L339-L343",
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
- Source path: [`TauLib/BookII/Enrichment/YonedaTheorem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/YonedaTheorem.lean#L339-L343)
- Source range: L339-L343
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `II.L11` — Probe Naturality iff Yoneda

## Immediate Comment / Docstring

```lean
/-- [II.L11] Formal proof: probe naturality IS tower coherence.
    For f = reduce(·, k), naturality at (x, k) reduces to
    reduce(reduce(x, k+1), k) = reduce(x, k), which is reduction_compat. -/
```

## Source Excerpt

```lean
theorem probe_naturality_structural (x : TauIdx) {k l : TauIdx} (h : k ≤ l) :
    reduce (reduce x l) k = reduce x k :=
  reduction_compat x h

end Tau.BookII.Enrichment
```
