---
{
  "projection_kind": "taulib_declaration",
  "title": "probe_naturality_is_tower_coherence",
  "permalink": "/verify/taulib/docs/book-ii-regularity-pre-yoneda/probe-naturality-is-tower-coherence/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Regularity.PreYoneda`.",
  "declaration_id": "TauLib.BookII.Regularity.PreYoneda::probe_naturality_is_tower_coherence",
  "declaration_slug": "probe-naturality-is-tower-coherence",
  "kind": "theorem",
  "name": "probe_naturality_is_tower_coherence",
  "module_name": "TauLib.BookII.Regularity.PreYoneda",
  "module_url": "/verify/taulib/docs/book-ii-regularity-pre-yoneda/",
  "source_line_start": 365,
  "source_line_end": 369,
  "registry_ids": [
    "II.R12"
  ],
  "related_registry_items": [
    {
      "id": "II.R12",
      "title": "Probe Naturality Equals Holomorphy",
      "url": "/registry/object/II.R12/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/PreYoneda.lean#L365-L369",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Regularity.PreYoneda",
        "url": "/verify/taulib/docs/book-ii-regularity-pre-yoneda/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/PreYoneda.lean#L365-L369",
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

- Module: [TauLib.BookII.Regularity.PreYoneda](/verify/taulib/docs/book-ii-regularity-pre-yoneda/)
- Source path: [`TauLib/BookII/Regularity/PreYoneda.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/PreYoneda.lean#L365-L369)
- Source range: L365-L369
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `II.R12` — Probe Naturality Equals Holomorphy

## Immediate Comment / Docstring

```lean
/-- [II.R12] Formal proof: probe naturality IS tower coherence.
    For the identity embedding, naturality at stage transition (k, k+1)
    is exactly reduction_compat. -/
```

## Source Excerpt

```lean
theorem probe_naturality_is_tower_coherence (x : TauIdx) {k l : TauIdx} (h : k ≤ l) :
    reduce (reduce x l) k = reduce x k :=
  reduction_compat x h

end Tau.BookII.Regularity
```
