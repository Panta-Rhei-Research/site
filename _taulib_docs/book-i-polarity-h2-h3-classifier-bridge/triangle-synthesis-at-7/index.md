---
{
  "projection_kind": "taulib_declaration",
  "title": "triangle_synthesis_at_7",
  "permalink": "/verify/taulib/docs/book-i-polarity-h2-h3-classifier-bridge/triangle-synthesis-at-7/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Polarity.H2H3ClassifierBridge`.",
  "declaration_id": "TauLib.BookI.Polarity.H2H3ClassifierBridge::triangle_synthesis_at_7",
  "declaration_slug": "triangle-synthesis-at-7",
  "kind": "theorem",
  "name": "triangle_synthesis_at_7",
  "module_name": "TauLib.BookI.Polarity.H2H3ClassifierBridge",
  "module_url": "/verify/taulib/docs/book-i-polarity-h2-h3-classifier-bridge/",
  "source_line_start": 165,
  "source_line_end": 171,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/H2H3ClassifierBridge.lean#L165-L171",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/H2H3ClassifierBridge.lean#L165-L171",
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
- Source path: [`TauLib/BookI/Polarity/H2H3ClassifierBridge.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/H2H3ClassifierBridge.lean#L165-L171)
- Source range: L165-L171
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Three-way synthesis at p = 7** (the first B-class prime):
    Wave 17's `chi`, Wave 19a's `Pol`, and Wave 18's `labelInfty`
    all agree.

    `chi(legendre)(7) = Pol(7) = labelInfty(3) = +1`. -/
```

## Source Excerpt

```lean
theorem triangle_synthesis_at_7 :
    chi legendreBClass 7 = Pol 7 ∧
    Pol 7 = labelInfty 3 ∧
    chi legendreBClass 7 = labelInfty 3 :=
  ⟨chi_legendre_eq_Pol_at_7,
   Pol_eq_labelInfty_at_seven,
   by native_decide⟩
```
