---
{
  "projection_kind": "taulib_declaration",
  "title": "OnticDist_distinct",
  "permalink": "/corpus/taulib/docs/book-i-addressability-ontic-ultrametric/ontic-dist-distinct/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Addressability.OnticUltrametric`.",
  "declaration_id": "TauLib.BookI.Addressability.OnticUltrametric::OnticDist_distinct",
  "declaration_slug": "ontic-dist-distinct",
  "kind": "theorem",
  "name": "OnticDist_distinct",
  "module_name": "TauLib.BookI.Addressability.OnticUltrametric",
  "module_url": "/corpus/taulib/docs/book-i-addressability-ontic-ultrametric/",
  "source_line_start": 161,
  "source_line_end": 163,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Addressability/OnticUltrametric.lean#L161-L163",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Addressability.OnticUltrametric",
        "url": "/corpus/taulib/docs/book-i-addressability-ontic-ultrametric/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Addressability/OnticUltrametric.lean#L161-L163",
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

- Module: [TauLib.BookI.Addressability.OnticUltrametric](/corpus/taulib/docs/book-i-addressability-ontic-ultrametric/)
- Source path: [`TauLib/BookI/Addressability/OnticUltrametric.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Addressability/OnticUltrametric.lean#L161-L163)
- Source range: L161-L163
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Distinct NF-equivalence classes are at maximum distance — a
    formal expression of *total disconnection* for the ontic
    ultrametric. -/
```

## Source Excerpt

```lean
theorem OnticDist_distinct (nf₁ nf₂ : NormalForm) (h : ¬ nfEquiv nf₁ nf₂) :
    OnticDist nf₁ nf₂ = 1 := by
  unfold OnticDist; rw [if_neg h]
```
