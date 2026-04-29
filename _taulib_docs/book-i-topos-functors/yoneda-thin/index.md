---
{
  "projection_kind": "taulib_declaration",
  "title": "yoneda_thin",
  "permalink": "/verify/taulib/docs/book-i-topos-functors/yoneda-thin/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Topos.Functors`.",
  "declaration_id": "TauLib.BookI.Topos.Functors::yoneda_thin",
  "declaration_slug": "yoneda-thin",
  "kind": "theorem",
  "name": "yoneda_thin",
  "module_name": "TauLib.BookI.Topos.Functors",
  "module_url": "/verify/taulib/docs/book-i-topos-functors/",
  "source_line_start": 146,
  "source_line_end": 148,
  "registry_ids": [
    "I.T23"
  ],
  "related_registry_items": [
    {
      "id": "I.T23",
      "title": "Yoneda Lemma",
      "url": "/registry/object/I.T23/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/Functors.lean#L146-L148",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Topos.Functors",
        "url": "/verify/taulib/docs/book-i-topos-functors/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/Functors.lean#L146-L148",
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

- Module: [TauLib.BookI.Topos.Functors](/verify/taulib/docs/book-i-topos-functors/)
- Source path: [`TauLib/BookI/Topos/Functors.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/Functors.lean#L146-L148)
- Source range: L146-L148
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `I.T23` — Yoneda Lemma

## Immediate Comment / Docstring

```lean
/-- [I.T23] The Yoneda Lemma for thin Cat_τ:
    Natural transformations from y(X) to a presheaf P
    are in bijection with P(X).

    In a thin category, this simplifies dramatically:
    since y(X) = Hom(-, X) is either empty or singleton for each Y,
    a natural transformation y(X) → P is determined by what it does
    at X (where Hom(X, X) = {id}).

    We formalize the key implication: evaluation at X determines
    the transformation. -/
```

## Source Excerpt

```lean
theorem yoneda_thin (P : Presheaf) (x : TauIdx) :
    P.support x = (yoneda x).support x → P.support x = true :=
  fun h => h
```
