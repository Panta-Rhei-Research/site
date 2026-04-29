---
{
  "projection_kind": "taulib_declaration",
  "title": "CayleyDist_compose_left",
  "permalink": "/verify/taulib/docs/book-i-addressability-cayley-metric/cayley-dist-compose-left/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Addressability.CayleyMetric`.",
  "declaration_id": "TauLib.BookI.Addressability.CayleyMetric::CayleyDist_compose_left",
  "declaration_slug": "cayley-dist-compose-left",
  "kind": "theorem",
  "name": "CayleyDist_compose_left",
  "module_name": "TauLib.BookI.Addressability.CayleyMetric",
  "module_url": "/verify/taulib/docs/book-i-addressability-cayley-metric/",
  "source_line_start": 121,
  "source_line_end": 128,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Addressability/CayleyMetric.lean#L121-L128",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Addressability.CayleyMetric",
        "url": "/verify/taulib/docs/book-i-addressability-cayley-metric/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Addressability/CayleyMetric.lean#L121-L128",
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

- Module: [TauLib.BookI.Addressability.CayleyMetric](/verify/taulib/docs/book-i-addressability-cayley-metric/)
- Source path: [`TauLib/BookI/Addressability/CayleyMetric.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Addressability/CayleyMetric.lean#L121-L128)
- Source range: L121-L128
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Symmetric: composition on the left preserves distance. -/
```

## Source Excerpt

```lean
theorem CayleyDist_compose_left (a b c : NormalForm) :
    CayleyDist (c.compose a) (c.compose b)
      = CayleyDist a b := by
  unfold CayleyDist NormalForm.compose
  unfold natAbsDiff
  simp; omega

end Tau.Addressability
```
