---
{
  "projection_kind": "taulib_declaration",
  "title": "eval_morphism",
  "permalink": "/verify/taulib/docs/book-i-topos-internal-hom/eval-morphism/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Topos.InternalHom`.",
  "declaration_id": "TauLib.BookI.Topos.InternalHom::eval_morphism",
  "declaration_slug": "eval-morphism",
  "kind": "theorem",
  "name": "eval_morphism",
  "module_name": "TauLib.BookI.Topos.InternalHom",
  "module_url": "/verify/taulib/docs/book-i-topos-internal-hom/",
  "source_line_start": 76,
  "source_line_end": 80,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/InternalHom.lean#L76-L80",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/InternalHom.lean#L76-L80",
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
- Source path: [`TauLib/BookI/Topos/InternalHom.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/InternalHom.lean#L76-L80)
- Source range: L76-L80
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Evaluation morphism: (Q^P × P) → Q. -/
```

## Source Excerpt

```lean
theorem eval_morphism (P Q : Presheaf) (x : TauIdx) :
    (cat_product (internal_hom P Q) P).support x = true →
    Q.support x = true := by
  simp only [cat_product, presheaf_product, internal_hom]
  cases hp : P.support x <;> cases hq : Q.support x <;> simp_all
```
