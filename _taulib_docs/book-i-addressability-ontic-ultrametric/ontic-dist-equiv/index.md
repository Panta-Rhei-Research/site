---
{
  "projection_kind": "taulib_declaration",
  "title": "OnticDist_equiv",
  "permalink": "/verify/taulib/docs/book-i-addressability-ontic-ultrametric/ontic-dist-equiv/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Addressability.OnticUltrametric`.",
  "declaration_id": "TauLib.BookI.Addressability.OnticUltrametric::OnticDist_equiv",
  "declaration_slug": "ontic-dist-equiv",
  "kind": "theorem",
  "name": "OnticDist_equiv",
  "module_name": "TauLib.BookI.Addressability.OnticUltrametric",
  "module_url": "/verify/taulib/docs/book-i-addressability-ontic-ultrametric/",
  "source_line_start": 167,
  "source_line_end": 171,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Addressability/OnticUltrametric.lean#L167-L171",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Addressability.OnticUltrametric",
        "url": "/verify/taulib/docs/book-i-addressability-ontic-ultrametric/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Addressability/OnticUltrametric.lean#L167-L171",
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

- Module: [TauLib.BookI.Addressability.OnticUltrametric](/verify/taulib/docs/book-i-addressability-ontic-ultrametric/)
- Source path: [`TauLib/BookI/Addressability/OnticUltrametric.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Addressability/OnticUltrametric.lean#L167-L171)
- Source range: L167-L171
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Equivalent NFs are at distance 0 — the *zero* ball of the
    ontic ultrametric is the NF-equivalence class. -/
```

## Source Excerpt

```lean
theorem OnticDist_equiv (nf₁ nf₂ : NormalForm) (h : nfEquiv nf₁ nf₂) :
    OnticDist nf₁ nf₂ = 0 := by
  unfold OnticDist; rw [if_pos h]

end Tau.Addressability
```
