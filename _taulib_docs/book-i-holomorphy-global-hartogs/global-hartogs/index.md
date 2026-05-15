---
{
  "projection_kind": "taulib_declaration",
  "title": "global_hartogs",
  "permalink": "/corpus/taulib/docs/book-i-holomorphy-global-hartogs/global-hartogs/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Holomorphy.GlobalHartogs`.",
  "declaration_id": "TauLib.BookI.Holomorphy.GlobalHartogs::global_hartogs",
  "declaration_slug": "global-hartogs",
  "kind": "theorem",
  "name": "global_hartogs",
  "module_name": "TauLib.BookI.Holomorphy.GlobalHartogs",
  "module_url": "/corpus/taulib/docs/book-i-holomorphy-global-hartogs/",
  "source_line_start": 67,
  "source_line_end": 69,
  "registry_ids": [
    "I.T31"
  ],
  "related_registry_items": [
    {
      "id": "I.T31",
      "title": "Global Hartogs Extension",
      "url": "/registry/object/I.T31/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/GlobalHartogs.lean#L67-L69",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Holomorphy.GlobalHartogs",
        "url": "/corpus/taulib/docs/book-i-holomorphy-global-hartogs/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/GlobalHartogs.lean#L67-L69",
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

- Module: [TauLib.BookI.Holomorphy.GlobalHartogs](/corpus/taulib/docs/book-i-holomorphy-global-hartogs/)
- Source path: [`TauLib/BookI/Holomorphy/GlobalHartogs.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/GlobalHartogs.lean#L67-L69)
- Source range: L67-L69
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- `I.T31` — Global Hartogs Extension

## Immediate Comment / Docstring

```lean
/-- [I.T31] The Global Hartogs Extension Theorem:
    Any two tower-coherent functions that agree at some reference depth
    agree at ALL depths ≤ that reference depth.

    Interpretation: if f is defined on L \ K and we can extend it
    to agree at depth d₀, then the extension is unique everywhere
    below d₀. The thin set K is "removable" because tower coherence
    forces the values on K to be determined by the surrounding data.

    Proof: direct application of the Identity Theorem (I.T21)
    which gives downward propagation of agreement via tower coherence. -/
```

## Source Excerpt

```lean
theorem global_hartogs (hd : HartogsData) :
    ∀ n k, k ≤ hd.depth → agree_at hd.f₁ hd.f₂ n k :=
  tau_identity_nat hd.f₁ hd.f₂ hd.coh₁ hd.coh₂ hd.depth hd.agree_ref
```
