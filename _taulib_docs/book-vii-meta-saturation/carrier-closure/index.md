---
{
  "projection_kind": "taulib_declaration",
  "title": "carrier_closure",
  "permalink": "/verify/taulib/docs/book-vii-meta-saturation/carrier-closure/",
  "summary_short": "`theorem` declaration in `TauLib.BookVII.Meta.Saturation`.",
  "declaration_id": "TauLib.BookVII.Meta.Saturation::carrier_closure",
  "declaration_slug": "carrier-closure",
  "kind": "theorem",
  "name": "carrier_closure",
  "module_name": "TauLib.BookVII.Meta.Saturation",
  "module_url": "/verify/taulib/docs/book-vii-meta-saturation/",
  "source_line_start": 274,
  "source_line_end": 277,
  "registry_ids": [
    "VII.L07"
  ],
  "related_registry_items": [
    {
      "id": "VII.L07",
      "title": "Carrier Closure Lemma",
      "url": "/registry/object/VII.L07/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Saturation.lean#L274-L277",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVII.Meta.Saturation",
        "url": "/verify/taulib/docs/book-vii-meta-saturation/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Saturation.lean#L274-L277",
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

- Module: [TauLib.BookVII.Meta.Saturation](/verify/taulib/docs/book-vii-meta-saturation/)
- Source path: [`TauLib/BookVII/Meta/Saturation.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Saturation.lean#L274-L277)
- Source range: L274-L277
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `VII.L07` — Carrier Closure Lemma

## Immediate Comment / Docstring

```lean
/-- [VII.L07] Carrier Closure: SelfDesc³ = SelfDesc². MetaDecode at level 3
    models only what level 2 already models. The model includes its own
    modelling capacity. M₃(X) = M₂(M₂(X)) ⊆ M₂(X). -/
```

## Source Excerpt

```lean
theorem carrier_closure :
    let sd := SelfDescIteration.mk 3 2
    sd.depth = 3 ∧ sd.idempotent_from = 2 :=
  ⟨rfl, rfl⟩
```
