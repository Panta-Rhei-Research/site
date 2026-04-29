---
{
  "projection_kind": "taulib_declaration",
  "title": "h2_h3_unified_classifier_at_seven",
  "permalink": "/verify/taulib/docs/book-i-polarity-h2-h3-classifier-bridge/h2-h3-unified-classifier-at-seven/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Polarity.H2H3ClassifierBridge`.",
  "declaration_id": "TauLib.BookI.Polarity.H2H3ClassifierBridge::h2_h3_unified_classifier_at_seven",
  "declaration_slug": "h2-h3-unified-classifier-at-seven",
  "kind": "theorem",
  "name": "h2_h3_unified_classifier_at_seven",
  "module_name": "TauLib.BookI.Polarity.H2H3ClassifierBridge",
  "module_url": "/verify/taulib/docs/book-i-polarity-h2-h3-classifier-bridge/",
  "source_line_start": 227,
  "source_line_end": 234,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/H2H3ClassifierBridge.lean#L227-L234",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/H2H3ClassifierBridge.lean#L227-L234",
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
- Source path: [`TauLib/BookI/Polarity/H2H3ClassifierBridge.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/H2H3ClassifierBridge.lean#L227-L234)
- Source range: L227-L234
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **The H2-H3 unified classifier corollary** (closes the
    structural circle):

    Wave 17 (abstract `chi` over B_class) with Wave 19a's concrete
    `legendreBClass` instantiation **IS** Wave 19a's `Pol` **IS**
    Wave 18's `labelInfty` (composed with `nth_prime`).

    Three different paper sections (paper §7.4, paper-prime-polarity
    §6, paper-prime-polarity §7) yield the same classifier on
    primes — and TauLib verifies this end-to-end. -/
```

## Source Excerpt

```lean
theorem h2_h3_unified_classifier_at_seven :
    -- All three classifiers agree at p_4 = 7 (first B-class prime)
    chi legendreBClass 7 = labelInfty 3 ∧
    chi legendreBClass 7 = Pol 7 ∧
    Pol 7 = labelInfty 3 := by
  refine ⟨?_, ?_, ?_⟩ <;> native_decide

end Tau.Polarity
```
