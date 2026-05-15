---
{
  "projection_kind": "taulib_declaration",
  "title": "triangle_synthesis_at_17",
  "permalink": "/corpus/taulib/docs/book-i-polarity-h2-h3-classifier-bridge/triangle-synthesis-at-17/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Polarity.H2H3ClassifierBridge`.",
  "declaration_id": "TauLib.BookI.Polarity.H2H3ClassifierBridge::triangle_synthesis_at_17",
  "declaration_slug": "triangle-synthesis-at-17",
  "kind": "theorem",
  "name": "triangle_synthesis_at_17",
  "module_name": "TauLib.BookI.Polarity.H2H3ClassifierBridge",
  "module_url": "/corpus/taulib/docs/book-i-polarity-h2-h3-classifier-bridge/",
  "source_line_start": 174,
  "source_line_end": 180,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/H2H3ClassifierBridge.lean#L174-L180",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Polarity.H2H3ClassifierBridge",
        "url": "/corpus/taulib/docs/book-i-polarity-h2-h3-classifier-bridge/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/H2H3ClassifierBridge.lean#L174-L180",
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

- Module: [TauLib.BookI.Polarity.H2H3ClassifierBridge](/corpus/taulib/docs/book-i-polarity-h2-h3-classifier-bridge/)
- Source path: [`TauLib/BookI/Polarity/H2H3ClassifierBridge.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/H2H3ClassifierBridge.lean#L174-L180)
- Source range: L174-L180
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Three-way synthesis at p = 17** (the second B-class prime). -/
```

## Source Excerpt

```lean
theorem triangle_synthesis_at_17 :
    chi legendreBClass 17 = Pol 17 ∧
    Pol 17 = labelInfty 6 ∧
    chi legendreBClass 17 = labelInfty 6 :=
  ⟨chi_legendre_eq_Pol_at_17,
   Pol_eq_labelInfty_at_seventeen,
   by native_decide⟩
```
