---
{
  "projection_kind": "taulib_declaration",
  "title": "chi_legendre_eq_Pol_at_23",
  "permalink": "/verify/taulib/docs/book-i-polarity-h2-h3-classifier-bridge/chi-legendre-eq-pol-at-23/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Polarity.H2H3ClassifierBridge`.",
  "declaration_id": "TauLib.BookI.Polarity.H2H3ClassifierBridge::chi_legendre_eq_Pol_at_23",
  "declaration_slug": "chi-legendre-eq-pol-at-23",
  "kind": "theorem",
  "name": "chi_legendre_eq_Pol_at_23",
  "module_name": "TauLib.BookI.Polarity.H2H3ClassifierBridge",
  "module_url": "/verify/taulib/docs/book-i-polarity-h2-h3-classifier-bridge/",
  "source_line_start": 111,
  "source_line_end": 112,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/H2H3ClassifierBridge.lean#L111-L112",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Polarity.H2H3ClassifierBridge",
        "url": "/verify/taulib/docs/book-i-polarity-h2-h3-classifier-bridge/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/H2H3ClassifierBridge.lean#L111-L112",
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

- Module: [TauLib.BookI.Polarity.H2H3ClassifierBridge](/verify/taulib/docs/book-i-polarity-h2-h3-classifier-bridge/)
- Source path: [`TauLib/BookI/Polarity/H2H3ClassifierBridge.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/H2H3ClassifierBridge.lean#L111-L112)
- Source range: L111-L112
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Wave 17 ↔ Wave 18-19a bridge at p = 23. -/
```

## Source Excerpt

```lean
theorem chi_legendre_eq_Pol_at_23 :
    chi legendreBClass 23 = Pol 23 := by native_decide
```
