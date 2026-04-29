---
{
  "projection_kind": "taulib_declaration",
  "title": "self_enrichment",
  "permalink": "/verify/taulib/docs/book-i-topos-internal-hom/self-enrichment/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Topos.InternalHom`.",
  "declaration_id": "TauLib.BookI.Topos.InternalHom::self_enrichment",
  "declaration_slug": "self-enrichment",
  "kind": "theorem",
  "name": "self_enrichment",
  "module_name": "TauLib.BookI.Topos.InternalHom",
  "module_url": "/verify/taulib/docs/book-i-topos-internal-hom/",
  "source_line_start": 89,
  "source_line_end": 91,
  "registry_ids": [
    "I.P28"
  ],
  "related_registry_items": [
    {
      "id": "I.P28",
      "title": "Self-Enrichment",
      "url": "/registry/object/I.P28/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/InternalHom.lean#L89-L91",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Topos.InternalHom",
        "url": "/verify/taulib/docs/book-i-topos-internal-hom/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/InternalHom.lean#L89-L91",
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

- Module: [TauLib.BookI.Topos.InternalHom](/verify/taulib/docs/book-i-topos-internal-hom/)
- Source path: [`TauLib/BookI/Topos/InternalHom.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/InternalHom.lean#L89-L91)
- Source range: L89-L91
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `I.P28` — Self-Enrichment

## Immediate Comment / Docstring

```lean
/-- [I.P28] E_τ is self-enriched: internal hom gives an
    internal presheaf of morphisms.
    Witness: internal_hom P Q is itself a Presheaf. -/
```

## Source Excerpt

```lean
theorem self_enrichment (P Q : Presheaf) :
    ∃ R : Presheaf, R = internal_hom P Q :=
  ⟨internal_hom P Q, rfl⟩
```
