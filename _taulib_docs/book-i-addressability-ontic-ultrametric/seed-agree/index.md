---
{
  "projection_kind": "taulib_declaration",
  "title": "seedAgree",
  "permalink": "/verify/taulib/docs/book-i-addressability-ontic-ultrametric/seed-agree/",
  "summary_short": "`def` declaration in `TauLib.BookI.Addressability.OnticUltrametric`.",
  "declaration_id": "TauLib.BookI.Addressability.OnticUltrametric::seedAgree",
  "declaration_slug": "seed-agree",
  "kind": "def",
  "name": "seedAgree",
  "module_name": "TauLib.BookI.Addressability.OnticUltrametric",
  "module_url": "/verify/taulib/docs/book-i-addressability-ontic-ultrametric/",
  "source_line_start": 55,
  "source_line_end": 63,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Addressability/OnticUltrametric.lean#L55-L63",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Addressability/OnticUltrametric.lean#L55-L63",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "status": "defined"
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
- Source path: [`TauLib/BookI/Addressability/OnticUltrametric.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Addressability/OnticUltrametric.lean#L55-L63)
- Source range: L55-L63
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Pointwise equality of two seed-maps over the 5-generator enumeration. -/
```

## Source Excerpt

```lean
def seedAgree (f g : Generator → Generator) : Prop :=
  f Generator.alpha = g Generator.alpha
    ∧ f Generator.pi = g Generator.pi
    ∧ f Generator.gamma = g Generator.gamma
    ∧ f Generator.eta = g Generator.eta
    ∧ f Generator.omega = g Generator.omega

instance (f g : Generator → Generator) : Decidable (seedAgree f g) := by
  unfold seedAgree; infer_instance
```
